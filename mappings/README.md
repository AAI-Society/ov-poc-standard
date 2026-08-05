# Framework Mappings (Crosswalks)

Proof-of-Control cross-references existing standards and frameworks rather than replacing them.
Almost none of the existing work produces independent evidence of what an agent did that holds
when the operator is the threat; Proof-of-Control is the evidence layer that sits alongside these
efforts and feeds them. This directory holds one crosswalk per framework referenced in
[Section 8 of the standard](../0.1/en/0x10-S08-Mapping-to-Existing-Standards.md).

> **✍️ [DRAFT] — mapping in progress.** The working group is classifying the mapping by domain of
> verification (proposed by Jim Schwoebel of Quome) and mapping it as a graph (led by David
> Thomson of Tesseract). Several crosswalks below need volunteers —
> **[sign up at advancedaisociety.org](https://advancedaisociety.org/)** to contribute one.

## Crosswalks

| Framework | Type | Relationship to Proof-of-Control | Crosswalk |
| --- | --- | --- | --- |
| MAESTRO (CSA) | Agent threat-modeling framework | Adopted as the System surface (Axis 2) in Section 5 | [maestro.md](maestro.md) |
| CSA AARM | Runtime enforcement standard | Complementary half: AARM enforces, PoC evidences | [csa-aarm.md](csa-aarm.md) |
| CSA AI Controls Matrix (AICM) | Control catalog | Crosswalk maintained separately by WG decision | [csa-aicm.md](csa-aicm.md) |
| OWASP (Agentic Top 10, LLM Top 10, AIVSS, AISVS) | Threat catalogs & verification standard | Threat-source for the PoC threat model; Security-domain alignment target | [owasp.md](owasp.md) |
| MITRE ATLAS | Adversarial threat catalog | Threat-source for the PoC threat model | [mitre-atlas.md](mitre-atlas.md) |
| NIST AI RMF (& AI 100-2) | Risk-governance framework | PoC produces the evidence that makes its requirements checkable | [nist-ai-rmf.md](nist-ai-rmf.md) |
| ISO/IEC 42001 | AI management system standard | Complementary; supplies the V&V vocabulary PoC uses | [iso-iec-42001.md](iso-iec-42001.md) |
| SOC 2 | Organizational attestation | PoC is SOC-2-grade in role, with a cryptographic stage SOC 2 never had | [soc-2.md](soc-2.md) |
| EU AI Act | Regulation | PoC evidence lets the Act be enforced against evidence, not filings | [eu-ai-act.md](eu-ai-act.md) |
| Zero Trust (NIST SP 800-207; Anthropic Zero Trust for AI Agents) | Security architecture / vendor framework | Zero Trust enforces at runtime; PoC shows independently that control held | [zero-trust.md](zero-trust.md) |
| Confidential Computing (TEEs) | Mechanism | One valid mechanism for delivering PoC, not the property itself | [confidential-computing.md](confidential-computing.md) |
| AIUC-1 | AI audit / certification framework | Portability-domain alignment target (cross-platform auditing) | [aiuc-1.md](aiuc-1.md) |

## The By-Domain Mapping (current working state)

For each domain of verification, the architectural mechanisms that produce the evidence and the
external standards to align with:

| Domain | Source architectural mechanism | Targets for external alignment |
| --- | --- | --- |
| Provenance | *working group to complete* | *to complete* |
| Privacy | TEEs, local-only inference enclaves | HIPAA / HAARF data governance, [EU AI Act](eu-ai-act.md) conformance |
| Portability | Agent Resource Discovery Spec, Open Handshakes | [AIUC-1](aiuc-1.md) cross-platform auditing |
| Authorization | Cryptographic hash chains, ZKML | [SOC 2 Type II](soc-2.md) (proving runtime execution matched policy) |
| Identity | W3C CID, WIMSE / IETF AI-Auth | HAARF audit logs, CSA Vanta Agent Trust Controls |
| Security | [OWASP AIVSS](owasp.md), SSF / CAEP | [OWASP Top 10 for Agentic AI](owasp.md), [NIST AI RMF](nist-ai-rmf.md) |

## Other Efforts Being Mapped

The working group is also mapping Proof-of-Control against: the IEEE 7000-series, zero-trust
architecture (NIST SP 800-207), vendor toolkits (Microsoft Agent Governance Toolkit, Mastercard
Verifiable Intent, Ping Identity, KYA), agent observability tooling, CSA Vanta Agent Trust
Controls, C2PA content provenance, SLSA / supply-chain attestation, and the Agent Resource
Discovery Specification. If you maintain a standard, or you see a crosswalk that is needed,
propose it.

## Contributing a Crosswalk

Working from the initial mapping, contributors extend the standard's crosswalks to other
standards and frameworks. Several crosswalks are marked
**⚠️ [WG-INPUT NEEDED] — volunteer needed**. To take one on, join a working group:
**[advancedaisociety.org](https://advancedaisociety.org/)**.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
