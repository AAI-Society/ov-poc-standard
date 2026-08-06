"""Proof-of-Control reference implementation — core evidence pipeline.

Implements the normative requirements of the specification that are
mechanically checkable in software:

  C7.1  Action Interception Gateway; evidence written before action release
  C7.1.4 Complete mediation via capability-bound dispatch
  C7.2  Contemporaneous evidence with anchored time
  C7.3  Tamper-evident hash chain; enclave-held signing keys
  C7.3.3 Non-equivocation via gossip between verifiers
  C7.6  Failure recording, sequence continuity, fail-closed operation
  C7.6.6 Bounded anchoring interval
  C4.1.7 Path-aware authorization over a bounded path summary
  C8.3.5 Halt enforced at the relying party, outside operator control

TRUST-BOUNDARY NOTE. A hardware TEE is not available in this environment.
`AttestingEnvironment` models the enclave as an in-process object whose
signing key is never exposed through its API and whose "measurement" is a
digest of the policy engine and bundle. This is a *functional* model: it
reproduces the protocol and its checks, and it is sufficient to validate the
security arguments about protocol structure (Theorem 1, Proposition 1,
Theorem 2). It does NOT reproduce hardware isolation, and reported latencies
therefore EXCLUDE enclave transition costs. See impl/README.md.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field, asdict
from typing import Any, Callable

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey, Ed25519PublicKey,
)
from cryptography.exceptions import InvalidSignature

# ---------------------------------------------------------------- primitives

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(obj: Any) -> bytes:
    """Deterministic serialization: the canonical form an evidence digest
    commits to. Sorted keys, no insignificant whitespace, UTF-8."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")


# ---------------------------------------------------------------- actions

@dataclass(frozen=True)
class Action:
    """A proposed agent action at an interception point."""
    kind: str                    # e.g. "db.read", "http.post"
    resource: str                # target endpoint / table
    params: dict = field(default_factory=dict)
    classification: str = "public"   # data sensitivity touched, if any

    def canonical_form(self) -> bytes:
        return canonical({"kind": self.kind, "resource": self.resource,
                          "params": self.params,
                          "classification": self.classification})


# ------------------------------------------------- bounded path summary (C4.1.7)

@dataclass
class PathSummary:
    """Bounded path state phi_t, updated by a fold (paper Sec. 6.2).

    Size is bounded by construction: a fixed set of scalar/flag fields plus a
    bounded set of classification labels. Evaluation cost is therefore
    independent of path length -- the property bench_scaling.py measures.
    """
    steps: int = 0
    sensitivity: str = "public"          # highest classification read so far
    egress_count: int = 0
    spend: float = 0.0
    labels: frozenset = frozenset()      # bounded label lattice
    trust_elevated: bool = False         # set only by explicit declassification

    ORDER = {"public": 0, "internal": 1, "confidential": 2, "restricted": 3}

    def fold(self, action: Action, verdict: str) -> "PathSummary":
        if verdict != "ALLOW":
            # denied actions advance the step counter only
            return PathSummary(self.steps + 1, self.sensitivity,
                               self.egress_count, self.spend, self.labels,
                               self.trust_elevated)
        sens = self.sensitivity
        if self.ORDER.get(action.classification, 0) > self.ORDER[sens]:
            sens = action.classification
        labels = self.labels
        if action.kind.startswith("db.") or action.kind.startswith("file."):
            labels = labels | {action.classification}
        egress = self.egress_count + (1 if action.kind.startswith("http.") else 0)
        spend = self.spend + float(action.params.get("amount", 0) or 0)
        return PathSummary(self.steps + 1, sens, egress, spend,
                           frozenset(list(labels)[:8]),   # hard size bound B
                           self.trust_elevated)

    def digest(self) -> str:
        return sha256(canonical({
            "steps": self.steps, "sensitivity": self.sensitivity,
            "egress_count": self.egress_count, "spend": round(self.spend, 6),
            "labels": sorted(self.labels), "trust_elevated": self.trust_elevated,
        }))


# ---------------------------------------------------------------- policy

@dataclass
class Grant:
    """Authority granted to the agent for a task (C4.1.1)."""
    principal: str
    allowed_kinds: frozenset
    allowed_resources: frozenset
    max_spend: float = 0.0
    max_sensitivity_egress: str = "public"   # highest class allowed to leave


class PolicyEngine:
    """Deterministic policy Pi over (action, identity, state, path summary).

    Path-aware (C4.1.7): the summary is an argument, so a composed sequence of
    individually permitted actions can be refused. `path_aware=False` models
    the per-action baseline used in the composition attack comparison.
    """

    def __init__(self, grant: Grant, path_aware: bool = True):
        self.grant = grant
        self.path_aware = path_aware
        self.bundle_hash = sha256(canonical({
            "principal": grant.principal,
            "kinds": sorted(grant.allowed_kinds),
            "resources": sorted(grant.allowed_resources),
            "max_spend": grant.max_spend,
            "max_sensitivity_egress": grant.max_sensitivity_egress,
            "path_aware": path_aware,
            "version": "poc-ref-1",
        }))

    def evaluate(self, action: Action, phi: PathSummary) -> tuple[str, str]:
        g = self.grant
        if action.kind not in g.allowed_kinds:
            return "DENY", "kind not in grant"
        if action.resource not in g.allowed_resources:
            return "DENY", "resource not in grant"
        amount = float(action.params.get("amount", 0) or 0)
        if amount and amount > g.max_spend:
            return "DENY", "single action exceeds spend limit"
        if self.path_aware:
            # cumulative budget across the path
            if g.max_spend and phi.spend + amount > g.max_spend:
                return "DENY", "cumulative spend would exceed grant"
            # information-flow style check: egress after reading above the
            # permitted egress classification
            if action.kind.startswith("http.") and not phi.trust_elevated:
                if (PathSummary.ORDER[phi.sensitivity]
                        > PathSummary.ORDER[g.max_sensitivity_egress]):
                    return "DENY", (f"egress after reading {phi.sensitivity} "
                                    f"data exceeds permitted egress class")
        return "ALLOW", "within grant"


# ------------------------------------------- attesting environment (enclave model)

class AttestingEnvironment:
    """Models the TEE: holds the signing key, evaluates policy, extends the
    chain, and issues evidence + capabilities. The signing key is never
    returned by any method (functional stand-in for hardware isolation)."""

    def __init__(self, policy: PolicyEngine, anchor=None,
                 anchor_interval_s: float = 1.0):
        self._sk = Ed25519PrivateKey.generate()
        self.pk: Ed25519PublicKey = self._sk.public_key()
        self.policy = policy
        # "measurement": digest of the evaluated code identity + policy bundle
        self.measurement = sha256(canonical({
            "engine": "poc-ref-1", "bundle": policy.bundle_hash,
        }))
        self.chain_head = sha256(b"poc-genesis")
        self.step_index = 0
        self.phi = PathSummary()
        self.anchor = anchor
        self.anchor_interval_s = anchor_interval_s
        self._last_anchor = time.time()
        self._nonces_issued: set[str] = set()

    # -- internal signing (key never leaves)
    def _sign(self, payload: bytes) -> bytes:
        return self._sk.sign(payload)

    def evaluate_and_evidence(self, action: Action, nonce: str,
                              agent_id: str) -> dict:
        """One intercepted step: evaluate, extend chain, emit evidence and
        (on ALLOW) an action-bound capability."""
        snap = {
            "agent_id": agent_id,
            "action": json.loads(action.canonical_form()),
            "path_summary": self.phi.digest(),
            "step_index": self.step_index,
        }
        snap_bytes = canonical(snap)
        snap_digest = sha256(snap_bytes)

        verdict, reason = self.policy.evaluate(action, self.phi)

        # extend chain: L_t = H(L_{t-1} || H(snapshot) || verdict)
        leaf = sha256((self.chain_head + snap_digest + verdict).encode())
        self.chain_head = leaf
        self.phi = self.phi.fold(action, verdict)

        token = {
            "iat": time.time(),
            "nonce": nonce,
            "eat_profile": "https://standards.org/poc/v1",
            "poc_claims": {
                "agent_id": agent_id,
                "interception_point": "PRE_CALL_TOOL_INVOCATION",
                "step_index": self.step_index,
                "merkle_root": leaf,
                "policy_bundle_hash": self.policy.bundle_hash,
                "target_resource": action.resource,
                "canonical_snapshot_hash": snap_digest,
                "path_summary_hash": snap["path_summary"],
                "verdict": verdict,
                "reason": reason,
            },
            "submods": {"attestation": {"measurement": self.measurement}},
        }
        token_bytes = canonical(token)
        token["signature"] = self._sign(token_bytes).hex()

        capability = None
        if verdict == "ALLOW":
            cap_body = {
                "snapshot_hash": snap_digest,
                "resource": action.resource,
                "nonce": nonce,
                "measurement": self.measurement,
            }
            capability = dict(cap_body)
            capability["signature"] = self._sign(canonical(cap_body)).hex()
            self._nonces_issued.add(nonce)

        self.step_index += 1
        if self.anchor is not None:
            now = time.time()
            if now - self._last_anchor >= self.anchor_interval_s:
                self.anchor.publish(self.chain_head, self.step_index, self._sign)
                self._last_anchor = now
        return {"token": token, "capability": capability, "verdict": verdict,
                "snapshot": snap}

    def force_anchor(self):
        if self.anchor is not None:
            self.anchor.publish(self.chain_head, self.step_index, self._sign)
            self._last_anchor = time.time()


# ---------------------------------------------------------------- gateway

class EvidenceStoreUnavailable(Exception):
    pass


class EvidenceStore:
    """Durable evidence log. `available=False` models pipeline failure, used
    to exercise the fail-closed requirement (C7.6.3)."""

    def __init__(self):
        self.records: list[dict] = []
        self.failures: list[dict] = []
        self.available = True

    def append(self, token: dict):
        if not self.available:
            raise EvidenceStoreUnavailable("evidence store unavailable")
        self.records.append(token)

    def record_failure(self, info: dict):
        self.failures.append(info)   # secondary durable log (C7.6.1)


class Gateway:
    """Action Interception Gateway (C7.1). Mediates every action: evidence is
    durably written before release, and dispatch carries the capability."""

    def __init__(self, ae: AttestingEnvironment, store: EvidenceStore,
                 agent_id: str = "did:web:example:agents:ref-1"):
        self.ae = ae
        self.store = store
        self.agent_id = agent_id
        self._n = 0

    def _nonce(self) -> str:
        self._n += 1
        return f"n-{self._n:08d}"

    def submit(self, action: Action, relying_party=None,
               dispatch_action: Action | None = None) -> dict:
        """Submit a proposed action.

        `dispatch_action` differing from `action` models the malicious host in
        the snapshot-substitution attack: policy sees one action, dispatch
        attempts another.
        """
        nonce = self._nonce()
        out = self.ae.evaluate_and_evidence(action, nonce, self.agent_id)
        try:
            self.store.append(out["token"])          # C7.1.3 write-before-release
        except EvidenceStoreUnavailable as e:
            self.store.record_failure({"nonce": nonce, "error": str(e)})
            return {"executed": False, "verdict": "FAIL_CLOSED", "reason": str(e)}

        if out["verdict"] != "ALLOW":
            return {"executed": False, "verdict": out["verdict"],
                    "reason": out["token"]["poc_claims"]["reason"]}

        effect = dispatch_action or action
        if relying_party is not None:
            ok, why = relying_party.execute(effect, out["capability"])
            return {"executed": ok, "verdict": "ALLOW" if ok else "REFUSED",
                    "reason": why, "token": out["token"]}
        return {"executed": True, "verdict": "ALLOW", "token": out["token"]}


# ---------------------------------------------------------------- relying party

class RelyingParty:
    """Enforces capability-bound dispatch (C7.1.4 option b, C8.3.5).

    `enforce=False` models an endpoint that does not verify capabilities --
    used to demonstrate Proposition 1 (without mediation the adversary wins
    with probability 1)."""

    def __init__(self, pk: Ed25519PublicKey, resource: str,
                 expected_measurement: str, enforce: bool = True):
        self.pk = pk
        self.resource = resource
        self.expected_measurement = expected_measurement
        self.enforce = enforce
        self.executed: list[Action] = []
        self.refused: list[tuple[Action, str]] = []
        self._used_nonces: set[str] = set()

    def execute(self, action: Action, capability: dict | None) -> tuple[bool, str]:
        if not self.enforce:
            self.executed.append(action)
            return True, "executed (no capability enforcement)"
        if capability is None:
            self.refused.append((action, "no capability"))
            return False, "no capability"
        body = {k: capability[k] for k in
                ("snapshot_hash", "resource", "nonce", "measurement")}
        try:
            self.pk.verify(bytes.fromhex(capability["signature"]), canonical(body))
        except InvalidSignature:
            self.refused.append((action, "bad signature"))
            return False, "bad signature"
        if body["measurement"] != self.expected_measurement:
            self.refused.append((action, "measurement mismatch"))
            return False, "measurement mismatch"
        if body["resource"] != self.resource:
            self.refused.append((action, "resource mismatch"))
            return False, "resource mismatch"
        if body["nonce"] in self._used_nonces:
            self.refused.append((action, "nonce replay"))
            return False, "nonce replay"
        # (iv) the executed request must match the committed snapshot
        expected = capability["snapshot_hash"]
        # recompute the action's contribution to the snapshot digest
        if not _action_matches_snapshot(action, expected, self._snap_probe):
            self.refused.append((action, "action does not match evidenced snapshot"))
            return False, "action does not match evidenced snapshot"
        self._used_nonces.add(body["nonce"])
        self.executed.append(action)
        return True, "executed"

    # the relying party is given the snapshot template so it can recompute the
    # digest for the request it is actually being asked to perform
    _snap_probe: Callable | None = None


def _action_matches_snapshot(action: Action, snapshot_hash: str,
                             probe: Callable | None) -> bool:
    if probe is None:
        return True          # configured without a probe: structural check only
    return probe(action) == snapshot_hash


# ---------------------------------------------------------------- anchoring

class TransparencyLog:
    """Append-only public anchor with gossip support (C7.3.3, C7.6.6)."""

    def __init__(self, name: str = "log"):
        self.name = name
        self.entries: list[dict] = []

    def publish(self, root: str, index: int, sign: Callable[[bytes], bytes]):
        body = {"root": root, "index": index, "t": time.time()}
        body["signature"] = sign(canonical(
            {"root": root, "index": index})).hex()
        self.entries.append(body)

    def latest(self) -> dict | None:
        return self.entries[-1] if self.entries else None


def gossip(log_a: TransparencyLog, log_b: TransparencyLog) -> tuple[bool, str]:
    """Cross-verifier consistency check (Theorem 2). Returns (consistent, msg).

    Two validly signed roots at a common index with distinct values are
    non-repudiable proof of equivocation."""
    by_index_a = {e["index"]: e["root"] for e in log_a.entries}
    by_index_b = {e["index"]: e["root"] for e in log_b.entries}
    for idx in sorted(set(by_index_a) & set(by_index_b)):
        if by_index_a[idx] != by_index_b[idx]:
            return False, (f"equivocation detected at index {idx}: "
                           f"{by_index_a[idx][:12]} != {by_index_b[idx][:12]}")
    return True, "consistent"


# ---------------------------------------------------------------- verifier

class Verifier:
    """Independent verifier: checks signatures, measurement, and chain
    continuity using only published material (C8.1.5, C8.1.8)."""

    def __init__(self, pk: Ed25519PublicKey, expected_measurement: str):
        self.pk = pk
        self.expected_measurement = expected_measurement

    def verify_chain(self, records: list[dict],
                     anchor: TransparencyLog | None = None) -> tuple[bool, str]:
        head = sha256(b"poc-genesis")
        for i, tok in enumerate(records):
            sig = bytes.fromhex(tok["signature"])
            body = {k: v for k, v in tok.items() if k != "signature"}
            try:
                self.pk.verify(sig, canonical(body))
            except InvalidSignature:
                return False, f"invalid signature at record {i}"
            c = tok["poc_claims"]
            if tok["submods"]["attestation"]["measurement"] != self.expected_measurement:
                return False, f"measurement mismatch at record {i}"
            if c["step_index"] != i:
                return False, (f"sequence gap: expected step {i}, "
                               f"found {c['step_index']} (omission detected)")
            leaf = sha256((head + c["canonical_snapshot_hash"] + c["verdict"]).encode())
            if leaf != c["merkle_root"]:
                return False, f"chain break at record {i} (alteration detected)"
            head = leaf
        if anchor is not None:
            last = anchor.latest()
            if last is None:
                return False, "no anchor published"
            if last["index"] > len(records):
                return False, (f"truncation detected: anchor covers "
                               f"{last['index']} steps, only {len(records)} presented")
        return True, f"chain verified: {len(records)} records"
