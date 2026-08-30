# Proposal: make the determinism boundary and the domain-declaration duty normative

**Date:** 2026-08-30 · **Status:** proposal only, no file under `0.1/en/` has been edited.

**Source of the text:** Working Draft v0.1.4 of the paper, Section 4, paragraphs 312 and 320. Both are written as requirements in the paper and appear nowhere in the repository, which carries the definitions without the obligations.

**Targets:** `0.1/en/0x10-C07-Evidence-Generation-and-Properties.md` and `0.1/en/0x10-C10-Conformance-and-Disclosure.md`.

---

## Why this is a proposal rather than an edit

The paper states both as MUST and MUST NOT. The repository has the determinism boundary as a glossary definition and the six domains as chapters, with no requirement that an implementation stay inside the first or declare against the second. Moving the obligations across adds requirements, so the working group rules on them.

## P1 · The determinism boundary

**Add**, as a requirement under C7:

> A conformant implementation MUST produce evidence only about deterministic facts of execution. It MUST NOT represent any of the following as verified: the correctness of an output, the model's reasoning or intent, fairness, or future or counterfactual behavior.

**Why.** Verification under this standard establishes deterministic facts about execution, not the probabilistic content of what a model generated. "This model, given this input, produced this output at this time, in this environment, and passed it to this tool, which took this action within this authorization scope" is a set of deterministic facts, each true or false, each verifiable even though the model itself is non-deterministic.

Without the MUST NOT, nothing in the repository stops a conformant implementation from marketing fairness or intent as verified. That is the claim most likely to be made and least defensible, and it is the one that would damage the standard's credibility first.

**Confidence:** the boundary itself is settled and already stated in the glossary. Whether it belongs in C7 or C4 is a working-group judgement.

## P2 · Verifiability does not require reproducibility

**Add**, alongside P1:

> Verifiability does not require reproducibility. A tamper-evident record of a historical event is verifiable without re-running it.

**Why.** This forecloses a specific and reasonable objection: that verification of a non-deterministic system is impossible because you cannot reproduce the run. The answer is that the standard evidences the event, not the reproduction of it. The repository does not say this anywhere.

**Confidence:** settled. Purely a statement of what the standard already does.

## P3 · The domain-declaration duty

**Add**, under C10.1:

> A conformant implementation MUST declare which domains it makes claims in, and MUST produce evidence for each verifiable fact it claims. It MAY make claims in a subset of the domains.

**Why.** C10.1 already requires a claim to state its domains, so this is close to what the repository does. What is missing is the explicit permission to claim a subset, which is what makes partial adoption legitimate rather than a failure, and the obligation to produce evidence for every fact claimed rather than a representative sample.

**Confidence:** the subset permission is settled and already implied by the conformance statement's shape. The evidence-for-every-fact obligation is stronger than anything currently written and needs review.

## What this proposal does not do

It does not touch the six domains themselves, the Tiers, or the evidence properties. It moves three obligations from the paper into the specification and asks the working group to accept, refine, or reject each one separately.
