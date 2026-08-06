#!/usr/bin/env python3
"""Correctness tests for the reference implementation. Run: python3 tests/test_core.py"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from poc import (Action, AttestingEnvironment, EvidenceStore, Gateway, Grant,
                 PathSummary, PolicyEngine, RelyingParty, TransparencyLog,
                 Verifier, gossip)

PASS = FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1; print(f"  ok   {name}")
    else:
        FAIL += 1; print(f"  FAIL {name}")


def stack(path_aware=True, anchor=None):
    g = Grant("user:alice", frozenset({"db.read", "http.post", "pay.send"}),
              frozenset({"customers", "api.partner.com", "api.bank.com"}),
              max_spend=100.0, max_sensitivity_egress="internal")
    ae = AttestingEnvironment(PolicyEngine(g, path_aware), anchor=anchor,
                              anchor_interval_s=0.0)
    s = EvidenceStore()
    return ae, s, Gateway(ae, s)


def main():
    print("Proof-of-Control reference implementation — tests\n")

    # evidence exists for every action, and precedes release
    ae, store, gw = stack()
    r = gw.submit(Action("db.read", "customers", {"row": 1}))
    check("C7.1.2 evidence emitted for an allowed action", len(store.records) == 1)
    check("C7.1.3 evidence written before release", r["executed"])

    # denied actions are evidenced too
    r = gw.submit(Action("db.delete", "customers", {}))
    check("C4.1.2 denial recorded with reason",
          r["verdict"] == "DENY" and len(store.records) == 2
          and store.records[-1]["poc_claims"]["verdict"] == "DENY")

    # chain verifies end-to-end by an independent verifier
    v = Verifier(ae.pk, ae.measurement)
    ok, msg = v.verify_chain(store.records)
    check(f"C8.1.5 independent verification ({msg})", ok)

    # signing key is not reachable through the API
    check("C7.3.2 signing key not exposed",
          not any(a for a in dir(ae) if a in ("sk", "signing_key", "private_key")))

    # spend budget accumulates across the path
    ae, store, gw = stack()
    a = Action("pay.send", "api.bank.com", {"amount": 60.0})
    r1 = gw.submit(a); r2 = gw.submit(a)
    check("C4.1.7 cumulative spend enforced across path",
          r1["verdict"] == "ALLOW" and r2["verdict"] == "DENY")

    # per-action policy misses the same composition
    ae, store, gw = stack(path_aware=False)
    r1 = gw.submit(a); r2 = gw.submit(a)
    check("baseline per-action policy misses cumulative overspend",
          r1["verdict"] == "ALLOW" and r2["verdict"] == "ALLOW")

    # bounded path summary stays bounded
    ae, store, gw = stack()
    for i in range(500):
        gw.submit(Action("db.read", "customers", {"row": i},
                         classification="confidential"))
    check("C4.1.7 path summary size bounded (labels <= 8)", len(ae.phi.labels) <= 8)
    check("path summary digest is stable-length", len(ae.phi.digest()) == 64)

    # anchoring + truncation detection
    log = TransparencyLog()
    ae, store, gw = stack(anchor=log)
    for i in range(4):
        gw.submit(Action("db.read", "customers", {"row": i}))
    ae.force_anchor()
    v = Verifier(ae.pk, ae.measurement)
    ok_full, _ = v.verify_chain(store.records, anchor=log)
    ok_trunc, _ = v.verify_chain(store.records[:2], anchor=log)
    check("C7.6.6 full chain verifies against anchor", ok_full)
    check("C7.6.6 truncated chain rejected against anchor", not ok_trunc)

    # gossip agrees when there is no fork
    log_b = TransparencyLog()
    for e in log.entries:
        log_b.entries.append(e)
    consistent, _ = gossip(log, log_b)
    check("C7.3.3 gossip reports consistency when histories agree", consistent)

    # capability binds to resource
    ae, store, gw = stack()
    rp_other = RelyingParty(ae.pk, "api.other.com", ae.measurement)
    out = ae.evaluate_and_evidence(
        Action("http.post", "api.partner.com", {"b": "x"}), "n1", gw.agent_id)
    ok, why = rp_other.execute(Action("http.post", "api.partner.com", {"b": "x"}),
                               out["capability"])
    check(f"C7.1.4 capability rejected at wrong resource ({why})", not ok)

    # measurement mismatch is rejected
    rp_bad = RelyingParty(ae.pk, "api.partner.com", "0" * 64)
    ok, why = rp_bad.execute(Action("http.post", "api.partner.com", {"b": "x"}),
                             out["capability"])
    check(f"C8.1.7 measurement mismatch rejected ({why})", not ok)

    print(f"\n{PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
