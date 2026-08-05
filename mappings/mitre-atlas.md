# Crosswalk: MITRE ATLAS

| | |
| --- | --- |
| **Framework type** | Adversarial threat catalog for AI systems (techniques and mitigations) |
| **Corpus version** | Living catalog, as accessed August 2026 — [access](https://atlas.mitre.org/) · [corpus provenance](corpus/README.md) |
| **Relationship** | Threat source — one of the three catalogs the PoC threat model draws from |
| **Coding status** | ⚠️ Draft seed coding, single coder — [rubric](rubric.md) |

## The Relationship

ATLAS catalogs how AI systems are attacked and which mitigations counter each technique. Its primary role for Proof-of-Control is as a **threat source**: the 27 catalogued threats in the PoC threat landscape are drawn from MITRE ATLAS, NIST AI 100-2, and the [OWASP Top 10s](owasp.md), which converge on the same core classes. [Appendix C](../0.1/en/0x92-Appendix-C_Threat-Model.md) states, for each threat, what PoC defends against and what is explicitly out of scope.

The coverage below is accordingly the lowest of any coded framework — and that is the expected result, not a deficiency: ATLAS answers "how are AI systems attacked and mitigated?", while PoC answers "can anyone verify what the system did?". Where they touch (supply-chain verification, access control, sandboxing, event logging), ATLAS mitigations are *controls* whose operation PoC turns into independently verifiable *evidence*.

## Requirement-Level Mapping

<!-- BEGIN GENERATED MAPPING (tools/generate_crosswalks.py) -->

**Coverage: 26%** of the 107 Proof-of-Control requirements (0 exact matches, 28 partial, 79 no match), computed per the [mapping rubric](rubric.md) from the row-level [coding sheet](coding_sheet.csv). *Draft seed coding — pending working-group validation.* To change this table, edit the coding sheet and run `python3 tools/generate_crosswalks.py`.

| PoC section | Reqs | Match | Closest framework clause(s) | Rationale |
| --- | :---: | :---: | --- | --- |
| [C1.1 Model and Artifact Provenance](../0.1/en/0x10-C01-Provenance.md) | 5 | 🟡 PM | Verify ML Artifacts (AML.M0014); code-signing mitigations | Mitigations for ML supply chain compromise (verify ML artifacts) cover provenance checking; no signed-manifest requirement |
| [C1.2 Input and Data Lineage](../0.1/en/0x10-C01-Provenance.md) | 4 | 🟡 PM | Sanitize Training Data (AML.M0007) | Data-provenance mitigations against poisoning; no custody chain to actions |
| [C1.3 Compute Substrate Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | ⚪ NM | — | Substrate attestation not addressed |
| [C1.4 Privacy-Preserving Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | ⚪ NM | — | Privacy-preserving provenance not addressed |
| [C2.1 Data-Access Evidence](../0.1/en/0x10-C02-Privacy.md) | 3 | ⚪ NM | — | Privacy evidence outside ATLAS scope |
| [C2.2 Policy and Consent Enforcement](../0.1/en/0x10-C02-Privacy.md) | 5 | ⚪ NM | — | Consent/purpose enforcement outside scope |
| [C2.3 Privacy-Preserving Verification Mechanisms](../0.1/en/0x10-C02-Privacy.md) | 3 | ⚪ NM | — | Outside scope |
| [C2.4 Evidence Handling for Protected Data](../0.1/en/0x10-C02-Privacy.md) | 2 | ⚪ NM | — | Outside scope |
| [C3.1 Boundary-Crossing Evidence](../0.1/en/0x10-C03-Portability.md) | 2 | ⚪ NM | — | Outside scope |
| [C3.2 Cross-Environment Continuity](../0.1/en/0x10-C03-Portability.md) | 3 | ⚪ NM | — | Outside scope |
| [C4.1 Authority and Scope Enforcement](../0.1/en/0x10-C04-Authorization.md) | 6 | 🟡 PM | Control Access to ML Models and Data (AML.M0005) | Least-privilege and access-control mitigations for ML systems; no evidenced gateway decisions |
| [C4.2 Delegation](../0.1/en/0x10-C04-Authorization.md) | 4 | ⚪ NM | — | Delegation chains not addressed |
| [C5.1 Agent and Principal Binding](../0.1/en/0x10-C05-Identity.md) | 4 | 🟡 PM | AML.M0005 | Access-control mitigations imply authenticated actors; no principal binding |
| [C5.2 Inter-Agent Identity](../0.1/en/0x10-C05-Identity.md) | 2 | ⚪ NM | — | Inter-agent identity not addressed |
| [C6.1 Execution Environment Integrity](../0.1/en/0x10-C06-Security.md) | 4 | 🟡 PM | Adversarial Input Detection (AML.M0015); vulnerability scanning | Mitigations for environment hardening and adversarial input detection; attestation not required |
| [C6.2 Isolation and Confidential Execution](../0.1/en/0x10-C06-Security.md) | 3 | 🟡 PM | Execution-restriction / sandboxing mitigations | Sandboxing/restricting execution mitigations align with isolation requirements |
| [C6.3 Cryptographic Key Lifecycle](../0.1/en/0x10-C06-Security.md) | 3 | ⚪ NM | — | Key lifecycle not addressed |
| [C7.1 Generation at the Action Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 3 | ⚪ NM | — | No evidence-generation concept |
| [C7.2 The Contemporaneous Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | ⚪ NM | — | Not addressed |
| [C7.3 The Tamper-Evident Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 🟡 PM | ML event-logging mitigations | Logging-of-ML-events mitigation supports detection; integrity mechanisms unspecified |
| [C7.4 The Transparent Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 1 | ⚪ NM | — | Not addressed |
| [C7.5 The Determinism Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | ⚪ NM | — | Not addressed |
| [C7.6 Evidence Custody and Resilience](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 5 | ⚪ NM | — | Not addressed |
| [C8.1 Tier Placement](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 8 | ⚪ NM | — | No verifiability grading |
| [C8.2 Mechanism-to-Requirement Fit](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 2 | ⚪ NM | — | No mechanism-fit rule |
| [C8.3 Chain Integrity and Self-Enforcement (Tier 4)](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 4 | ⚪ NM | — | No self-enforcement concept |
| [C9.1 Locating Evidence on the System Surface](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | ⚪ NM | — | Not addressed |
| [C9.2 Layer Coverage](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | ⚪ NM | — | Not addressed |
| [C10.1 Conformance Claims](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 7 | ⚪ NM | — | No conformance regime |
| [C10.2 Trust-Assumption Disclosure](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 2 | ⚪ NM | — | Not addressed |
| [C10.3 Continuously Monitored Operation](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 6 | ⚪ NM | — | Not addressed |

### Gap Analysis (what this framework does not cover)

* **C1.3 Compute Substrate Provenance** — Substrate attestation not addressed
* **C1.4 Privacy-Preserving Provenance** — Privacy-preserving provenance not addressed
* **C2.1 Data-Access Evidence** — Privacy evidence outside ATLAS scope
* **C2.2 Policy and Consent Enforcement** — Consent/purpose enforcement outside scope
* **C2.3 Privacy-Preserving Verification Mechanisms** — Outside scope
* **C2.4 Evidence Handling for Protected Data** — Outside scope
* **C3.1 Boundary-Crossing Evidence** — Outside scope
* **C3.2 Cross-Environment Continuity** — Outside scope
* **C4.2 Delegation** — Delegation chains not addressed
* **C5.2 Inter-Agent Identity** — Inter-agent identity not addressed
* **C6.3 Cryptographic Key Lifecycle** — Key lifecycle not addressed
* **C7.1 Generation at the Action Boundary** — No evidence-generation concept
* **C7.2 The Contemporaneous Property** — Not addressed
* **C7.4 The Transparent Property** — Not addressed
* **C7.5 The Determinism Boundary** — Not addressed
* **C7.6 Evidence Custody and Resilience** — Not addressed
* **C8.1 Tier Placement** — No verifiability grading
* **C8.2 Mechanism-to-Requirement Fit** — No mechanism-fit rule
* **C8.3 Chain Integrity and Self-Enforcement (Tier 4)** — No self-enforcement concept
* **C9.1 Locating Evidence on the System Surface** — Not addressed
* **C9.2 Layer Coverage** — Not addressed
* **C10.1 Conformance Claims** — No conformance regime
* **C10.2 Trust-Assumption Disclosure** — Not addressed
* **C10.3 Continuously Monitored Operation** — Not addressed

*Match granularity is the PoC section; every requirement in a section carries its section's coding in the [coding sheet](coding_sheet.csv). Requirement-level refinement is the working group's next pass.*

<!-- END GENERATED MAPPING -->

## Threat-Model Role (the primary crosswalk)

For the threat-by-threat view of what PoC evidence reaches — 🟢 Full · 🔵 Strong · 🟡 Partial ·
⚪ Not addressed across all 29 threats — see [Appendix C: Threat Model](../0.1/en/0x92-Appendix-C_Threat-Model.md).

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
