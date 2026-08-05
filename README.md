# Open Verification: the Proof-of-Control Standard for Agents (PoC)

[![CC BY 4.0][cc-by-shield]][cc-by]
[![Status: Working Draft](https://img.shields.io/badge/Status-Working%20Draft%20v0.1.4-orange.svg)](0.1/en/0x01-Frontispiece.md)
[![Steward: Advanced AI Society](https://img.shields.io/badge/Steward-Advanced%20AI%20Society-6f42c1.svg)](https://advancedaisociety.org/)

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: https://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg

> **📣 Get involved:** Proof-of-Control is developed in the open and stewarded by the
> **[Advanced AI Society](https://advancedaisociety.org/)**. Join a working group, comment on
> the draft, or become a member — **[sign up at advancedaisociety.org](https://advancedaisociety.org/)**.

## What is Proof-of-Control?

The **Proof-of-Control Standard (PoC)** is a catalogue of verifiable requirements for AI agent systems: independent, tamper-evident evidence of what an agent actually did — the data it touched, the authority it exercised, the tools it invoked — in a form anyone can check without trusting the operator. It gives security practitioners, auditors, insurers, and governance owners a structured framework to make, assess, and price claims about agent behavior.

PoC is the approach this standard defines for reaching **Open Verification**: verification whose root of trust is a mechanism anyone can verify — mathematics, or a decentralized protocol — rather than a party. Every requirement follows the same philosophy as [OWASP AISVS/ASVS](https://github.com/OWASP/AISVS): **verifiable, testable, and implementable**.

A system has Proof-of-Control when, and only when, its evidence reaches **Tier 3 or Tier 4** of the Verifiability Tiers — the binary threshold that makes the category procurable: *"Does your AI have Proof-of-Control?"* is a yes-or-no question.

## Project Leadership

The standard is led by co-chairs **Ken Huang** and **Tricia Wang**, produced by the Proof-of-Control Initiative's working groups, reviewed by a Distinguished Review Board, and stewarded by the [Advanced AI Society](https://advancedaisociety.org/) as a public good (see [Governance](docs/governance.md)). The Proof-of-Control Lab is being established as a community lab at Linux Foundation Decentralized Trust.

---

### What Proof-of-Control is NOT

* **Not validation.** PoC shows that an agent stayed inside the control boundaries that were set; it does not judge whether those boundaries were the right ones, or whether an output was correct, fair, or wise. That judgment stays a human responsibility ([C7.5](0.1/en/0x10-C07-Evidence-Generation-and-Properties.md)).
* **Not a governance or risk framework.** Governance is covered by [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [ISO/IEC 42001](https://www.iso.org/standard/42001), and the EU AI Act; PoC produces the evidence that makes their requirements checkable.
* **Not a runtime enforcement layer.** Enforcement (what an agent *may* do) is CSA AARM's half; PoC is the evidence half (what it *actually did*, checkable by others).
* **Not tied to any technology or vendor.** The standard defines what the evidence must be, not which mechanism produces it, and no member's product is the reference implementation.

### How Proof-of-Control complements other standards

| Standard | Focus | PoC relationship |
| --- | --- | --- |
| [CSA MAESTRO](mappings/maestro.md) | Agent threat modeling (7-layer stack) | Adopted as PoC's System surface ([C9](0.1/en/0x10-C09-System-Surface-MAESTRO.md)) |
| [CSA AARM](mappings/csa-aarm.md) | Runtime enforcement at the action boundary | Complementary halves: AARM enforces, PoC evidences |
| [OWASP Top 10s / AIVSS / AISVS](mappings/owasp.md) | Agent & LLM threat awareness; AI security controls | Threat source for PoC's threat model; PoC adds the independent-evidence layer |
| [MITRE ATLAS](mappings/mitre-atlas.md) | Adversarial AI threat catalog | Threat source for PoC's threat model ([Appendix C](0.1/en/0x92-Appendix-C_Threat-Model.md)) |
| [NIST AI RMF](mappings/nist-ai-rmf.md) | AI risk governance | PoC supplies the runtime evidence RMF-aligned controls can be checked against |
| [ISO/IEC 42001](mappings/iso-iec-42001.md) | AI management systems | PoC evidences that declared controls held at execution |
| [SOC 2](mappings/soc-2.md) | Organizational controls attestation | PoC is SOC-2-grade in role, with a cryptographic stage SOC 2 never had |
| [EU AI Act](mappings/eu-ai-act.md) | Regulation | PoC evidence lets rules be enforced against evidence, not filings |
| [Zero Trust](mappings/zero-trust.md) · [Confidential Computing](mappings/confidential-computing.md) · [AIUC-1](mappings/aiuc-1.md) | Architecture / mechanism / audit | See the [mappings directory](mappings/README.md) |

---

## Latest Version

The latest version is **Working Draft v0.1.4**, open for public comment until October 30, 2026:

| Format | Link |
| --- | --- |
| Markdown (source) | [Browse `0.1/en/`](0.1/en) |
| Companion documents (the case for the standard) | [Browse `docs/`](docs) |

Version 1.0 is targeted for **February 1, 2027** ([roadmap](docs/roadmap.md)).

## Requirement Levels

Each PoC requirement is assigned a level (1, 2, or 3) indicating the depth of assurance:

| Level | Description | When to use |
| :---: | --- | --- |
| **1** | Baseline requirements for any Proof-of-Control claim; without these the claim does not clear the binary threshold. | Every system claiming Proof-of-Control. |
| **2** | Extended requirements for systems handling sensitive data or making consequential decisions; Third-Party Assessed readiness. | Production systems, regulated data, consequential agent actions. |
| **3** | Advanced requirements for high-assurance environments: Tier 4 self-enforcing execution and Continuously Monitored operation. | Critical infrastructure, high-value targets, cross-organizational agent chains. |

The levels grade the *requirements*; they are distinct from the **Verifiability Tiers** (1–4), which grade the *evidence* — see [Using Proof-of-Control](0.1/en/0x03-Using-Proof-of-Control.md) and the naming discipline in the [Glossary](0.1/en/0x90-Appendix-A_Glossary.md).

## How to use Proof-of-Control

* **During design.** Use requirements as an architecture checklist; the Action Interception Gateways ([C7](0.1/en/0x10-C07-Evidence-Generation-and-Properties.md)) are structural and hard to retrofit.
* **During development.** Build the per-domain evidence pipeline, choosing mechanisms from the [Proof-Mechanism Inventory](0.1/en/0x91-Appendix-B_Proof-Mechanism-Inventory.md).
* **During security assessments.** Use as the verification framework for a conformance stage ([C10](0.1/en/0x10-C10-Conformance-and-Disclosure.md)).
* **For procurement and insurance.** Ask the binary question — "does your system have Proof-of-Control?" — and compare vendors on their trust-assumption disclosures.

## Requirement Chapters

1. [C1: Provenance](0.1/en/0x10-C01-Provenance.md)
2. [C2: Privacy](0.1/en/0x10-C02-Privacy.md)
3. [C3: Portability](0.1/en/0x10-C03-Portability.md)
4. [C4: Authorization](0.1/en/0x10-C04-Authorization.md)
5. [C5: Identity](0.1/en/0x10-C05-Identity.md)
6. [C6: Security](0.1/en/0x10-C06-Security.md)
7. [C7: Evidence Generation & Properties](0.1/en/0x10-C07-Evidence-Generation-and-Properties.md)
8. [C8: Verifiability Tiers & the Binary Threshold](0.1/en/0x10-C08-Verifiability-Tiers.md)
9. [C9: System Surface (MAESTRO)](0.1/en/0x10-C09-System-Surface-MAESTRO.md)
10. [C10: Conformance & Trust-Assumption Disclosure](0.1/en/0x10-C10-Conformance-and-Disclosure.md)

Chapters C1–C6 are the **six domains of verification** — what must be verified. Chapters C7–C10 are the **cross-cutting requirements** — what the evidence must be, how it is graded, where it applies, and how claims are checked.

## Appendices

* [Appendix A: Glossary](0.1/en/0x90-Appendix-A_Glossary.md)
* [Appendix B: Proof-Mechanism & Controls Inventory](0.1/en/0x91-Appendix-B_Proof-Mechanism-Inventory.md) (the seven MAESTRO layer control tables)
* [Appendix C: Threat Model](0.1/en/0x92-Appendix-C_Threat-Model.md) (29 threats: coverage and out-of-scope boundaries)
* [Appendix D: Open Working-Group Issues](0.1/en/0x93-Appendix-D_Open-Issues.md) (every `⚠️ [WG-INPUT NEEDED]` decision)

## Companion Documents

The case for the standard — informative, no requirements:

* [Introduction: Open Verification, the concept, and the design principles](docs/introduction.md)
* [Why Verification Matters: the Verifiability Gap, economics, insurance, and the stakes for society](docs/why-verification-matters.md)
* [The Standards Landscape: where PoC sits in verifiable AI](docs/standards-landscape.md)
* [Use Cases](docs/use-cases.md) · [Roadmap & Timeline](docs/roadmap.md) · [Governance](docs/governance.md)
* [Framework mappings (crosswalks)](mappings/README.md)

---

## How to Reference PoC Requirements

Each requirement has an identifier in the format `C<chapter>.<section>.<requirement>`, where each element is a number — for example `C4.1.4`.

* The `C<chapter>` value corresponds to the chapter the requirement comes from; for example, all `C4.#.#` requirements are from the [Authorization](0.1/en/0x10-C04-Authorization.md) chapter.
* The `<section>` value corresponds to the section within that chapter; for example, all `C4.1.#` requirements are in the 'Authority and Scope Enforcement' section.
* The `<requirement>` value identifies the specific requirement, for example `C4.1.4`, which as of v0.1 of this standard is:

> Verify that the evaluated payload parameters of each tool invocation matched the exact structural schema authorized at execution time.

Since identifiers may change between versions, prefer the format `v<version>-C<chapter>.<section>.<requirement>`, for example: `v0.1-C4.1.4`. The `v` should always be lowercase. If identifiers are used without the version element, they should be assumed to refer to the latest content.

## Versioning

PoC uses a two-part version number, `v<MAJOR>.<MINOR>`. Each release is published as a numbered folder in this repository; once a version is released, its folder is locked and all future work happens in a new folder — the approach used by [OWASP ASVS](https://github.com/OWASP/ASVS) and [AISVS](https://github.com/OWASP/AISVS). The full policy is in [RELEASE.md](RELEASE.md).

```text
/
├── 0.1/        <- Working Draft v0.1.4 (public comment, in progress)
├── docs/       <- companion documents (the case for the standard)
├── mappings/   <- framework crosswalks
```

---

## Contributing

We welcome contributions from the community — see [CONTRIBUTING.md](CONTRIBUTING.md). The open working-group decisions that most need input are collected in [Appendix D](0.1/en/0x93-Appendix-D_Open-Issues.md). To report an issue with the standard itself, please open an issue; for security concerns, follow the [Security Policy](SECURITY.md).

**Membership is open to any organization — [sign up at advancedaisociety.org](https://advancedaisociety.org/).**

## License

The specification is under the **[Creative Commons Attribution 4.0 International][cc-by]** license. The certification mark ("Proof-of-Control Certified") is protected as a trademark so that only systems assessed as conformant may claim it.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/).
Help build the evidence layer for AI governance —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
