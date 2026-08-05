# Preface: How to Read This Standard

This standard has two kinds of content, separated by section.

**The standard is the normative core: Sections 3 to 7.** These are the requirements an
implementer must meet, and they are what is under change control as the versioned specification:
terms and definitions ([Section 3](0x10-S03-Terms-and-Definitions.md)), what must be verified
([Section 4](0x10-S04-What-Must-Be-Verified.md)), where in the system
([Section 5](0x10-S05-System-Surface.md)), the evidence and its grading
([Section 6](0x10-S06-Evidence-and-Grading.md)), and conformance
([Section 7](0x10-S07-Conformance.md)). Requirements language follows RFC 2119: MUST and MUST NOT
are absolute; SHOULD and SHOULD NOT are strong recommendations you may deviate from with good
reason; MAY is optional. Only normative sections use these as requirements.

**All other sections are the case for the standard, and are informative.** The introduction
([Section 1](0x10-S01-Introduction.md)), why verification matters
([Section 2](0x10-S02-Why-Verification-Matters.md)), the mapping to existing standards
([Section 8](0x10-S08-Mapping-to-Existing-Standards.md)), and the use cases
([Section 9](0x10-S09-Use-Cases.md)) explain and motivate the standard; they add no requirements.

**How unfinished items are marked:**

* `⚠️ [WG-INPUT NEEDED]` — open working-group issues, or the working group still has to decide
  something. A commenter can find every open decision by searching for that tag.
* `✍️ [DRAFT]` — a whole section still being written.

Formal change proposals (issues and pull requests) are made against the normative core; the
informative material rides alongside as clearly-marked context or lives as companion documents.

## One-Page Overview

Everything the standard describes is about one thing: evidence of what the agent actually did —
the execution record of its actions and their effects — in a form others can check. The overview
below reads as the questions a reader meets, in order, and works as the table of contents.

| Question | In short | Section | Part of the standard? |
| --- | --- | :---: | --- |
| Who is this for, and how do they use it? | Security practitioners and auditors first, then business and governance owners, in any organization. An operational framework, like FinOps for cloud value, that lets technical and non-technical people make AI governance decisions together. | [1](0x10-S01-Introduction.md) | No (context) |
| What is this a standard for? | Open Verification, the category for any industry, achieved through Proof-of-Control, the approach for AI agents. | [1](0x10-S01-Introduction.md) | No (introduction; precise terms in Section 3) |
| How is it designed? | The seven design principles: industry-led, insurance-ready, speed, interoperable, technology-neutral, vendor-neutral, and open and independent. | [1](0x10-S01-Introduction.md) | No (context) |
| Why does verification matter? | The Verifiability Gap, the threat landscape, and the stakes for society: the risks agents create, and why verification is a check on concentrated power. | [2](0x10-S02-Why-Verification-Matters.md) | No (context) |
| What do the key terms mean? | Open Verification, Proof-of-Control, the six domains, the four Verifiability Tiers, and the evidence properties, defined precisely. | [3](0x10-S03-Terms-and-Definitions.md) | **Yes** |
| What must be verified? | The six domains of verification, each with its verifiable facts: Provenance, Privacy, Portability, Authorization, Identity, Security. | [4](0x10-S04-What-Must-Be-Verified.md) | **Yes** |
| Where in the system does it apply? | The System surface (Axis 2), with MAESTRO as today's framework: which layer of the agent stack the evidence covers. The axis is ours; the framework is pluggable. | [5](0x10-S05-System-Surface.md) | **Yes** (the axis; MAESTRO and the mechanisms are reference) |
| How independently can it be verified? | The Verifiability Tiers, four tiers: who you must trust — the operator, a third party, the mathematics, or no one. | [6](0x10-S06-Evidence-and-Grading.md) | **Yes** |
| Is the evidence any good? | The evidence properties: binary, contemporaneous, tamper-evident, transparent. Whether the evidence is the right kind: made at run time, unforgeable, honest about what it still trusts. | [6](0x10-S06-Evidence-and-Grading.md) | **Yes** |
| How thoroughly was the claim checked? | The three conformance stages: Self-Declared, Third-Party Assessed, Continuously Monitored. | [7](0x10-S07-Conformance.md) | **Yes** |
| How does it relate to existing standards? | The standards mapping, classified by domain and in progress: the AARM and CSA complementary halves, plus NIST AI RMF, ISO/IEC 42001, SOC 2, OWASP, the EU AI Act and others, cross-referenced, not replaced. | [8](0x10-S08-Mapping-to-Existing-Standards.md) | No (context) |
| What does it look like in practice? | Worked use cases exercising the six domains, the Verifiability Tiers, and the System surface. | [9](0x10-S09-Use-Cases.md) | No (context) |

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
