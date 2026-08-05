# Using Proof-of-Control

*This chapter is informative. It collects the practical entry points: how to get involved today,
how an operator will make a first claim, and how an evaluator reads one.*

| If you are | Start with |
| --- | --- |
| Taking part now (a contributor, member, insurer, or anyone) | [Getting involved](#getting-involved) |
| An operator planning to adopt the standard | [Making your first claim](#making-your-first-proof-of-control-claim) |
| An assessor, buyer, or insurer evaluating a claim | [Reading a claim](#reading-a-proof-of-control-claim) |

## Getting Involved

The standard is being developed in the open, and there are several ways to take part now.
**The front door for all of them is [advancedaisociety.org](https://advancedaisociety.org/) —
sign up there to join.**

* **Comment on the draft:** anyone can comment during public comment. To weigh in on the open
  decisions, search for `⚠️ [WG-INPUT NEEDED]` and comment there; those are the questions the
  working group most needs input on.
* **Join a working group:** there are six domain working groups, one for each domain of
  verification ([Section 4](0x10-S04-What-Must-Be-Verified.md)), plus an insurance working group
  where carriers, reinsurers, and actuaries define what the standard must carry to be priceable
  and insurable. [Sign up](https://advancedaisociety.org/) for the group closest to your
  expertise and contribute to authoring and extending its verifiable facts and the use cases that
  validate them.
* **Contribute a crosswalk:** working from the initial mapping
  ([Section 8](0x10-S08-Mapping-to-Existing-Standards.md) and
  [`mappings/`](../../mappings/README.md)), contributors extend the standard's crosswalks to
  other standards and frameworks. If you maintain a standard, or you see a crosswalk that is
  needed, propose it.
* **Strengthen the standard:** if you see a way to improve any section, comment on it.
  Contributors shape the standard, and their names stand behind the version that ships.

## Making Your First Proof-of-Control Claim

*This is how adoption will work once the standard is in use. It is laid out now so an adopter can
see the path.*

1. **Choose your domains:** decide which of the six domains you make claims in
   ([Section 4](0x10-S04-What-Must-Be-Verified.md)). You may claim a subset; you do not have to
   cover all six. For each domain you claim, you produce evidence for the verifiable facts you
   assert.
2. **Locate where the evidence is produced:** map each claim to where in the system it lives,
   using the System surface and its MAESTRO layers ([Section 5](0x10-S05-System-Surface.md)).
3. **Choose the mechanisms:** select the proof mechanisms that generate the evidence (the
   proof-mechanism taxonomy, [Section 5](0x10-S05-System-Surface.md)). Match the mechanism to the
   evidentiary requirement: a mechanism that proves an artifact's integrity at signing time
   proves nothing about its behavior at runtime.
4. **Meet the four evidence properties:** every piece of evidence must be binary,
   contemporaneous, tamper-evident, and transparent
   ([Section 6](0x10-S06-Evidence-and-Grading.md)).
5. **Grade each claim on the Verifiability Tiers:** place each claim at Tier 1 to 4
   ([Section 6](0x10-S06-Evidence-and-Grading.md)). To count as Proof-of-Control, the evidence
   must clear the binary threshold — Tiers 3 and 4: cryptographic evidence generated at execution
   time and checkable by parties other than you.
6. **Disclose your residual trust assumptions:** state, in the standardized disclosure, what
   still has to be trusted ([Section 6](0x10-S06-Evidence-and-Grading.md), the Transparent
   property; [Section 7](0x10-S07-Conformance.md)). This is what turns a yes-or-no claim into a
   risk-differentiable profile.
7. **Publish a Self-Declared conformance statement:** this is your entry point
   ([Section 7](0x10-S07-Conformance.md)). The statement names the system, the domains claimed,
   and for each claim the evidence properties met, the Tier reached, the mechanisms used, and the
   trust-assumption disclosure. Third-Party Assessed and Continuously Monitored come later.

For the infrastructure behind these steps, and the order to build it in, see the implementation
roadmap ([Roadmap and Timeline, Part B](0x20-Roadmap-and-Timeline.md)).

## Guidance for Implementers: Producing Evidence That Counts

These are not requirements; the requirements are in the specification. They are the habits that
tend to separate evidence that holds up from evidence that does not, drawn in part from Ken
Huang's Proof-of-Control framework for the Universal Commerce Protocol
([Section 9](0x10-S09-Use-Cases.md)).

* **Generate the evidence while the action happens, not after a dispute.** A contract creates a
  remedy after something goes wrong; evidence created at the moment of action is what lets anyone
  reconstruct what happened later. A system that plans to rebuild authority from mutable logs
  months afterward usually cannot. (This is the contemporaneous property of
  [Section 6](0x10-S06-Evidence-and-Grading.md), stated as a working habit.)
* **Scope authority to the action, not to the actor.** An agent's permission should be tied to
  the specific operation, its configuration, and its limits at the time it acts, not carried as a
  broad standing identity. Authority bound to its context cannot be replayed against a different
  action. (This extends the Authorization domain,
  [Section 4](0x10-S04-What-Must-Be-Verified.md).)
* **Carrying a signal is not enforcing it.** A system can transmit a consent flag, a policy, or a
  constraint and still not apply it. This standard asks for evidence that the constraint shaped
  behavior, not only that it was communicated. Transmission is a message; enforcement is a
  control. (This is why the Privacy and Authorization domains ask for enforcement evidence,
  [Section 4](0x10-S04-What-Must-Be-Verified.md).)

## Reading a Proof-of-Control Claim

*This is how an evaluator reads a claim once systems are conformant.*

If you are assessing, buying, or insuring a system, four things tell you what a claim is worth:

1. the **domains** it claims ([Section 4](0x10-S04-What-Must-Be-Verified.md)),
2. the **Verifiability Tier** of each claim ([Section 6](0x10-S06-Evidence-and-Grading.md)),
3. the **conformance stage** the claim was established at
   ([Section 7](0x10-S07-Conformance.md)), and
4. the **trust-assumption disclosure**.

Two systems can both be conformant and carry very different risk; the disclosure is what lets you
tell them apart ([Section 7](0x10-S07-Conformance.md)).

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
