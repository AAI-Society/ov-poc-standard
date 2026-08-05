# Section 6 — The Evidence and Its Grading (normative)

***This section answers:*** *How independently can it be verified? And is the evidence any good?
— Two independent axes. The Verifiability Tiers grade how independently evidence can be
verified, from the operator's word to self-enforcing execution. The evidence properties make it
sound: contemporaneous, tamper-evident, and transparent. The binary threshold draws the
yes-or-no line between them.*

> **✍️ [DRAFT] — actively in progress.** This section is being worked on with the working group.

This section grades evidence along two independent axes. The first is the Verifiability Tiers,
which grade how independently a piece of evidence can be verified, from an operator's word up to
self-enforcing execution. The second is the evidence properties, the qualities that make a piece
of evidence sound. The two are separate: a high tier does not excuse weak properties, and strong
properties do not by themselves make evidence independently verifiable. Below, the Tiers come
first, then the properties, then the binary threshold.

## The Verifiability Tiers

Verifiability is expressed as a four-level scale (1 to 4), not a spectrum and not a maturity
model. Higher tiers require less trust in any party, and the tier is set by how much you must
trust, not by whether cryptography is used.

|  | **Assertion — Tier 1** | **Attestation — Tier 2** | **Independently verifiable — Tier 3** | **Self-enforcing — Tier 4** |
| --- | --- | --- | --- | --- |
| **Proof-of-Control?** | No | No | **Yes** | **Yes** |
| **Who you must trust** | The operator | A third party, or the root-keeper | The cryptographic mechanism (e.g., mathematical or distributed assumptions) | The network protocol or continuous mathematical constraints |
| **How it is verified** | Not verified; asserted | An auditor checks, with privileged access | Anyone can verify, no privileged access | Execution is mechanically gated by cryptographic proofs; verification is continuous and automated |
| **What makes it this tier** | Their word | A third party vouches | The trusted party is removed | Enforcement is built in; it cannot run if integrity breaks |
| **Cryptography** | None | Can be cryptographic but centralized | Requires decentralized or trust-minimized cryptographic architectures | Execution layer is bound by the cryptographic proof (e.g., verifiable computation) |

*The Proof-of-Control line falls between Tier 2 and Tier 3 of this table. Tiers 1–2 are
authenticated documentation (you still trust a party) and are not Proof-of-Control; Tiers 3–4 are
independently verifiable cryptographic evidence and are Proof-of-Control. See
[the binary threshold](#the-binary-threshold) below.*

All systems at Tier 3 and 4 must explicitly document their residual mathematical, hardware, or
distributed trust assumptions **in the standardized disclosure format.**

**Chain Integrity** — If a use case requires Tier 4, every system in the interaction chain MUST
attest up to Tier 4 for the interactions they share. A component MAY operate at a lower tier
internally, as long as it preserves the integrity of the Tier-4 interactions: a proprietary model
or a piece of silicon can sit at Tier 1 or 2 on its own, and only its interactions with other
systems need to meet Proof-of-Control. It is only how the systems talk to each other that needs
to fall under Proof-of-Control.

**Cryptography is a mechanism, not a tier.** A centralized Merkle tree is cryptographic but sits
at Tier 2; you still trust whoever controls the root. Cryptography counts toward Tiers 3 and 4
only when there is no central party to trust. What separates Tiers 3 and 4 from Tier 2 is the
removal of the trusted party, not the use of cryptography. All systems at Tier 3 and 4 must
explicitly document their residual mathematical, hardware, or distributed trust assumptions to
satisfy the Transparent property.

**Cryptography is not automatically Tier 4.** Two things knock cryptography down from Tier 4:
you still have to trust a party, which drops it to Tier 2; or you can only verify it after the
fact rather than it enforcing itself, which is Tier 3.

*Cryptographic, but you still trust a party (Tier 2):*

* An operator publishing a hash of its own data. It proves the data matches that hash, but they
  chose what to hash and could swap it.
* A system signing its own logs or outputs with its own key. You trust the key-holder not to lie
  or backdate. The random-number generator signing its own API responses is this.
* Traditional PKI: a certificate signed by a certificate authority. Trust is rooted in the CA.
* A permissioned or consortium blockchain. Cryptographic and ledger-based, but the validators are
  controlled.
* A zero-knowledge proof with a trusted setup run by one party. Whoever ran the setup could
  forge.
* A Trusted Execution Environment attestation whose root of trust is the chip vendor's
  attestation service.
* A centralized or private Merkle tree. Cryptographic, but you trust whoever controls the root.

*Cryptographic and independently verifiable, but not self-enforcing (Tier 3, not Tier 4):*

* A public, append-only transparency log with independent monitors. Anyone can audit, but it
  detects tampering after the fact; it does not stop the system.
* A public blockchain commitment anyone can verify. Independently verifiable, but point-in-time,
  and it does not gate operation.
* A zero-knowledge proof with a trustless setup, produced on demand. Anyone can verify it, but if
  the system can run without producing it, verification is not enforced.

*Tier 4 is where verification is continuous and built into operation:* the system produces
trustless evidence as it runs and cannot operate unless its integrity holds.

## The Evidence Properties

To count under this standard, a piece of evidence must satisfy four properties. They describe
what the evidence must do, not how it must be built, and they are technology-neutral. The
standard's design principles, including technology-neutrality, are set out in
[Section 1](0x10-S01-Introduction.md); this section states only what an implementation must
produce.

**Binary:** a system has the Proof-of-Control property or it does not. It has it when its
evidence reaches Tier 3 or Tier 4 of the Verifiability Tiers: generated by the mechanism at
execution time and checkable by parties other than the operator. This is the binary threshold,
drawn in full below.

**Contemporaneous:** cryptographic evidence generated at the moment of execution, not
reconstructed or narrated after the fact.

**Tamper-evident:** the cryptographic evidence is tamper-evident: any alteration, fabrication,
or backdating is detectable. The evidence is produced by the cryptographic mechanism, not by the
system operator.

**Transparent:** every conformant implementation discloses its residual trust assumptions in a
standardized format. Enterprises, insurers, and regulators can see exactly what must still be
trusted.

> ⚠️ **[WG-INPUT NEEDED]** — a possible fifth evidence property, continuity across boundaries.
> Credited to Advait Patel, who wants it added.
> Advait Patel: "The four properties are clean but I think one is missing in practice. Evidence
> continuity across boundaries."

## The Binary Threshold

The first question the standard answers is: does this system have Proof-of-Control or not? That
yes-or-no is the Binary evidence property, drawn on the Verifiability Tiers above, and it falls
at one place: the boundary between Tier 2 and Tier 3.

Below the line, at Tiers 1 and 2, the evidence is authenticated documentation. You still have to
trust a party: the operator's word at Tier 1, or a signer or root-keeper at Tier 2. A signed
operator log is Tier 2. This is not Proof-of-Control. Above the line, at Tiers 3 and 4, the
evidence is independently verifiable, produced by the mechanism itself and checkable without
trusting the operator. This is Proof-of-Control. The binary threshold is that Tier-2-to-Tier-3
crossover: below it, documentation; above it, evidence. So a system has Proof-of-Control when,
and only when, its evidence reaches Tier 3 or Tier 4.

**What that requires:** evidence you can verify without having to trust any single party.
Trusting the operator is the obvious way to fail this, but not the only one; trusting any
designated party fails it too. A certificate you can only believe by trusting a certificate
authority, or an attestation rooted in a chip vendor's service, can be checked by people other
than the operator and still sits at Tier 2, because a party is still being trusted. Tier 3 begins
where no single party has to be trusted: the evidence is produced by the mechanism, and its
integrity rests on mathematical or distributed assumptions rather than on anyone's honesty.
Cryptography is how that is reached, but cryptography alone is not the test; a signed operator
log is cryptographic and still sits at Tier 2. Below the line sit compliance frameworks, audit
processes, contractual assurances, traditional security controls, and any cryptographic record
whose integrity still depends on trusting a party — all valuable, none of them Proof-of-Control.
Above the line, the evidence stands on the mechanism, not on trust in any party.

**Why binary matters:** the category does not exist until buyers can ask a yes-or-no question.
"Does your AI have Proof-of-Control?" is procurable; "how far along the trust-minimization
spectrum is your AI?" is not. Every successful standard that created a category used a binary
threshold: FIPS validated or not, Common Criteria certified or not, PCI compliant or not, CSA
STAR listed or not.

**The critical definitional line:** The line is the same Tier-2-to-Tier-3 crossover, drawn in
detail. The standard must separate two things that both use cryptography but are fundamentally
different:

| Authenticated documentation (Tiers 1–2, not Proof-of-Control) | Cryptographic evidence (Tiers 3–4, Proof-of-Control) |
| --- | --- |
| The system operator produces logs or records, then signs them with a cryptographic key. The signature proves the log hasn't been altered after creation. It does not prove the log accurately reflects what happened. Trust required: the operator produced the log honestly. | The cryptographic mechanism generates evidence as a byproduct of execution itself. A ZK proof, a TEE attestation report, a consensus timestamp, a verifiable computation proof. The evidence is produced by the mechanism, not narrated by the operator. Trust required: the cryptographic mechanism is sound. |

This critical line definition must be defined with precision; it is where the standard will face
its toughest technical scrutiny. A corollary: mechanism selection must match the control's
evidentiary requirement. A claimed control's evidence MUST actually enforce the domain it is
offered for; a control cannot satisfy a domain it does not enforce: an encryption control does
not satisfy the Identity domain. A mechanism that shows the integrity of an artifact at signing
time reveals nothing about its behavior at runtime; a TEE attestation of the execution
environment is silent on the model weights loaded into it. Conformance must judge
mechanism-to-requirement fit, not just mechanism presence. This is the rule that prevents
conformance gaming.

One concrete case the standard must address: AI-powered validation tools that analyze, score,
and verify code or data quality before deployment. These tools produce detailed evidence of what
was validated, verifiable by third parties.

> ⚠️ **[WG-INPUT NEEDED]** — the binary threshold is the standard's most consequential definition
> and its most-scrutinized point, and the working group must review and ratify it with dedicated
> cryptography and blockchain review. There are many impossibility results pertaining to
> controlling or verifying agentic behavior that can be derived through computational complexity
> theory, and certain verifications are going to be extremely expensive. Thus, careful care must
> be taken to ensure that a binary definition is efficiently achievable. Two questions in
> particular. (1) Is the defining test for the Tier-2-to-Tier-3 line, *no single trusted party*
> (not the operator, and not a third-party root of trust such as a certificate authority, a chip
> vendor, or a trusted setup), as stated above, the correct one, or is a more precise formulation
> needed? (2) Does the authenticated-documentation vs. mechanism-generated-evidence distinction
> hold under adversarial scrutiny across the mechanism families (zero-knowledge proofs, TEE
> attestation, transparency logs, verifiable computation, consensus systems)?

Additional research on the topic of the Proof-of-Control binary threshold, from a cryptographic
and complexity-theoretic perspective, is being done by a group of researchers with an academic
background. This work is currently being coordinated and led by Hart Montgomery, CTO of the
Linux Foundation Decentralized Trust. The goals are twofold: first, prove impossibility results
around proof of control so that it is known (or formalized) what is achievable and what is not,
and second, develop some basic formal definitions and frameworks so that systems can be built and
classified rigorously.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
