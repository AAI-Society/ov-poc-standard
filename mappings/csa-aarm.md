# Crosswalk: CSA AARM (Autonomous Action Runtime Management)

| | |
| --- | --- |
| **Framework type** | Runtime enforcement standard (Cloud Security Alliance, contributed by Vanta) |
| **Corpus version** | 2026 publication — [access](https://cloudsecurityalliance.org/) · [corpus provenance](corpus/README.md) |
| **Relationship** | Complementary halves of agentic assurance — AARM is the enforcement half, PoC the evidence half |
| **Coding status** | Draft seed coding, single coder — [rubric](rubric.md) |

## The Relationship

CSA's AARM defines runtime enforcement: it intercepts agent actions at the boundary and approves, modifies, defers, or denies them. Proof-of-Control defines the independent, tamper-evident evidence of what the agent did. The two share the same architectural spot — the action boundary — which is why the mapping below contains exact matches precisely there (action interception, the runtime gateway) and no-matches everywhere evidence-independence begins.

| AARM (runtime enforcement) | Proof-of-Control (independent evidence) |
| --- | --- | --- |
| Question | What may the agent do at the action boundary? | What did the agent actually do, and can anyone verify it? |
| When | At execution, before the action | At execution, producing evidence of the action |
| Trust | Operator-run enforcement and audit trail | Independent, tamper-evident, checkable by others |
| Scope | Agent actions inside one deployment (the runtime gateway) | System-wide and portable, across vendors, layers, and jurisdictions |
| Certifiable? | Yes; a vendor-neutral CSA standard with a conformance regime | Yes; the standard, plus forthcoming independent certification |

Where they meet: AARM mints the tamper-evident receipt at the runtime gateway inside one deployment; PoC carries that evidence outward and makes it independently verifiable across organizations. Enforcement decides what an agent may do; verification shows what it actually did. Prevention can fail silently; detection cannot.

## Requirement-Level Mapping

<!-- BEGIN GENERATED MAPPING (tools/generate_crosswalks.py) -->

**Coverage: 50%** of the 118 Proof-of-Control requirements (13 exact matches, 46 partial matches, 59 not covered), computed per the [mapping rubric](rubric.md) from the row-level [coding sheet](coding_sheet.csv). *Draft seed coding — pending working-group validation.* To change this table, edit the coding sheet and run `python3 tools/generate_crosswalks.py`.

**How to read the Match column** ([full rubric](rubric.md)): **Exact** — the framework has a clause equivalent in scope and intent. **Partial** — the framework covers the topic, but not with PoC's operator-independent evidence (or not at the same depth). **None** — the framework has no analogous provision.

| PoC section | Reqs | Match | Closest framework clause(s) | Rationale |
| --- | :---: | :---: | --- | --- |
| [C1.1 Model and Artifact Provenance](../0.1/en/0x10-C01-Provenance.md) | 5 | None | — | Artifact provenance outside runtime-enforcement scope |
| [C1.2 Input and Data Lineage](../0.1/en/0x10-C01-Provenance.md) | 4 | None | — | Outside scope |
| [C1.3 Compute Substrate Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | None | — | Outside scope |
| [C1.4 Privacy-Preserving Provenance](../0.1/en/0x10-C01-Provenance.md) | 2 | None | — | Outside scope |
| [C2.1 Data-Access Evidence](../0.1/en/0x10-C02-Privacy.md) | 3 | Partial | Runtime gateway — data-action gating | Runtime gating of data-touching actions produces access records; operator-run audit trail |
| [C2.2 Policy and Consent Enforcement](../0.1/en/0x10-C02-Privacy.md) | 5 | Partial | Policy evaluation at the action boundary | Policy enforcement at the action boundary covers purpose/consent policy checks at runtime |
| [C2.3 Privacy-Preserving Verification Mechanisms](../0.1/en/0x10-C02-Privacy.md) | 3 | None | — | Cryptographic privacy mechanisms not addressed |
| [C2.4 Evidence Handling for Protected Data](../0.1/en/0x10-C02-Privacy.md) | 2 | None | — | Evidence-store handling not addressed |
| [C3.1 Boundary-Crossing Evidence](../0.1/en/0x10-C03-Portability.md) | 2 | None | — | Boundary-crossing evidence not addressed |
| [C3.2 Cross-Environment Continuity](../0.1/en/0x10-C03-Portability.md) | 3 | None | — | Not addressed |
| [C4.1 Authority and Scope Enforcement](../0.1/en/0x10-C04-Authorization.md) | 8 | Exact | Action interception: approve / modify / defer / deny | Action interception with approve/modify/defer/deny decisions matches scope enforcement and evidenced rejection |
| [C4.2 Delegation](../0.1/en/0x10-C04-Authorization.md) | 4 | Partial | Authority evaluation at the boundary | Authority evaluation at the boundary partially covers delegation checks |
| [C5.1 Agent and Principal Binding](../0.1/en/0x10-C05-Identity.md) | 4 | Partial | Agent identity as authorization input | Agent identity as an input to runtime authorization; no principal-binding tokens |
| [C5.2 Inter-Agent Identity](../0.1/en/0x10-C05-Identity.md) | 2 | None | — | Inter-agent identity not addressed |
| [C6.1 Execution Environment Integrity](../0.1/en/0x10-C06-Security.md) | 4 | Partial | Runtime control enforcement | Runtime control enforcement covers controls-held aims; environment attestation not addressed |
| [C6.2 Isolation and Confidential Execution](../0.1/en/0x10-C06-Security.md) | 3 | None | — | Isolation proof not addressed |
| [C6.3 Cryptographic Key Lifecycle](../0.1/en/0x10-C06-Security.md) | 5 | None | — | Key lifecycle not addressed |
| [C7.1 Generation at the Action Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 5 | Exact | The AARM runtime gateway | The AARM runtime gateway is the same interception boundary, mediating all agent actions |
| [C7.2 The Contemporaneous Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | Partial | Execution-time audit trail | Enforcement produces execution-time records; operator-run, not operator-independent |
| [C7.3 The Tamper-Evident Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 3 | Partial | Gateway receipts | Tamper-evident receipts at the gateway; trust remains rooted in the deployment operator |
| [C7.4 The Transparent Property](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 1 | None | — | No trust-assumption disclosure |
| [C7.5 The Determinism Boundary](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 2 | None | — | Not addressed |
| [C7.6 Evidence Custody and Resilience](../0.1/en/0x10-C07-Evidence-Generation-and-Properties.md) | 6 | Partial | Deny/failure decisions | Deny/failure decisions at the gateway cover failure events; fail-closed evidence gating unspecified |
| [C8.1 Tier Placement](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 8 | None | — | No verifiability grading |
| [C8.2 Mechanism-to-Requirement Fit](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 2 | None | — | No mechanism-fit rule |
| [C8.3 Chain Integrity and Self-Enforcement (Tier 4)](../0.1/en/0x10-C08-Verifiability-Tiers.md) | 5 | None | — | No self-enforcement concept |
| [C9.1 Locating Evidence on the System Surface](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | None | — | Not addressed |
| [C9.2 Layer Coverage](../0.1/en/0x10-C09-System-Surface-MAESTRO.md) | 3 | None | — | Not addressed |
| [C10.1 Conformance Claims](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 8 | Partial | CSA conformance regime | CSA conformance regime with independent review partially parallels claim requirements |
| [C10.2 Trust-Assumption Disclosure](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 2 | None | — | No trust-assumption disclosure |
| [C10.3 Continuously Monitored Operation](../0.1/en/0x10-C10-Conformance-and-Disclosure.md) | 7 | Partial | Continuous runtime enforcement | Continuous runtime enforcement aligns with continuous-operation intent |

### Gap Analysis (what this framework does not cover)

* **C1.1 Model and Artifact Provenance** — Artifact provenance outside runtime-enforcement scope
* **C1.2 Input and Data Lineage** — Outside scope
* **C1.3 Compute Substrate Provenance** — Outside scope
* **C1.4 Privacy-Preserving Provenance** — Outside scope
* **C2.3 Privacy-Preserving Verification Mechanisms** — Cryptographic privacy mechanisms not addressed
* **C2.4 Evidence Handling for Protected Data** — Evidence-store handling not addressed
* **C3.1 Boundary-Crossing Evidence** — Boundary-crossing evidence not addressed
* **C3.2 Cross-Environment Continuity** — Not addressed
* **C5.2 Inter-Agent Identity** — Inter-agent identity not addressed
* **C6.2 Isolation and Confidential Execution** — Isolation proof not addressed
* **C6.3 Cryptographic Key Lifecycle** — Key lifecycle not addressed
* **C7.4 The Transparent Property** — No trust-assumption disclosure
* **C7.5 The Determinism Boundary** — Not addressed
* **C8.1 Tier Placement** — No verifiability grading
* **C8.2 Mechanism-to-Requirement Fit** — No mechanism-fit rule
* **C8.3 Chain Integrity and Self-Enforcement (Tier 4)** — No self-enforcement concept
* **C9.1 Locating Evidence on the System Surface** — Not addressed
* **C9.2 Layer Coverage** — Not addressed
* **C10.2 Trust-Assumption Disclosure** — No trust-assumption disclosure

*Match granularity is the PoC section; every requirement in a section carries its section's coding in the [coding sheet](coding_sheet.csv). Requirement-level refinement is the working group's next pass.*

<!-- END GENERATED MAPPING -->

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
