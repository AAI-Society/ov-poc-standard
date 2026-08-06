# Crosswalk: MITRE ATLAS

| | |
| --- | --- |
| **Framework type** | Adversarial threat catalog for AI systems (techniques and mitigations) |
| **Corpus version** | Living catalog, as accessed August 2026 — [access](https://atlas.mitre.org/) · [corpus provenance](corpus/README.md) |
| **Relationship** | Threat source — one of the three catalogs the PoC threat model draws from |
| **Coding status** | Draft seed coding, single coder — [rubric](rubric.md) |

## The Relationship

ATLAS catalogs how AI systems are attacked and which mitigations counter each technique. Its primary role for Proof-of-Control is as a **threat source**: the 27 catalogued threats in the PoC threat landscape are drawn from MITRE ATLAS, NIST AI 100-2, and the [OWASP Top 10s](owasp.md), which converge on the same core classes. [Appendix C](../0.1/en/0x92-Appendix-C_Threat-Model.md) states, for each threat, what PoC defends against and what is explicitly out of scope.

The coverage below is accordingly the lowest of any coded framework — and that is the expected result, not a deficiency: ATLAS answers "how are AI systems attacked and mitigated?", while PoC answers "can anyone verify what the system did?". Where they touch (supply-chain verification, access control, sandboxing, event logging), ATLAS mitigations are *controls* whose operation PoC turns into independently verifiable *evidence*.

## Requirement-Level Mapping

<!-- BEGIN GENERATED MAPPING (tools/generate_crosswalks.py) -->

**Coverage: 25%** of the 125 Proof-of-Control requirements (0 exact matches, 31 partial matches, 94 not covered), computed per the [mapping rubric](rubric.md) from the row-level [coding sheet](coding_sheet.csv). *Draft seed coding — pending working-group validation.* To change this table, edit the coding sheet and run `python3 tools/generate_crosswalks.py`.

**How to read the Match column** ([full rubric](rubric.md)): **Exact** — the framework has a clause equivalent in scope and intent. **Partial** — the framework covers the topic, but not with PoC's operator-independent evidence (or not at the same depth). **None** — the framework has no analogous provision. Where a section holds a mix, the badge shows the strongest match present and the **Covered** column shows how many of its requirements are matched at all — so a section reading *Partial 3/5* has two requirements this framework does not reach.

| PoC section | Reqs | Covered | Match | Closest framework clause(s) | Rationale |
| --- | :---: | :---: | :---: | --- | --- |
| [C1.1 Model and Artifact Provenance](../0.1/en/0x10-C01-Provenance.md) | 5 | 5/5 | Partial | Verify ML Artifacts (AML.M0014); code-signing mitigations | Mitigations for ML supply chain compromise (verify ML artifacts) cover provenance checking; no signed-manifest requirement |
| [C1.2 Input and Data Lineage](../0.1/en/0x10-C01-Provenance.md) | 4 | 4/4 | Partial | Sanitize Training Data (AML.M0007) | Data-provenance mitigations against poisoning; no custody chain to actions |
| [C1.3 Compute Substrate Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | 0/2 | None | — | Substrate attestation not addressed |
| [C1.4 Privacy-Preserving Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | 0/2 | None | — | Privacy-preserving provenance not addressed |
| [C2.1 Data-Access Evidence](../0.1/en/0x10-C02-Privacy.md) | 3 | 0/3 | None | — | Privacy evidence outside ATLAS scope |
| [C2.2 Policy and Consent Enforcement](../0.1/en/0x10-C02-Privacy.md) | 5 | 0/5 | None | — | Consent/purpose enforcement outside scope |
| [C2.3 Privacy-Preserving Verification Mechanisms](../0.1/en/0x10-C02-Privacy.md) | 3 | 0/3 | None | — | Outside scope |
| [C2.4 Evidence Handling for Protected Data](../0.1/en/0x10-C02-Privacy.md) | 2 | 0/2 | None | — | Outside scope |
| [C3.1 Boundary-Crossing Evidence](../0.1/en/0x10-C03-Portability.md) | 2 | 0/2 | None | — | Outside scope |
| [C3.2 Cross-Environment Continuity](../0.1/en/0x10-C03-Portability.md) | 3 | 0/3 | None | — | Outside scope |
| [C4.1 Authority and Scope Enforcement](../0.1/en/0x10-C04-Authorization.md) | 8 | 8/8 | Partial | Control Access to ML Models and Data (AML.M0005) | Least-privilege and access-control mitigations for ML systems; no evidenced gateway decisions |
| [C4.2 Delegation](../0.1/en/0x10-C04-Authorization.md) | 4 | 0/4 | None | — | Delegation chains not addressed |
| [C5.1 Agent and Principal Binding](../0.1/en/0x10-C05-Identity.md) | 4 | 4/4 | Partial | AML.M0005 | Access-control mitigations imply authenticated actors; no principal binding |
| [C5.2 Inter-Agent Identity](../0.1/en/0x10-C05-Identity.md) | 2 | 0/2 | None | — | Inter-agent identity not addressed |
| [C6.1 Execution Environment Integrity](../0.1/en/0x10-C06-Security.md) | 4 | 4/4 | Partial | Adversarial Input Detection (AML.M0015); vulnerability scanning | Mitigations for environment hardening and adversarial input detection; attestation not required |
| [C6.2 Isolation and Confidential Execution](../0.1/en/0x10-C06-Security.md) | 3 | 3/3 | Partial | Execution-restriction / sandboxing mitigations | Sandboxing/restricting execution mitigations align with isolation requirements |
| [C6.3 Cryptographic Key Lifecycle](../0.1/en/0x10-C06-Security.md) | 5 | 0/5 | None | — | Key lifecycle not addressed |
| [C7.1 Generation at the Action Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 5 | 0/5 | None | — | No evidence-generation concept |
| [C7.2 The Contemporaneous Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 0/2 | None | — | Not addressed |
| [C7.3 The Tamper-Evident Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 5 | 3/5 | Partial | ML event-logging mitigations | Logging-of-ML-events mitigation supports detection; integrity mechanisms unspecified. Not reached: 7.3.4, 7.3.5. |
| [C7.4 The Transparent Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 1 | 0/1 | None | — | Not addressed |
| [C7.5 The Determinism Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | 0/2 | None | — | Not addressed |
| [C7.6 Evidence Custody and Resilience](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 6 | 0/6 | None | — | Not addressed |
| [C7.7 The Interoperable Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 5 | 0/5 | None | — | Out of scope |
| [C8.1 Tier Placement](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 8 | 0/8 | None | — | No verifiability grading |
| [C8.2 Mechanism-to-Requirement Fit](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 2 | 0/2 | None | — | No mechanism-fit rule |
| [C8.3 Chain Integrity and Self-Enforcement (Tier 4)](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 5 | 0/5 | None | — | No self-enforcement concept |
| [C9.1 Locating Evidence on the System Surface](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | 0/3 | None | — | Not addressed |
| [C9.2 Layer Coverage](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | 0/3 | None | — | Not addressed |
| [C10.1 Conformance Claims](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 8 | 0/8 | None | — | No conformance regime |
| [C10.2 Trust-Assumption Disclosure](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 2 | 0/2 | None | — | Not addressed |
| [C10.3 Continuously Monitored Operation](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 7 | 0/7 | None | — | Not addressed |

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
* **C7.3 The Tamper-Evident Property** — partially reached; no provision for 7.3.4, 7.3.5: Adversary-technique catalogue; log structure out of scope
* **C7.4 The Transparent Property** — Not addressed
* **C7.5 The Determinism Boundary** — Not addressed
* **C7.6 Evidence Custody and Resilience** — Not addressed
* **C7.7 The Interoperable Property** — Out of scope
* **C8.1 Tier Placement** — No verifiability grading
* **C8.2 Mechanism-to-Requirement Fit** — No mechanism-fit rule
* **C8.3 Chain Integrity and Self-Enforcement (Tier 4)** — No self-enforcement concept
* **C9.1 Locating Evidence on the System Surface** — Not addressed
* **C9.2 Layer Coverage** — Not addressed
* **C10.1 Conformance Claims** — No conformance regime
* **C10.2 Trust-Assumption Disclosure** — Not addressed
* **C10.3 Continuously Monitored Operation** — Not addressed

*Coding granularity is the individual requirement; the section rows above summarize the requirements beneath them. Where a section is coded uniformly the summary is exact, and where it is mixed the Covered column and the gap list name what is missing. Row-level detail is in the [coding sheet](coding_sheet.csv). This is seed coding by a single coder and has not yet had the second-coder pass the [rubric](rubric.md) requires.*

<!-- END GENERATED MAPPING -->

## Threat-Model Role (the primary crosswalk)

For the threat-by-threat view of what PoC evidence reaches — Full · Strong · Partial ·
Not addressed across all 29 threats — see [Appendix C: Threat Model](../0.1/en/0x92-Appendix-C_Threat-Model.md).

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
