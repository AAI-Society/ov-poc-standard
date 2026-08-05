# Crosswalk: CSA AARM (Autonomous Action Runtime Management)

**Framework type:** Runtime enforcement standard (Cloud Security Alliance, contributed by Vanta)
**Relationship:** Complementary halves of agentic assurance — AARM is the enforcement half,
Proof-of-Control is the evidence half. See
[Section 8](../0.1/en/0x10-S08-Mapping-to-Existing-Standards.md).

## What AARM Is

CSA's AARM defines runtime enforcement: it intercepts agent actions at the boundary and
approves, modifies, defers, or denies them.

## The Complementary Mapping

|  | AARM (runtime enforcement) | Proof-of-Control (independent evidence) |
| --- | --- | --- |
| Question | What may the agent do at the action boundary? | What did the agent actually do, and can anyone verify it? |
| When | At execution, before the action | At execution, producing evidence of the action |
| Trust | Operator-run enforcement and audit trail | Independent, tamper-evident, checkable by others |
| Role | The enforcement half | The evidence half |
| Scope | Agent actions inside one deployment (the runtime gateway) | System-wide and portable, across vendors, layers, and jurisdictions |
| Certifiable? | Yes; a vendor-neutral CSA standard with a conformance regime and independent review | Yes; the standard, plus forthcoming independent certification |

## Where They Meet

AARM mints the tamper-evident receipt at the runtime gateway inside one deployment;
Proof-of-Control carries that evidence outward and makes it independently verifiable across
organizations, for an auditor, insurer, or regulator. AARM enforces and records;
Proof-of-Control shows, independently, what the system did.

Enforcement decides what an agent may do; verification shows what it actually did. Enforcement
still leaves an audit trail the operator runs — the operator's word again. Prevention can fail
silently; detection cannot. Proof-of-Control is not a competing runtime layer; the two are
designed to compose.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
