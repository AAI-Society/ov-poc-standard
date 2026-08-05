# Crosswalk: SOC 2

**Framework type:** Organizational controls attestation (AICPA)
**Relationship:** Complementary — Proof-of-Control is SOC-2-grade in role, with a cryptographic
stage SOC 2 never had. It does not replace SOC 2; it fills a gap SOC 2 was not designed to
address for AI agents. See
[Section 8](../docs/standards-landscape.md).

## The Distinction

SOC 2 attests that an organization's controls exist and were tested by an auditor; it is
institutional assurance about the organization. Proof-of-Control is independently verifiable
evidence of what the system actually did.

| | SOC 2 | Proof-of-Control |
| --- | --- | --- |
| Question answered | "Did the organization implement the controls it said it would?" | "Did the AI system operate within its defined control boundaries, and can anyone verify?" |
| Subject | The organization | The agent system's execution |
| Evidence | Auditor-tested controls, point-in-time or over a period | Mechanism-generated, tamper-evident, contemporaneous execution evidence |
| Trust required | The auditor and the operator's records | The cryptographic mechanism (Tiers 3–4) |

## Adoption Pattern

An insurer or buyer can require Proof-of-Control the way they already require SOC 2 or
ISO 27001. SOC 2 became effectively mandatory for software through the insurance and procurement
chain rather than through regulation — the dynamic this standard is built to activate for agents
([Section 2](../docs/why-verification-matters.md), Insurance is the forcing
function).

## By-Domain Alignment

| PoC domain | SOC 2 alignment |
| --- | --- |
| Authorization | SOC 2 Type II — proving runtime execution matched policy |

## Peer Assurance Ladder

| Proof-of-Control Stage | SOC 2 peer |
| --- | --- |
| Third-Party Assessed | SOC 2 (alongside CSA STAR Level 2, Common Criteria EAL, FIPS 140 validation) |

## Status

> **📌 [INSERT]** — an early-draft nine-dimension side-by-side exists as a companion crosswalk
> tab, "Proof-of-Control in the verifiable-AI landscape," to be merged here.
> **⚠️ [WG-INPUT NEEDED] — volunteer needed to develop out the crosswalk.**
> [Sign up at advancedaisociety.org](https://advancedaisociety.org/) to contribute.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
