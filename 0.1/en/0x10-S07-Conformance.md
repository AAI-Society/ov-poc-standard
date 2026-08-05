# Section 7 — Conformance (normative)

***This section answers:*** *How thoroughly was the claim checked? — The three conformance
stages: Self-Declared, Third-Party Assessed, and Continuously Monitored.*

Conformance grades how thoroughly a claim of meeting this standard was checked: the rigor of the
assessment, a separate axis from the Verifiability Tiers, which grades the evidence itself. The
binary threshold ([Section 6](0x10-S06-Evidence-and-Grading.md)) decides whether a system is
Proof-of-Control-conformant at all; the conformance stages grade how that conformance was
established, and by whom.

## The Conformance Stages

There are three conformance stages. They are named, never numbered, and a conformance claim MUST
state its stage.

**Self-Declared:** the operator attests, in a standardized conformance statement, that its
system meets the standard.

**Third-Party Assessed:** an accredited assessor examines the system and confirms conformance.

**Continuously Monitored:** conformance is verified on an ongoing basis rather than at a single
point in time.

> ⚠️ **[WG-INPUT NEEDED]** — the operational requirements for the Continuously Monitored stage
> are not yet defined. "On an ongoing basis" has to be made concrete enough to certify against.
> Three questions in particular. (1) Minimum monitoring cadence: how continuous "continuous" must
> be, real-time and event-driven, or a bounded interval such as hourly or daily, and whether it
> varies by domain or by Verifiability Tier. (2) Automated versus human: what must be
> machine-validated as the system runs versus periodically re-assessed by a person. (3) Incident
> response: what is expected when monitoring detects a control failure, a broken trust
> assumption, or a gap in evidence, including notification, remediation, and whether conformance
> is suspended until the issue is resolved.

> A starting point for the working group to react to, not yet normative: a Continuously Monitored
> implementation SHOULD generate evidence for every in-scope action as it occurs rather than by
> sampling; validate that evidence automatically against the claimed Verifiability Tier in
> near-real-time; retain it in a tamper-evident store; alert on any validation failure or
> coverage gap within a bounded window; and undergo periodic third-party re-assessment, for
> example annually, to confirm the monitoring itself is sound. The cadence, the bounded windows,
> and the re-assessment interval are the specific numbers the working group needs to set.

## Trust-Assumption Disclosure

Every conformant implementation MUST disclose, in a standardized format, the trust assumptions
that remain. This operationalizes the Transparent evidence property
([Section 6](0x10-S06-Evidence-and-Grading.md)): it turns a binary yes-or-no into a
risk-differentiable profile, which is what makes conformance claims comparable across
implementations and useful to the insurers and regulators pricing residual risk.

The example below shows three deployments, all conformant at the Third-Party Assessed stage,
with materially different risk profiles. The disclosure is what lets an assessor or an actuary
tell them apart.

| Deployment | Trust assumptions | Residual risk |
| --- | --- | --- |
| Healthcare AI agent on Azure | TEE-based (Intel TDX). Trusts Intel silicon manufacturing and Azure physical security. | Hardware supply-chain risk; single-vendor trust dependency, mitigated by Azure's controls and Intel's attestation. |
| Cross-border payment agent | ZK-STARK proofs with transparent setup. Trusts collision-resistant hash functions only; no hardware dependency. | Narrowest trust base, mathematical assumptions only; higher compute cost, no single-entity dependency. |
| Supply-chain verification agent | Groth16 ZK proofs with a multi-party ceremony. Trusts that at least 1 of 47 ceremony participants was honest, and the BN254 curve. | Ceremony trust distributed; well-studied assumptions; moderate residual risk from ceremony integrity. |

> ⚠️ **[WG-INPUT NEEDED]** — the standardized disclosure format itself is not yet defined. The
> working group must fix a finite set of trust-assumption categories so disclosures are
> comparable across implementations. Bob Blessing-Hartley proposed a two-dimensional matrix of
> privacy-enhancing mechanisms (ZK, FHE, TEE-based confidential compute, MPC) against trust
> category (trusted setup, hardware-vendor attestation, and so on). A draft set of
> trust-assumption categories already exists as a starting point: Hardware, Mathematical,
> Ceremony, Vendor, Implementation, and Distributed. The working group can ratify, refine, or
> replace it.

## The Self-Declared Conformance Statement (draft template)

At the Self-Declared stage the operator publishes a conformance statement. A conformant
statement includes:

1. the system identified;
2. the domains in which claims are made ([Section 4](0x10-S04-What-Must-Be-Verified.md));
3. for each claim, the evidence properties met and the Tier reached
   ([Section 6](0x10-S06-Evidence-and-Grading.md));
4. the mechanisms that produce the evidence; and
5. the trust-assumption disclosure.

The exact template is being drafted with the working group.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
