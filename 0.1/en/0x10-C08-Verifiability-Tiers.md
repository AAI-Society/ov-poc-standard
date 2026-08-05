# C8 Verifiability Tiers and the Binary Threshold

## Control Objective

Grade every piece of evidence by how independently it can be verified — that is, how much you must trust to believe it — and draw the yes-or-no line that makes the category procurable. Verifiability is a four-tier scale, not a spectrum and not a maturity model. A system has Proof-of-Control when, and only when, its evidence reaches Tier 3 or Tier 4.

> **[DRAFT] — actively in progress.** This chapter is being worked on with the working group.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../../images/diagrams/tier-ladder-dark.svg">
    <img alt="The four Verifiability Tiers with the binary threshold between Tier 2 and Tier 3: below it authenticated documentation, above it mechanism-generated evidence" src="../../images/diagrams/tier-ladder-light.svg" width="720">
  </picture>
</p>

## The Four Tiers

| **Assertion — Tier 1** | **Attestation — Tier 2** | **Independently verifiable — Tier 3** | **Self-enforcing — Tier 4** |
| --- | --- | --- | --- | --- |
| **Proof-of-Control?** | No | No | **Yes** | **Yes** |
| **Who you must trust** | The operator | A third party, or the root-keeper | The cryptographic mechanism (mathematical or distributed assumptions) | The network protocol or continuous mathematical constraints |
| **How it is verified** | Not verified; asserted | An auditor checks, with privileged access | Anyone can verify, no privileged access | Execution is mechanically gated by cryptographic proofs; verification is continuous and automated |
| **What makes it this tier** | Their word | A third party vouches | The trusted party is removed | Enforcement is built in; it cannot run if integrity breaks |
| **Cryptography** | None | Can be cryptographic but centralized | Requires decentralized or trust-minimized cryptographic architectures | Execution layer is bound by the cryptographic proof (e.g., verifiable computation) |

The binary threshold falls between Tier 2 and Tier 3: below it, authenticated documentation (you still trust a party); above it, evidence produced by the mechanism itself. Below the line sit compliance frameworks, audit processes, contractual assurances, traditional security controls, and any cryptographic record whose integrity still depends on trusting a party — all valuable, none of them Proof-of-Control.

| Authenticated documentation (Tiers 1–2, not Proof-of-Control) | Cryptographic evidence (Tiers 3–4, Proof-of-Control) |
| --- | --- |
| The system operator produces logs or records, then signs them. The signature proves the log hasn't been altered after creation; it does not prove the log accurately reflects what happened. Trust required: the operator produced the log honestly. | The cryptographic mechanism generates evidence as a byproduct of execution itself — a ZK proof, a TEE attestation report, a consensus timestamp, a verifiable computation proof. Trust required: the cryptographic mechanism is sound. |

---

## C8.1 Tier Placement

The tier is set by how much you must trust, not by whether cryptography is used. Examples of cryptography that still sits at Tier 2: an operator publishing a hash of its own data; a system signing its own logs; traditional PKI rooted in a CA; a permissioned blockchain; a ZK proof with a single-party trusted setup; a TEE attestation rooted in the chip vendor's service; a centralized Merkle tree.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **8.1.1** | **Verify that** the claim register records an assigned Tier (1–4) for every claim, with no unassigned entries. | 1 |
| **8.1.2** | **Verify that** each claim's register entry includes a written trust analysis naming every party that must be trusted for the evidence to hold (operator, signer, CA, chip vendor, ceremony participants), and that the assigned Tier is consistent with that list — any single trusted party caps the claim at Tier 2. | 1 |
| **8.1.3** | **Verify that** claims whose trust analysis names a single trusted party — operator-signed logs, single-party trusted setups, vendor-rooted attestations, centralized Merkle trees, permissioned ledgers — are registered at Tier 2 or below. | 1 |
| **8.1.4** | **Verify that** the words "Proof-of-Control" appear in the conformance statement and marketing claims only for claims registered at Tier 3 or 4, confirmed by the documented claims review. | 1 |
| **8.1.5** | **Verify that** for each Tier 3+ claim, an external party can obtain the evidence and complete verification using only published materials — demonstrated by a recorded verification run performed without operator credentials. | 3 |
| **8.1.6** | **Verify that** claims whose evidence is checkable only after the fact — transparency logs with independent monitors, on-demand proofs the system can run without producing — are registered at Tier 3, and Tier 4 is registered only where verification gates operation. | 1 |
| **8.1.7** | **Verify that** claims resting on a vendor-rooted attestation service are either registered at Tier 2, or composed with independent anchoring (e.g., attestation reports committed to a public transparency log with independent monitors) before being registered at Tier 3 — with the vendor trust assumption on the disclosure in both cases. | 3 |
| **8.1.8** | **Verify that** the verification procedure and tooling for each Tier 3+ claim are published (public repository or equivalent), versioned, and usable without an NDA, license negotiation, or operator-issued credentials. | 3 |

**Auditor evidence:** 8.1.1–8.1.3 — the claim register; recompute the tier for three sampled claims from their trust analyses. 8.1.4 — claims-review sign-off vs. current public claim text. 8.1.5 — the recorded independent verification run; repeat it yourself. 8.1.6 — register entries for after-the-fact mechanisms. 8.1.7 — anchoring configuration and a validated anchor proof. 8.1.8 — locate, install, and run the published verifier as an outsider.

---

## C8.2 Mechanism-to-Requirement Fit

The rule that prevents conformance gaming: conformance judges mechanism-to-requirement fit, not just mechanism presence.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **8.2.1** | **Verify that** the claim register maps each claimed control to its mechanism and to the specific verifiable fact it evidences, using the mechanism's "what it proves" scope from [Appendix B](0x91-Appendix-B_Proof-Mechanism-Inventory.md) — and that no mapping pairs a mechanism with a domain outside that scope (e.g., an encryption control offered for the Identity domain). | 1 |
| **8.2.2** | **Verify that** the mapping distinguishes signing-time claims from runtime claims: no artifact-integrity mechanism (signature at rest) is mapped to a runtime-behavior fact, and no environment attestation is mapped to a claim about the model weights loaded into it. | 1 |

**Auditor evidence:** 8.2.1 — the control→mechanism→fact mapping; check three rows against Appendix B scopes. 8.2.2 — search the mapping for signing-time mechanisms attached to runtime facts.

---

## C8.3 Chain Integrity and Self-Enforcement (Tier 4)

Tier 4 is where verification is continuous and built into operation: the system produces trustless evidence as it runs and cannot operate unless its integrity holds. A component may operate at a lower tier internally — a proprietary model or a piece of silicon can sit at Tier 1 or 2 on its own — as long as its *interactions* with other systems meet Proof-of-Control.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **8.3.1** | **Verify that** where a use case is designated Tier 4, an interaction inventory lists every system in the chain, and each listed system's shared interactions carry Tier 4 evidence — confirmed per interaction, not per system. | 4 |
| **8.3.2** | **Verify that** components operating internally below Tier 4 interact with the chain only through interfaces that produce Tier 4 evidence, per the interaction inventory. | 4 |
| **8.3.3** | **Verify that** operation is mechanically gated on proof validity: in test, invalidating the proof chain (or withholding a required proof) halts the system's in-scope actions. | 4 |
| **8.3.4** | **Verify that** the claim documents the availability impact of proof-gated operation — expected halt conditions, recovery procedure, and maximum tolerable outage — and that the recovery procedure has been exercised. | 4 |

**Auditor evidence:** 8.3.1–8.3.2 — the interaction inventory; sample two interactions and validate their evidence tier. 8.3.3 — the halt test record; re-run it. 8.3.4 — the availability analysis and the recovery-exercise report.

> **[WG-INPUT NEEDED]** — the binary threshold is the standard's most consequential definition
> and its most-scrutinized point; the working group must ratify it with dedicated cryptography
> and blockchain review, including impossibility results being formalized by researchers
> coordinated by Hart Montgomery (CTO, Linux Foundation Decentralized Trust). See
> [Appendix D](0x93-Appendix-D_Open-Issues.md), issue 6.

---

## References

* [Appendix A — Glossary](0x90-Appendix-A_Glossary.md): Verifiability Tiers, Tier, binary threshold terms
* [Appendix B — Proof-Mechanism Inventory](0x91-Appendix-B_Proof-Mechanism-Inventory.md): the mechanisms that produce Tier 3–4 evidence
* [Certificate Transparency](https://certificate.transparency.dev/) — the public transparency-log pattern
* Crosswalks: [Confidential Computing](../../mappings/confidential-computing.md) (Tier-2 caveat for vendor-rooted attestation), [SOC 2](../../mappings/soc-2.md)
