# Crosswalk: ISO/IEC 42001

| | |
| --- | --- |
| **Framework type** | AI management system standard (ISO/IEC) |
| **Corpus version** | ISO/IEC 42001:2023 — [access](https://www.iso.org/standard/81230.html) · [corpus provenance](corpus/README.md) |
| **Relationship** | Complementary — PoC evidences that declared AIMS controls held at execution; PoC borrows its verification/validation vocabulary |
| **Coding status** | ⚠️ Draft seed coding, single coder — [rubric](rubric.md) |

## The Relationship

ISO/IEC 42001 defines the management system (AIMS) through which an organization governs its AI: policies, roles, documented information, impact assessment, and continual improvement. Like other management-system standards, it establishes *that controls exist and are managed*; Proof-of-Control supplies the independent, tamper-evident evidence that those controls *held at execution*, checkable by a party that need not trust the operator. An organization certified to 42001 can use PoC evidence to demonstrate — with mechanism-generated records rather than management assertion — that its declared controls operated as designed.

**Verification, not validation.** PoC adopts the systems-engineering distinction as used by ISO/IEC 42001 and IEEE: *verification* asks whether the system was built and run right (did it execute within authorized boundaries — PoC delivers this); *validation* asks whether it was the right system (whether the boundaries and outputs were the correct choice — a human responsibility). See [C7.5](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md).

## Requirement-Level Mapping

<!-- BEGIN GENERATED MAPPING (tools/generate_crosswalks.py) -->

**Coverage: 60%** of the 107 Proof-of-Control requirements (7 exact matches, 57 partial, 43 no match), computed per the [mapping rubric](rubric.md) from the row-level [coding sheet](coding_sheet.csv). *Draft seed coding — pending working-group validation.* To change this table, edit the coding sheet and run `python3 tools/generate_crosswalks.py`.

| PoC section | Reqs | Match | Closest framework clause(s) | Rationale |
| --- | :---: | :---: | --- | --- |
| [C1.1 Model and Artifact Provenance](../0.1/en/0x10-C01-Provenance.md) | 5 | 🟡 PM | Annex A.4; Cl. 7.5 | Annex A resources/data controls require model documentation and versioning; no digest binding |
| [C1.2 Input and Data Lineage](../0.1/en/0x10-C01-Provenance.md) | 4 | 🟡 PM | Annex A.7 | Data management controls cover provenance and quality records; no hash-linked custody |
| [C1.3 Compute Substrate Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | ⚪ NM | — | Substrate attestation not addressed |
| [C1.4 Privacy-Preserving Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | ⚪ NM | — | Privacy-preserving provenance not addressed |
| [C2.1 Data-Access Evidence](../0.1/en/0x10-C02-Privacy.md) | 3 | 🟡 PM | Annex A.7; Cl. 7.5 | AIMS records and data management cover access documentation; no evidence-content constraints |
| [C2.2 Policy and Consent Enforcement](../0.1/en/0x10-C02-Privacy.md) | 5 | 🟡 PM | Annex A.5; Annex A.7 | Data management and impact-assessment controls cover purpose and consent obligations |
| [C2.3 Privacy-Preserving Verification Mechanisms](../0.1/en/0x10-C02-Privacy.md) | 3 | ⚪ NM | — | Cryptographic privacy mechanisms not addressed |
| [C2.4 Evidence Handling for Protected Data](../0.1/en/0x10-C02-Privacy.md) | 2 | ⚪ NM | — | Erasure-vs-immutability reconciliation not addressed |
| [C3.1 Boundary-Crossing Evidence](../0.1/en/0x10-C03-Portability.md) | 2 | ⚪ NM | — | Boundary-crossing evidence not addressed |
| [C3.2 Cross-Environment Continuity](../0.1/en/0x10-C03-Portability.md) | 3 | ⚪ NM | — | Evidence continuity not addressed |
| [C4.1 Authority and Scope Enforcement](../0.1/en/0x10-C04-Authorization.md) | 6 | 🟡 PM | Annex A.9 | Human oversight and resource-authority controls; no evidenced per-action evaluation |
| [C4.2 Delegation](../0.1/en/0x10-C04-Authorization.md) | 4 | ⚪ NM | — | Delegation chains not addressed |
| [C5.1 Agent and Principal Binding](../0.1/en/0x10-C05-Identity.md) | 4 | 🟡 PM | Cl. 5.3; Annex A.3 | Roles, responsibilities and accountability controls; no cryptographic binding |
| [C5.2 Inter-Agent Identity](../0.1/en/0x10-C05-Identity.md) | 2 | ⚪ NM | — | Inter-agent identity not addressed |
| [C6.1 Execution Environment Integrity](../0.1/en/0x10-C06-Security.md) | 4 | 🟡 PM | Cl. 8 (via ISO/IEC 27001 alignment) | Security controls via ISO 27001 alignment cover environment integrity; attestation not required |
| [C6.2 Isolation and Confidential Execution](../0.1/en/0x10-C06-Security.md) | 3 | ⚪ NM | — | Isolation proof not addressed |
| [C6.3 Cryptographic Key Lifecycle](../0.1/en/0x10-C06-Security.md) | 3 | 🟡 PM | ISO/IEC 27001 cryptographic controls (adjunct) | 27001-aligned cryptographic control expectations (key management) without evidence-key specificity |
| [C7.1 Generation at the Action Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 3 | ⚪ NM | — | No action-interception concept |
| [C7.2 The Contemporaneous Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 🟡 PM | Cl. 7.5.3 | Documented-information controls require contemporaneous records; operator-produced |
| [C7.3 The Tamper-Evident Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 🟡 PM | Cl. 7.5.3 | Records control protects integrity of documented information; not mechanism-generated |
| [C7.4 The Transparent Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 1 | 🟡 PM | Annex A.8 | Transparency and reporting controls; no trust-assumption format |
| [C7.5 The Determinism Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 🟡 PM | Cl. 9.1 | 42001 adopts the verification/validation distinction PoC builds on; no claims-review requirement |
| [C7.6 Evidence Custody and Resilience](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 5 | 🟡 PM | Cl. 7.5.3 | Records retention and control of documented information; fail-closed not addressed |
| [C8.1 Tier Placement](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 8 | ⚪ NM | — | No verifiability grading |
| [C8.2 Mechanism-to-Requirement Fit](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 2 | ⚪ NM | — | No mechanism-fit rule |
| [C8.3 Chain Integrity and Self-Enforcement (Tier 4)](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 4 | ⚪ NM | — | No self-enforcement concept |
| [C9.1 Locating Evidence on the System Surface](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | 🟡 PM | Cl. 4.3 | AIMS scoping requires defining system boundaries; not per-claim layer fields |
| [C9.2 Layer Coverage](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | ⚪ NM | — | Layer-matched evidence not addressed |
| [C10.1 Conformance Claims](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 7 | 🟣 EM | Cl. 4.3; Statement of Applicability | Management-system conformity with a statement of applicability parallels a scoped, versioned conformance statement |
| [C10.2 Trust-Assumption Disclosure](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 2 | 🟡 PM | Cl. 6.1; Statement of Applicability | Statement of applicability and risk treatment disclose residuals; not categorized trust assumptions |
| [C10.3 Continuously Monitored Operation](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 6 | 🟡 PM | Cl. 9.2–9.3; Cl. 10 | Internal audit and continual improvement provide ongoing checking; not per-action validation |

### Gap Analysis (what this framework does not cover)

* **C1.3 Compute Substrate Provenance** — Substrate attestation not addressed
* **C1.4 Privacy-Preserving Provenance** — Privacy-preserving provenance not addressed
* **C2.3 Privacy-Preserving Verification Mechanisms** — Cryptographic privacy mechanisms not addressed
* **C2.4 Evidence Handling for Protected Data** — Erasure-vs-immutability reconciliation not addressed
* **C3.1 Boundary-Crossing Evidence** — Boundary-crossing evidence not addressed
* **C3.2 Cross-Environment Continuity** — Evidence continuity not addressed
* **C4.2 Delegation** — Delegation chains not addressed
* **C5.2 Inter-Agent Identity** — Inter-agent identity not addressed
* **C6.2 Isolation and Confidential Execution** — Isolation proof not addressed
* **C7.1 Generation at the Action Boundary** — No action-interception concept
* **C8.1 Tier Placement** — No verifiability grading
* **C8.2 Mechanism-to-Requirement Fit** — No mechanism-fit rule
* **C8.3 Chain Integrity and Self-Enforcement (Tier 4)** — No self-enforcement concept
* **C9.2 Layer Coverage** — Layer-matched evidence not addressed

*Match granularity is the PoC section; every requirement in a section carries its section's coding in the [coding sheet](coding_sheet.csv). Requirement-level refinement is the working group's next pass.*

<!-- END GENERATED MAPPING -->

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
