# Crosswalk: OWASP (Agentic Top 10, LLM Top 10, AIVSS, AISVS)

**Framework type:** Threat catalogs, scoring system, and verification standard (OWASP)
**Relationship:** Threat source and Security-domain alignment target. Proof-of-Control points to
and complements OWASP's work rather than duplicating it — it produces the evidence that makes
OWASP requirements checkable. See
[Section 8](../docs/standards-landscape.md).

## OWASP Top 10 for LLM Applications & OWASP Top 10 for Agentic AI

These catalogs are two of the three established agent-threat sources (with
[MITRE ATLAS](mitre-atlas.md) and NIST AI 100-2) from which the 27 threats in the
Proof-of-Control threat landscape ([Section 2](../docs/why-verification-matters.md))
and threat model ([Section 4](../0.1/en/0x92-Appendix-C_Threat-Model.md)) are drawn. The
catalogs converge on the same core threat classes.

For each catalogued threat, the Proof-of-Control threat model states what the evidence defends
against and what is out of scope — for example:

| OWASP-class threat | PoC coverage | What PoC does |
| --- | --- | --- |
| Prompt injection / goal hijacking | 🟡 Partial | Gates and records the out-of-bounds action the injection attempts; the injection itself is out of scope |
| Excessive agency / over-permission | 🔵 Strong | Evidences what authority was exercised and whether actions stayed in bounds; gates over-scope |
| Tool misuse | 🔵 Strong | Evidences every tool call and its arguments; gates disallowed calls |
| Improper output handling | 🟡 Partial | Evidences the output and where it flowed; validation is the consuming system's job |
| Sensitive info exfiltration | 🔵 Strong | Evidences data access and boundary crossings; gates unauthorized egress |
| Misinformation / hallucination | ⚪ Not addressed | Correctness is out of scope (the determinism boundary) |

The full 29-row threat model is in [Section 4](../0.1/en/0x92-Appendix-C_Threat-Model.md).

## OWASP AIVSS (AI Vulnerability Scoring System)

AIVSS appears in the by-domain mapping as a **source architectural mechanism for the Security
domain**: it scores the severity of AI vulnerabilities, while Proof-of-Control produces the
runtime evidence that the corresponding security controls held.

## OWASP AISVS (AI Security Verification Standard)

AISVS is a community-driven catalogue of testable security requirements for AI-enabled systems
(the structural model for this repository). The relationship follows the standard's general
pattern: AISVS defines *which controls* an AI system should implement and how to test them;
Proof-of-Control defines what *independently verifiable evidence* that those controls held at
execution must be, graded on the Verifiability Tiers. An AISVS-verified system can additionally
claim Proof-of-Control when its control evidence reaches Tier 3 or 4.

## By-Domain Alignment

| PoC domain | OWASP alignment |
| --- | --- |
| Security | OWASP AIVSS (source mechanism); OWASP Top 10 for Agentic AI (external alignment target) |

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
