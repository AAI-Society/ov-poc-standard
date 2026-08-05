# Crosswalk: NIST AI RMF

| | |
| --- | --- |
| **Framework type** | AI risk-management / governance framework (NIST) |
| **Corpus version** | AI RMF 1.0 (NIST AI 100-1, January 2023) — [access](https://www.nist.gov/itl/ai-risk-management-framework) · [corpus provenance](corpus/README.md) |
| **Relationship** | Complementary — PoC produces the runtime evidence that makes RMF-aligned controls checkable |
| **Coding status** | ⚠️ Draft seed coding, single coder — [rubric](rubric.md) |

## The Relationship

NIST AI RMF governs how organizations identify, measure, and manage AI risk through its four functions (GOVERN, MAP, MEASURE, MANAGE). Governance frameworks tell an organization *what to manage*; they do not, by themselves, produce independent evidence of what an agent did that holds when the operator is the threat. Proof-of-Control is the evidence layer that sits alongside the RMF and feeds it: the independently verifiable, tamper-evident record that lets an RMF-aligned control be *checked* by a party that need not trust the operator.

This is visible in the mapping below: the RMF has the **highest coverage of any coded framework, yet zero exact matches** — it asks for nearly every control PoC verifies, and never for operator-independent evidence of them. That pattern is the binary threshold, seen from the outside.

**NIST AI 100-2** (Adversarial Machine Learning taxonomy) is, separately, one of the three threat catalogs the PoC threat model draws from ([Appendix C](../0.1/en/0x92-Appendix-C_Threat-Model.md)), alongside [MITRE ATLAS](mitre-atlas.md) and the [OWASP Top 10s](owasp.md).

## Requirement-Level Mapping

<!-- BEGIN GENERATED MAPPING (tools/generate_crosswalks.py) -->

**Coverage: 63%** of the 107 Proof-of-Control requirements (0 exact matches, 67 partial, 40 no match), computed per the [mapping rubric](rubric.md) from the row-level [coding sheet](coding_sheet.csv). *Draft seed coding — pending working-group validation.* To change this table, edit the coding sheet and run `python3 tools/generate_crosswalks.py`.

| PoC section | Reqs | Match | Closest framework clause(s) | Rationale |
| --- | :---: | :---: | --- | --- |
| [C1.1 Model and Artifact Provenance](../0.1/en/0x10-C01-Provenance.md) | 5 | 🟡 PM | MAP 2.3; GOVERN 1.6 | MAP function calls for provenance and documentation of models; no cryptographic binding |
| [C1.2 Input and Data Lineage](../0.1/en/0x10-C01-Provenance.md) | 4 | 🟡 PM | MAP 2.3; MEASURE 2.8 | MAP/MEASURE cover data documentation and lineage practices; no hash-linked custody chain |
| [C1.3 Compute Substrate Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | ⚪ NM | — | Compute-substrate attestation not addressed |
| [C1.4 Privacy-Preserving Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | ⚪ NM | — | Privacy-preserving provenance not addressed |
| [C2.1 Data-Access Evidence](../0.1/en/0x10-C02-Privacy.md) | 3 | 🟡 PM | MEASURE 2.10 | MEASURE privacy risk and GOVERN accountability cover access recording; no used-vs-disclosed evidence model |
| [C2.2 Policy and Consent Enforcement](../0.1/en/0x10-C02-Privacy.md) | 5 | 🟡 PM | GOVERN 1.1; MANAGE 1.3 | GOVERN/MANAGE address privacy values and controls; runtime enforcement evidence not required |
| [C2.3 Privacy-Preserving Verification Mechanisms](../0.1/en/0x10-C02-Privacy.md) | 3 | 🟡 PM | MEASURE 2.10 | RMF profiles reference privacy-enhancing technologies; no verifiable-evidence requirement |
| [C2.4 Evidence Handling for Protected Data](../0.1/en/0x10-C02-Privacy.md) | 2 | ⚪ NM | — | Evidence-store handling of protected data not addressed |
| [C3.1 Boundary-Crossing Evidence](../0.1/en/0x10-C03-Portability.md) | 2 | ⚪ NM | — | Boundary-crossing evidence not addressed |
| [C3.2 Cross-Environment Continuity](../0.1/en/0x10-C03-Portability.md) | 3 | ⚪ NM | — | Evidence continuity across environments not addressed |
| [C4.1 Authority and Scope Enforcement](../0.1/en/0x10-C04-Authorization.md) | 6 | 🟡 PM | GOVERN 2.1; GOVERN 3.2 | GOVERN roles/authority and MANAGE controls cover authority definition; no evidenced per-action evaluation |
| [C4.2 Delegation](../0.1/en/0x10-C04-Authorization.md) | 4 | ⚪ NM | — | Delegation chains not addressed |
| [C5.1 Agent and Principal Binding](../0.1/en/0x10-C05-Identity.md) | 4 | 🟡 PM | GOVERN 2.1; GOVERN 4.1 | GOVERN accountability requires attributable actors; no cryptographic principal binding |
| [C5.2 Inter-Agent Identity](../0.1/en/0x10-C05-Identity.md) | 2 | ⚪ NM | — | Inter-agent identity not addressed |
| [C6.1 Execution Environment Integrity](../0.1/en/0x10-C06-Security.md) | 4 | 🟡 PM | MEASURE 2.7 | MEASURE secure-and-resilient characteristic covers environment integrity aims; attestation not required |
| [C6.2 Isolation and Confidential Execution](../0.1/en/0x10-C06-Security.md) | 3 | 🟡 PM | MEASURE 2.7 | Secure-and-resilient characteristic covers isolation expectations generally |
| [C6.3 Cryptographic Key Lifecycle](../0.1/en/0x10-C06-Security.md) | 3 | ⚪ NM | — | Key lifecycle not addressed (delegated to security control catalogs) |
| [C7.1 Generation at the Action Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 3 | ⚪ NM | — | No action-interception evidence concept |
| [C7.2 The Contemporaneous Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 🟡 PM | MEASURE 2.8; MANAGE 4.1 | MEASURE documentation and test records are contemporaneous practices; no mechanism-generated evidence |
| [C7.3 The Tamper-Evident Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 🟡 PM | MEASURE 2.8 | Traceability and documentation expectations; records remain operator-produced |
| [C7.4 The Transparent Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 1 | 🟡 PM | GOVERN 4.2; MAP 4.1 | Transparency and documentation of limitations align with disclosure; no standardized trust-assumption format |
| [C7.5 The Determinism Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 🟡 PM | MEASURE 2.5 | RMF's validity/reliability framing distinguishes measured facts from aspirations; no claims-discipline requirement |
| [C7.6 Evidence Custody and Resilience](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 5 | 🟡 PM | MANAGE 2.3; MANAGE 4.1 | MANAGE incident response and monitoring cover failure handling; fail-closed evidence gating not addressed |
| [C8.1 Tier Placement](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 8 | ⚪ NM | — | No evidence-verifiability grading |
| [C8.2 Mechanism-to-Requirement Fit](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 2 | ⚪ NM | — | No mechanism-fit rule |
| [C8.3 Chain Integrity and Self-Enforcement (Tier 4)](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 4 | ⚪ NM | — | No self-enforcing execution concept |
| [C9.1 Locating Evidence on the System Surface](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | 🟡 PM | MAP 1.1 | MAP requires system context/scope mapping; not per-claim stack location |
| [C9.2 Layer Coverage](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | ⚪ NM | — | Per-layer evidence coverage not addressed |
| [C10.1 Conformance Claims](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 7 | 🟡 PM | GOVERN 4.2 | GOVERN transparency artifacts and RMF profiles resemble scoped claims; no standardized statement |
| [C10.2 Trust-Assumption Disclosure](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 2 | 🟡 PM | MANAGE 1.4 | MANAGE requires documenting residual risk; not categorized trust assumptions |
| [C10.3 Continuously Monitored Operation](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 6 | 🟡 PM | MANAGE 4.1 | MANAGE continuous monitoring aligns in intent; per-action near-real-time validation not specified |

### Gap Analysis (what this framework does not cover)

* **C1.3 Compute Substrate Provenance** — Compute-substrate attestation not addressed
* **C1.4 Privacy-Preserving Provenance** — Privacy-preserving provenance not addressed
* **C2.4 Evidence Handling for Protected Data** — Evidence-store handling of protected data not addressed
* **C3.1 Boundary-Crossing Evidence** — Boundary-crossing evidence not addressed
* **C3.2 Cross-Environment Continuity** — Evidence continuity across environments not addressed
* **C4.2 Delegation** — Delegation chains not addressed
* **C5.2 Inter-Agent Identity** — Inter-agent identity not addressed
* **C6.3 Cryptographic Key Lifecycle** — Key lifecycle not addressed (delegated to security control catalogs)
* **C7.1 Generation at the Action Boundary** — No action-interception evidence concept
* **C8.1 Tier Placement** — No evidence-verifiability grading
* **C8.2 Mechanism-to-Requirement Fit** — No mechanism-fit rule
* **C8.3 Chain Integrity and Self-Enforcement (Tier 4)** — No self-enforcing execution concept
* **C9.2 Layer Coverage** — Per-layer evidence coverage not addressed

*Match granularity is the PoC section; every requirement in a section carries its section's coding in the [coding sheet](coding_sheet.csv). Requirement-level refinement is the working group's next pass.*

<!-- END GENERATED MAPPING -->

## Peer Assurance Ladder

| Proof-of-Control Stage | NIST peer |
| --- | --- |
| Continuously Monitored | NIST Continuous Monitoring |

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
