# Section 3 — Terms and Definitions (normative)

***This section answers:*** *What do the key terms mean? — Open Verification, Proof-of-Control,
the six domains, the four Verifiability Tiers, and the evidence properties, each defined
precisely.*

This section defines the terms the standard uses, and the definitions here are normative. Where a
term is enumerated or graded, the definition states what it is and points to the section that
specifies it: what must be verified ([Section 4](0x10-S04-What-Must-Be-Verified.md)), where in
the system ([Section 5](0x10-S05-System-Surface.md)), the evidence and its grading
([Section 6](0x10-S06-Evidence-and-Grading.md)), and conformance
([Section 7](0x10-S07-Conformance.md)).

## Requirements Language

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY,
and OPTIONAL in this document's normative sections are to be interpreted as described in RFC 2119
and RFC 8174 when, and only when, they appear in all capitals. A conformance claim is assessed
against the MUST and MUST NOT requirements; SHOULD-level items are strong recommendations a
conformant implementation is expected to weigh; MAY-level items are optional. Requirements
language appears only in the normative sections (3 to 7); the informative sections carry no
requirements.

## The Core Concepts

**Open Verification** is open, independent, graded verification that a system's controls are
implemented and hold, method and evidence both open to inspection, graded by how much you must
trust to believe it. Verification is open when what you must trust is a mechanism anyone can
verify rather than a party. It applies to any system, not only AI.

**Proof-of-Control** is open verification that the controls governing an agent system are
implemented and hold, graded on the four Verifiability Tiers by how independently that can be
verified. For each control it claims, across the six domains (Provenance, Privacy, Portability,
Authorization, Identity, Security), a conformant implementation MUST produce evidence, generated
by the enforcing mechanism at execution time, that the control held; place that evidence on the
Verifiability Tiers; and disclose its residual trust assumptions. A system has Proof-of-Control
when, and only when, its evidence reaches Tier 3 or Tier 4.

**What Proof-of-Control does not do:** it does not judge whether an agent's outputs were
substantively correct, fair, or wise, or whether the controls the operator chose were adequate
for the risk. Those remain human judgment; Proof-of-Control composes with evaluation and
oversight, it does not replace them.

**Proof-of-Control, in plain terms:** When your organization lets an AI agent act on its behalf,
approve something, move money, pull a record, Proof-of-Control is how you *prove*, rather than
promise, that the agent stayed inside the rules you set. Think of it like a public notary for
your agents' actions, with one difference that changes everything: no one has to trust the
notary. The proof can be verified by anyone, an auditor, an insurer, a regulator, or your own
board, without taking your word or your vendor's.

**Verifiability Gap:** the absence of evidence of what an AI system did.

**Verification:** establishing what a system did on the basis of evidence rather than assertion.
The specific modes are *attest* (a signed attestation), *show* or *evidence* (a record of what a
system did), and *prove* (a mathematical or cryptographic proof). "Prove" is reserved for genuine
cryptographic proofs and for the coined name Proof-of-Control; what an agent did is shown or
evidenced, never "proven."

**Execution record:** the record of an agent's actions and their effects. It is where
verification is performed.

**Chain of custody:** a continuous, verifiable trail binding each action to the identity and
authority under which it was taken, so that control can be shown to have held from end to end.

## The Actors

**Agent:** an AI system that acts, planning, calling tools, and taking actions that have
effects, on behalf of a principal.

**Operator:** the party that deploys and runs the agent.

**Principal:** the party on whose behalf the agent acts and whose authority it exercises, a
person or an organization.

## What Is Verified

**Domain of verification:** one of the six areas the standard produces evidence about. The six
domains are Provenance, Privacy, Portability, Authorization, Identity, and Security. Enumerated,
each with its verifiable facts, in [Section 4](0x10-S04-What-Must-Be-Verified.md).

**Verifiable fact:** a deterministic, true-or-false statement about an agent's execution, for
example which data was read, which authority was exercised, or which model ran. Verifiable facts
sit inside the domains; [Section 4](0x10-S04-What-Must-Be-Verified.md) lists them.

**Determinism boundary:** the line between what the standard verifies and what it does not.
Verification establishes deterministic facts about execution; it does not establish the
correctness, reasoning, intent, fairness, or future behavior of a model. Stated in full in
[Section 4](0x10-S04-What-Must-Be-Verified.md).

## The Evidence and Its Grading

**Evidence property:** one of the four qualities evidence must have to count under this standard:
binary, contemporaneous, tamper-evident, and transparent. Defined in
[Section 6](0x10-S06-Evidence-and-Grading.md).

**Verifiability Tiers:** the scale that grades evidence by how independently it can be verified,
that is, how much you must trust to believe it. It has four tiers: Tier 1 Assertion, Tier 2
Attestation, Tier 3 Independently-Verifiable, and Tier 4 Self-Enforcing. Claims-based AI sits at
Tier 1. Defined and graded in [Section 6](0x10-S06-Evidence-and-Grading.md).

**Tier:** a position on the Verifiability Tiers (Tiers 1 to 4). An unqualified number always
refers to a Tier.

## Conformance

**Conformance:** how thoroughly a claim of meeting this standard has been checked. Conformance
grades the audit of the claim, a separate axis from the Verifiability Tiers, which grades the
evidence itself.

**Conformance stage:** one of the three named stages of conformance rigor: Self-Declared,
Third-Party Assessed, and Continuously Monitored. Conformance stages are named, never numbered,
and always qualified as conformance stages. Defined in [Section 7](0x10-S07-Conformance.md).

## Where in the System

**System surface:** where in the agent stack a piece of evidence applies. The System surface is a
pluggable axis; MAESTRO is the first framework that fills it, with layers numbered 1 to 7.
Treated in [Section 5](0x10-S05-System-Surface.md).

**Layer:** a position in the System-surface framework (for MAESTRO, Layers 1 to 7). "Layer"
refers to the System surface, never to the Verifiability Tiers or to conformance, and never to
verification itself.

## Naming Discipline

To keep the three graded axes distinct, each has its own word:

* **Tier** grades the evidence (the Verifiability Tiers). Numbered 1 to 4.
* **Stage** grades the audit of the claim (conformance). Named, never numbered.
* **Layer** locates the evidence in the stack (the System surface / MAESTRO). Numbered per the
  framework.

An unqualified number always means a Tier.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
