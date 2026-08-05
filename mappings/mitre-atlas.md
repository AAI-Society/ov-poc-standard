# Crosswalk: MITRE ATLAS

**Framework type:** Adversarial threat catalog for AI systems
**Relationship:** Threat source — one of the three established agent-threat catalogs the
Proof-of-Control threat model draws from. See
[Section 2](../docs/why-verification-matters.md) and
[Section 4](../0.1/en/0x92-Appendix-C_Threat-Model.md).

## How Proof-of-Control Uses ATLAS

The 27 threats in the Proof-of-Control threat landscape are drawn from MITRE ATLAS, NIST AI
100-2, and the [OWASP Top 10s for LLM and Agentic Applications](owasp.md), which converge on the
same core threat classes. The threat model in
[Section 4](../0.1/en/0x92-Appendix-C_Threat-Model.md) then states, for each threat, what
Proof-of-Control defends against and what is explicitly out of scope.

## Threat-Family Coverage Summary

| Threat family (ATLAS-aligned) | Representative PoC coverage |
| --- | --- |
| Instruction and goal manipulation | 🟡 Partial (prompt injection) to 🔵 Strong (poisoned goals); system-prompt leakage ⚪ not addressed |
| Memory, knowledge, and supply chain | 🔵 Strong (memory poisoning, model poisoning, supply chain); 🟡 Partial (RAG weakness) |
| Identity, authority, and inter-agent trust | 🔵 Strong across the family |
| Tools, actions, and effects | 🔵 Strong (tool misuse); 🟡 Partial (code execution, actuation, output handling) |
| Data exposure | 🔵 Strong (exfiltration evidence and gating) |
| Autonomy, drift, and lifecycle | 🔵 Strong (autonomy creep, scope creep); 🟡 Partial (behavioral drift) |
| Record integrity and resilience | 🟢 Full (audit tampering); 🟡 Partial (cascading failures); 🔵 Strong (coverage decay) |
| Human oversight and disclosure | 🟡 Partial (approval fatigue); 🔵 Strong (undisclosed AI / consent) |
| Output quality and availability | ⚪ Not addressed (misinformation, bias); 🟡 Partial (unbounded consumption) |

The honest edge of the claim: threats marked "not addressed" match the determinism boundary —
Proof-of-Control verifies what an agent did, not whether the output was correct, fair, or wise.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
