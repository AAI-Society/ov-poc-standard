# Proof-of-Control — Reference Implementation

A working implementation of the evidence pipeline specified in
[`0.1/en/`](../0.1/en): action interception, path-aware policy evaluation,
hash-chained signed evidence, capability-bound dispatch, anchoring, gossip, and
independent verification — with an attack harness and benchmarks.

```bash
cd impl
python3 tests/test_core.py        # 14 correctness tests
python3 attacks/run_attacks.py    # 8 attack scenarios, with and without the requirement
python3 bench/bench.py            # latency, scaling, verification, utility
python3 bench/bench_pq.py         # post-quantum signature comparison
```

Requires Python 3.11+ and `cryptography` (Ed25519). Results are written to
[`results/`](results).

## What is real and what is modelled

**Real:** the protocol and every check in it. Ed25519 signing and verification,
SHA-256 hash chaining with monotonic sequence indices, canonical serialization,
policy evaluation over a bounded path summary, capability minting and
verification at the relying party, anchoring, gossip-based equivocation
detection, and fail-closed behaviour when the evidence pipeline is unavailable.
The attack harness executes real attacks against real defenses.

**Modelled:** the hardware TEE. No Intel TDX / AMD SEV-SNP machine was available,
so `AttestingEnvironment` is an in-process object whose signing key is never
returned by any method and whose "measurement" is a digest of the policy engine
identity and bundle. This reproduces the *protocol structure* the security
arguments depend on — which is what the theorems are about — but it does **not**
reproduce hardware isolation.

**Consequence for the numbers:** reported latencies exclude enclave transition
costs. A real TEE deployment adds an enclave round trip per evaluated step. The
measurements below are therefore a *lower bound* on end-to-end latency and an
accurate measure of the software components (canonicalization, policy
evaluation, signing, chaining, verification). We state this rather than
extrapolating a TEE overhead we did not measure.

## Results

Measured on Apple M2 Max, Python 3.11.11, single core; 5,000 iterations after
200 warm-up steps.

### Per-step latency

| Component | Mean | p95 | p99 |
| --- | ---: | ---: | ---: |
| Canonicalization + digest | 3.65 µs | 3.83 µs | 7.00 µs |
| Policy evaluation (path-aware) | 0.35 µs | 0.42 µs | 0.71 µs |
| Ed25519 signing | 83.42 µs | 95.88 µs | 110.04 µs |
| Chain append | 0.67 µs | 0.79 µs | 3.38 µs |
| **End-to-end gateway step** | **191.08 µs** | **215.96 µs** | **237.00 µs** |

Throughput: **5,233 steps/s** on one core. The end-to-end figure exceeds the sum
of components because a gateway step signs twice (evidence token and
capability) and serializes the token for the store. Signing dominates: ~87% of
the step. The design target is 15 ms per intercepted step; the software pipeline
uses **1.3% of that budget** (78× headroom), which is the margin available for
enclave transitions in a hardware deployment.

### Scaling with path length — the bounded-summary claim

| Path length | Bounded summary | Naive full-path re-evaluation |
| ---: | ---: | ---: |
| 10 | 0.208 µs | 5.79 µs |
| 100 | 0.208 µs | 64.92 µs |
| 1,000 | 0.208 µs | 663.88 µs |
| 5,000 | 0.209 µs | 3,379.17 µs |

Per-step cost with the bounded summary is **flat** across a 500× increase in
path length, confirming the O(|Π| + B) claim; the naive baseline is linear in
path length and would exhaust the 15 ms budget at roughly 22,000 steps.

### Independent verification

| Records | Total | Per record |
| ---: | ---: | ---: |
| 100 | 18.79 ms | 187.87 µs |
| 1,000 | 190.62 ms | 190.62 µs |
| 5,000 | 949.74 ms | 189.95 µs |

Verification is linear and dominated by Ed25519 verification. A verifier can
check a 5,000-step agent history in under a second, using only published keys
and reference values.

### Utility cost of path-aware authorization

2,000 randomized workflows (70% benign, 30% attempting read-then-egress
escalation):

| Configuration | False-rejection rate (benign) | Malicious blocked |
| --- | ---: | ---: |
| No declassification point | **42.2%** | 74.6% |
| With explicit declassification (redaction step) | **0.0%** | 71.8% |

This is the paper's most consequential measurement and it reproduces the
classical information-flow result: a monitor that accumulates labels along a
path suffers **label creep**, refusing nearly half of benign work. Adding an
explicit declassification point — a redaction step that resets the accumulated
label — eliminates the false rejections at a cost of 2.8 points of detection.
Path-aware authorization is therefore *not* deployable without declassification
design, which is a requirement-level finding, not a tuning detail.

## Post-quantum signing

Evidence is only worth what its signature is worth *when someone examines it*, which for audit
and litigation may be a decade after the fact. A scheme that becomes forgeable in 2035
retroactively destroys evidence about actions taken today, so this is a first-order concern for
an evidence standard rather than a checkbox.

**The chain is already fine.** Grover buys a square root on preimage search, so SHA-256 keeps
~128-bit security: the hash chain, sequence numbering, and anchoring survive unchanged. Only the
signatures migrate.

| Scheme | Signature | Public key | Record | Per million actions |
| --- | ---: | ---: | ---: | ---: |
| Ed25519 (classical) | 64 B | 32 B | 928 B | 0.93 GB |
| ML-DSA-44 (FIPS 204) | 2,420 B | 1,312 B | 10,352 B | 10.35 GB |
| ML-DSA-65 (FIPS 204) | 3,309 B | 1,952 B | 13,908 B | 13.91 GB |
| Hybrid Ed25519 + ML-DSA-44 | 2,484 B | 1,344 B | 10,608 B | 10.61 GB |

The cost is **size, not speed**: signatures grow 38×, and since the chain stores one per action,
records grow about 11×. That is a storage and bandwidth bill, not a cryptography problem. Hybrid
costs 64 bytes more than ML-DSA alone and covers you either way, which makes it the sensible
default during transition.

> **Timing caveat.** Ed25519 here is C-backed; ML-DSA is a pure-Python reference implementation.
> The measured ML-DSA times (tens of ms) are an artifact of that and are **not** representative —
> optimized ML-DSA is competitive with Ed25519, and verification is fast. Do not cite timing
> comparisons from this benchmark. The size figures are implementation-independent and do
> transfer.

Requirements added as a result: **C6.3.4** (algorithm identified in every record; migration path
declared) and **C6.3.5** (post-quantum or hybrid signing, or scheduled re-signing, where
retention outlives the scheme).

## Attack harness

Each scenario runs with and without the relevant requirement.

| # | Attack | Without the requirement | With it |
| --- | --- | --- | --- |
| A1 | Snapshot substitution | Succeeds: evidence attests a benign action while a malicious one executes | Refused: action does not match evidenced snapshot |
| A2 | Log alteration | Succeeds against unsigned operator logs | Detected: invalid signature at record 2 |
| A3 | Omission of a step | Succeeds: dropped step is indistinguishable from one that never happened | Detected: sequence gap at step 3 |
| A4 | Head truncation | Succeeds: truncated prefix is internally consistent | Detected: anchor covers 8 steps, 5 presented |
| A5 | Split-view / equivocation | Succeeds: each verifier's chain is internally consistent | Detected: divergent roots at index 3 |
| A6 | Path-composition escalation | Succeeds: read and egress each within grant | Blocked: egress after confidential read |
| A7 | Capability replay | Succeeds without single-use semantics | Refused: nonce replay |
| A8 | Evidence-pipeline failure | Succeeds: system keeps acting while logging is down | Refused: FAIL_CLOSED, failure recorded |

A1 is the empirical form of Proposition 1 in the paper: without a check binding
the executed request to the evidenced snapshot, the adversary wins with
probability 1 — here, on the first attempt.

## Layout

```
impl/
├── poc/core.py            the pipeline: snapshot, policy, chain, evidence,
│                          gateway, relying party, anchor, gossip, verifier
├── attacks/run_attacks.py 8 attack scenarios, with/without each requirement
├── bench/bench.py         B1 latency · B2 scaling · B3 verification · B4 utility
├── bench/bench_pq.py      post-quantum signature comparison (size and cost)
├── tests/test_core.py     14 correctness tests mapped to requirement IDs
└── results/               attacks.json, bench.json (regenerated by the scripts)
```

## Limitations

1. **No hardware TEE**, as described above; enclave transition cost is unmeasured.
2. **Single-process**, so network and IPC costs between gateway, enclave, and
   relying party are excluded.
3. **Synthetic workloads.** The utility measurement uses a randomized workflow
   model, not traces from a production agent; the qualitative result
   (label creep, fixed by declassification) is robust, the specific 42.2% is
   workload-dependent.
4. **Python**, so absolute latencies are conservative; a Rust/WASM policy engine
   would be faster, and the relative component breakdown is the durable result.
5. **Pure-Python ML-DSA**, so post-quantum *timings* are unrepresentative; the size results are not affected.
6. **No ZK path.** The privacy-preserving evidence options of C2.3 are specified
   but not implemented here.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
