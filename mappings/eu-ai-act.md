# Crosswalk: EU AI Act

| | |
| --- | --- |
| **Framework type** | Regulation (European Union) |
| **Corpus version** | Regulation (EU) 2024/1689, OJ 12 July 2024 — [access](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) · [corpus provenance](corpus/README.md) |
| **Relationship** | Complementary — PoC evidence lets the Act be enforced against evidence rather than filings |
| **Coding status** | ⚠️ Draft seed coding, single coder — [rubric](rubric.md) |

## The Relationship

Rules for AI agents are only as strong as what they can verify. A regulation that asks an operator to attest that its agent behaved rests on assertion; one that can require independently verifiable evidence of what the agent did rests on proof. The Act's high-risk regime already demands the *practices* PoC evidences — automatic event recording (Art. 12), technical documentation (Art. 11), human oversight (Art. 14), conformity assessment (Art. 43) — but its records remain operator-produced. Proof-of-Control is the evidence layer that would let a market-surveillance authority check an Art. 12 log without trusting the party that wrote it.

Concretely: regulators today cannot verify that a high-risk system operated within authorized parameters ([the Verifiability Gap](../docs/why-verification-matters.md)); PoC evidence at Tiers 3–4 is checkable by a regulator without privileged access. The PoC conformance stages give a graded assessment ladder a conformity-assessment regime can reference, and in the by-domain mapping the Act is the external alignment target for the **Privacy** domain.

## Requirement-Level Mapping

<!-- BEGIN GENERATED MAPPING (tools/generate_crosswalks.py) -->

**Coverage: 55%** of the 107 Proof-of-Control requirements (7 exact matches, 52 partial, 48 no match), computed per the [mapping rubric](rubric.md) from the row-level [coding sheet](coding_sheet.csv). *Draft seed coding — pending working-group validation.* To change this table, edit the coding sheet and run `python3 tools/generate_crosswalks.py`.

| PoC section | Reqs | Match | Closest framework clause(s) | Rationale |
| --- | :---: | :---: | --- | --- |
| [C1.1 Model and Artifact Provenance](../0.1/en/0x10-C01-Provenance.md) | 5 | 🟡 PM | Art. 11; Annex IV | Art 11/Annex IV technical documentation identifies the model and versions; no cryptographic digest binding or signed manifests |
| [C1.2 Input and Data Lineage](../0.1/en/0x10-C01-Provenance.md) | 4 | 🟡 PM | Art. 10 | Art 10 data governance covers data provenance practices; no hash-linked custody chain to the action record |
| [C1.3 Compute Substrate Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | ⚪ NM | — | No provision on compute-substrate identification or attestation |
| [C1.4 Privacy-Preserving Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | ⚪ NM | — | No provision on privacy-preserving provenance evidence |
| [C2.1 Data-Access Evidence](../0.1/en/0x10-C02-Privacy.md) | 3 | 🟡 PM | Art. 12 | Art 12 automatic event recording covers data-access logging; used-vs-disclosed distinction and non-exposure of content not required |
| [C2.2 Policy and Consent Enforcement](../0.1/en/0x10-C02-Privacy.md) | 5 | 🟡 PM | Art. 10 | Art 10 data governance plus GDPR interplay covers purpose/consent obligations; runtime enforcement evidence not required |
| [C2.3 Privacy-Preserving Verification Mechanisms](../0.1/en/0x10-C02-Privacy.md) | 3 | ⚪ NM | — | No provision on ZK proofs, selective disclosure, or commitments |
| [C2.4 Evidence Handling for Protected Data](../0.1/en/0x10-C02-Privacy.md) | 2 | ⚪ NM | — | No provision reconciling erasure obligations with tamper-evident records |
| [C3.1 Boundary-Crossing Evidence](../0.1/en/0x10-C03-Portability.md) | 2 | ⚪ NM | — | No boundary-crossing evidence provision |
| [C3.2 Cross-Environment Continuity](../0.1/en/0x10-C03-Portability.md) | 3 | ⚪ NM | — | No cross-environment evidence-continuity provision |
| [C4.1 Authority and Scope Enforcement](../0.1/en/0x10-C04-Authorization.md) | 6 | 🟡 PM | Art. 9; Art. 14 | Art 14 human oversight and Art 9 risk controls require authority limits and oversight; gateway-blocked rejection evidence not required |
| [C4.2 Delegation](../0.1/en/0x10-C04-Authorization.md) | 4 | ⚪ NM | — | No delegation-chain provisions |
| [C5.1 Agent and Principal Binding](../0.1/en/0x10-C05-Identity.md) | 4 | 🟡 PM | Art. 12; Art. 50 | Art 12 traceability and Art 50 disclosure touch actor identification; no cryptographic principal-to-agent binding |
| [C5.2 Inter-Agent Identity](../0.1/en/0x10-C05-Identity.md) | 2 | ⚪ NM | — | No inter-agent identity provisions |
| [C6.1 Execution Environment Integrity](../0.1/en/0x10-C06-Security.md) | 4 | 🟡 PM | Art. 15 | Art 15 accuracy/robustness/cybersecurity requires environment controls; attestation vs golden values not required |
| [C6.2 Isolation and Confidential Execution](../0.1/en/0x10-C06-Security.md) | 3 | 🟡 PM | Art. 15 | Art 15 cybersecurity covers isolation expectations generally; no proof-of-isolation requirement |
| [C6.3 Cryptographic Key Lifecycle](../0.1/en/0x10-C06-Security.md) | 3 | ⚪ NM | — | No key-lifecycle provisions |
| [C7.1 Generation at the Action Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 3 | ⚪ NM | — | No action-interception or evidence-at-boundary concept |
| [C7.2 The Contemporaneous Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 🟡 PM | Art. 12 | Art 12 requires automatic recording of events over the lifetime; no operator-independent time anchoring |
| [C7.3 The Tamper-Evident Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 🟡 PM | Art. 12; Art. 19 | Art 12/19 logging and retention imply record integrity; evidence remains operator-produced (Tier 2 in PoC terms) |
| [C7.4 The Transparent Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 1 | 🟡 PM | Art. 13 | Art 13 transparency to deployers discloses capabilities and limitations; no trust-assumption disclosure |
| [C7.5 The Determinism Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | ⚪ NM | — | No determinism-boundary or claims-discipline provision |
| [C7.6 Evidence Custody and Resilience](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 5 | 🟡 PM | Art. 19 | Art 19 log retention covers retention duty; fail-closed and omission-detectability not addressed |
| [C8.1 Tier Placement](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 8 | ⚪ NM | — | No evidence-verifiability grading concept |
| [C8.2 Mechanism-to-Requirement Fit](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 2 | ⚪ NM | — | No mechanism-to-requirement fit rule |
| [C8.3 Chain Integrity and Self-Enforcement (Tier 4)](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 4 | ⚪ NM | — | No self-enforcing execution concept |
| [C9.1 Locating Evidence on the System Surface](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | ⚪ NM | — | No system-surface location requirement |
| [C9.2 Layer Coverage](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | ⚪ NM | — | No per-layer evidence coverage requirement |
| [C10.1 Conformance Claims](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 7 | 🟣 EM | Art. 43; Art. 47–48 | Art 43 conformity assessment and Art 47 EU declaration of conformity require a published, scoped, versioned conformance claim |
| [C10.2 Trust-Assumption Disclosure](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 2 | 🟡 PM | Art. 13 | Art 13 requires disclosing limitations and residual risks to deployers; not categorized trust assumptions |
| [C10.3 Continuously Monitored Operation](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 6 | 🟡 PM | Art. 72 | Art 72 post-market monitoring requires ongoing surveillance; not per-action evidence validation |

### Gap Analysis (what this framework does not cover)

* **C1.3 Compute Substrate Provenance** — No provision on compute-substrate identification or attestation
* **C1.4 Privacy-Preserving Provenance** — No provision on privacy-preserving provenance evidence
* **C2.3 Privacy-Preserving Verification Mechanisms** — No provision on ZK proofs, selective disclosure, or commitments
* **C2.4 Evidence Handling for Protected Data** — No provision reconciling erasure obligations with tamper-evident records
* **C3.1 Boundary-Crossing Evidence** — No boundary-crossing evidence provision
* **C3.2 Cross-Environment Continuity** — No cross-environment evidence-continuity provision
* **C4.2 Delegation** — No delegation-chain provisions
* **C5.2 Inter-Agent Identity** — No inter-agent identity provisions
* **C6.3 Cryptographic Key Lifecycle** — No key-lifecycle provisions
* **C7.1 Generation at the Action Boundary** — No action-interception or evidence-at-boundary concept
* **C7.5 The Determinism Boundary** — No determinism-boundary or claims-discipline provision
* **C8.1 Tier Placement** — No evidence-verifiability grading concept
* **C8.2 Mechanism-to-Requirement Fit** — No mechanism-to-requirement fit rule
* **C8.3 Chain Integrity and Self-Enforcement (Tier 4)** — No self-enforcing execution concept
* **C9.1 Locating Evidence on the System Surface** — No system-surface location requirement
* **C9.2 Layer Coverage** — No per-layer evidence coverage requirement

*Match granularity is the PoC section; every requirement in a section carries its section's coding in the [coding sheet](coding_sheet.csv). Requirement-level refinement is the working group's next pass.*

<!-- END GENERATED MAPPING -->

## Peer Assurance Ladder

| Proof-of-Control Stage | EU peer |
| --- | --- |
| Continuously Monitored | EU Cybersecurity Act (comparable assurance bar) |

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
