#!/usr/bin/env python3
"""Post-quantum signing for Proof-of-Control evidence.

WHY THIS MATTERS HERE. Evidence is not a session key. A record produced today
may be examined in a dispute, an audit, or a court a decade from now, and it
is only worth what its signature is worth *at the moment it is examined*. A
signature scheme that becomes forgeable in 2035 does not merely expire -- it
retroactively destroys the value of evidence about actions taken in 2026. For
an evidence standard this is a first-order concern, not a checkbox.

WHAT IS AND IS NOT AFFECTED. The hash chain is already post-quantum: Grover
gives at best a square-root speedup on preimage search, so SHA-256 retains
~128-bit security and the chain, sequence numbering, and Merkle anchoring
survive unchanged. Only the *signatures* need migrating -- on evidence tokens,
on capabilities, and on published roots.

MEASUREMENT HONESTY. Ed25519 here is the C/Rust-backed implementation in
`cryptography`; ML-DSA is `dilithium-py`, a pure-Python reference
implementation. The TIME comparison is therefore NOT apples-to-apples and
overstates ML-DSA's cost by a large factor -- optimized ML-DSA is competitive
with, and for verification often faster than, Ed25519. The SIZE comparison IS
implementation-independent, and size is the cost that actually binds here.
"""
from __future__ import annotations

import json
import platform
import statistics as st
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from dilithium_py.ml_dsa import ML_DSA_44, ML_DSA_65

from poc import canonical

N = 200          # pure-Python ML-DSA is slow; enough for a stable median
N_FAST = 2000


def bench(sign, verify, n):
    msg = canonical({"poc": "evidence-token", "step": 12345, "verdict": "ALLOW"})
    sig = sign(msg)
    st_sign, st_ver = [], []
    for _ in range(n):
        t0 = time.perf_counter_ns(); sign(msg)
        t1 = time.perf_counter_ns(); verify(msg, sig)
        t2 = time.perf_counter_ns()
        st_sign.append((t1 - t0) / 1000)
        st_ver.append((t2 - t1) / 1000)
    return st.median(st_sign), st.median(st_ver), len(sig)


def main():
    print("Post-quantum signing for evidence — comparison\n")
    rows = []

    # Ed25519 (classical baseline, C-backed)
    sk = Ed25519PrivateKey.generate(); pk = sk.public_key()
    def ed_sign(m): return sk.sign(m)
    def ed_ver(m, s): pk.verify(s, m); return True
    s_us, v_us, siglen = bench(ed_sign, ed_ver, N_FAST)
    rows.append({"scheme": "Ed25519 (classical)", "impl": "C/Rust",
                 "sign_us": round(s_us, 1), "verify_us": round(v_us, 1),
                 "sig_bytes": siglen, "pk_bytes": 32, "pq": False})

    # ML-DSA-44 and -65 (FIPS 204), pure Python
    for name, alg, pkl in (("ML-DSA-44 (FIPS 204)", ML_DSA_44, 1312),
                           ("ML-DSA-65 (FIPS 204)", ML_DSA_65, 1952)):
        mpk, msk = alg.keygen()
        def m_sign(m, _sk=msk, _a=alg): return _a.sign(_sk, m)
        def m_ver(m, s, _pk=mpk, _a=alg): return _a.verify(_pk, m, s)
        s_us, v_us, siglen = bench(m_sign, m_ver, N)
        rows.append({"scheme": name, "impl": "pure Python (reference)",
                     "sign_us": round(s_us, 1), "verify_us": round(v_us, 1),
                     "sig_bytes": siglen, "pk_bytes": pkl, "pq": True})

    # Hybrid: sign with both, verify both (transition guidance)
    mpk, msk = ML_DSA_44.keygen()
    def h_sign(m): return sk.sign(m) + ML_DSA_44.sign(msk, m)
    def h_ver(m, s):
        pk.verify(s[:64], m)
        return ML_DSA_44.verify(mpk, m, s[64:])
    s_us, v_us, siglen = bench(h_sign, h_ver, N)
    rows.append({"scheme": "Hybrid Ed25519 + ML-DSA-44", "impl": "mixed",
                 "sign_us": round(s_us, 1), "verify_us": round(v_us, 1),
                 "sig_bytes": siglen, "pk_bytes": 32 + 1312, "pq": True})

    print(f"{'scheme':<30}{'sign':>10}{'verify':>10}{'sig':>9}{'pubkey':>9}")
    for r in rows:
        print(f"{r['scheme']:<30}{r['sign_us']:>9.1f}u{r['verify_us']:>9.1f}u"
              f"{r['sig_bytes']:>9}{r['pk_bytes']:>9}")

    # ---- storage: what this costs an evidence chain
    base = len(canonical({
        "iat": 1773532800, "nonce": "0x8f93e2a110c49b",
        "eat_profile": "https://standards.org/poc/v1",
        "poc_claims": {"agent_id": "did:web:enterprise.com:agents:finance-04",
                       "interception_point": "PRE_CALL_TOOL_INVOCATION",
                       "step_index": 3, "merkle_root": "0x" + "a" * 64,
                       "policy_bundle_hash": "sha256:" + "b" * 64,
                       "target_resource": "api.bank.com/v1/payments",
                       "canonical_snapshot_hash": "sha256:" + "c" * 64,
                       "verdict": "ALLOW"},
        "submods": {"attestation": {"measurement": "d" * 64}}}))
    print(f"\nevidence record without signature: {base} bytes")
    storage = []
    for r in rows:
        # hex-encoded signature in the JSON token, plus capability signature
        rec = base + 2 * r["sig_bytes"] * 2
        per_million_gb = rec * 1_000_000 / 1e9
        storage.append({"scheme": r["scheme"], "record_bytes": rec,
                        "gb_per_million_actions": round(per_million_gb, 3)})
        print(f"  {r['scheme']:<30} record {rec:>7} B   "
              f"{per_million_gb:>7.3f} GB / million actions")

    out = {
        "environment": {"platform": platform.platform(),
                        "python": platform.python_version()},
        "caveat": ("Ed25519 is C/Rust-backed; ML-DSA is a pure-Python reference "
                   "implementation. Time comparisons overstate ML-DSA cost by a "
                   "large factor and should not be cited as representative. "
                   "Size comparisons are implementation-independent."),
        "schemes": rows,
        "storage": storage,
        "note_hash_chain": ("The hash chain, sequence numbering, and Merkle "
                            "anchoring are already post-quantum: Grover gives "
                            "at best a square-root speedup, leaving SHA-256 at "
                            "~128-bit security. Only signatures migrate."),
    }
    p = Path(__file__).resolve().parent.parent / "results" / "bench_pq.json"
    p.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nwritten to {p}")


if __name__ == "__main__":
    main()
