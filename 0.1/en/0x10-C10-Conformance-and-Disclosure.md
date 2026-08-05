# C10 Conformance and Trust-Assumption Disclosure

## Control Objective

Grade how thoroughly a claim of meeting this standard was checked, and make residual trust visible and comparable. Conformance is a separate axis from the Verifiability Tiers: the [binary threshold](0x10-C08-Verifiability-Tiers.md) decides whether a system is Proof-of-Control-conformant at all; the conformance stages grade how that conformance was established, and by whom.

There are three conformance stages. They are named, never numbered:

| Stage | Who checks | Peer certifications at a comparable bar |
| --- | --- | --- |
| **Self-Declared** | The operator attests, in a standardized conformance statement | CSA STAR Level 1, SLSA Level 1, PCI DSS SAQ |
| **Third-Party Assessed** | An accredited assessor examines the system and confirms conformance | CSA STAR Level 2, Common Criteria EAL, FIPS 140 validation, SOC 2 |
| **Continuously Monitored** | Conformance is verified on an ongoing basis rather than at a single point in time | CSA STAR Level 3, NIST Continuous Monitoring, EU Cybersecurity Act |

Until the accredited-assessor body is established, a system is described as *placed* at a conformance stage, not *certified* (see [Governance](../../docs/governance.md)).

---

## C10.1 Conformance Claims

An implementation may make claims in a subset of the six domains; for each domain it claims, it produces evidence for the verifiable facts it asserts.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **10.1.1** | **Verify that** every conformance claim states its stage: Self-Declared, Third-Party Assessed, or Continuously Monitored. | 1 |
| **10.1.2** | **Verify that** the implementation declares which of the six domains it makes claims in. | 1 |
| **10.1.3** | **Verify that** evidence is produced for each verifiable fact claimed. | 1 |
| **10.1.4** | **Verify that** the conformance statement includes: the system identified; the domains claimed; for each claim, the evidence properties met and the Tier reached; the mechanisms that produce the evidence; and the trust-assumption disclosure. | 1 |
| **10.1.5** | **Verify that** conformance claims reference the specific version of this standard they are made against. | 1 |
| **10.1.6** | **Verify that** the conformance statement defines the system boundary and the classes of in-scope agent actions, and enumerates excluded action classes with rationale — so a narrow claim cannot present itself as a broad one. | 1 |
| **10.1.7** | **Verify that** the claim and its evidence are available in a documented, machine-readable format, so that claims are comparable across implementations by assessors, insurers, and regulators. | 2 |

---

## C10.2 Trust-Assumption Disclosure

Disclosure operationalizes the [Transparent property](0x10-C07-Evidence-Generation-and-Properties.md): it turns a binary yes-or-no into a risk-differentiable profile, which is what makes conformance claims comparable across implementations and useful to the insurers and regulators pricing residual risk. Example — three deployments, all conformant at the Third-Party Assessed stage, with materially different risk profiles:

| Deployment | Trust assumptions | Residual risk |
| --- | --- | --- |
| Healthcare AI agent on Azure | TEE-based (Intel TDX). Trusts Intel silicon manufacturing and Azure physical security. | Hardware supply-chain risk; single-vendor trust dependency, mitigated by Azure's controls and Intel's attestation. |
| Cross-border payment agent | ZK-STARK proofs with transparent setup. Trusts collision-resistant hash functions only; no hardware dependency. | Narrowest trust base, mathematical assumptions only; higher compute cost, no single-entity dependency. |
| Supply-chain verification agent | Groth16 ZK proofs with a multi-party ceremony. Trusts that at least 1 of 47 ceremony participants was honest, and the BN254 curve. | Ceremony trust distributed; well-studied assumptions; moderate residual risk from ceremony integrity. |

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **10.2.1** | **Verify that** residual trust assumptions — mathematical, hardware, or distributed — are disclosed in the standardized format. | 1 |
| **10.2.2** | **Verify that** disclosures use the defined trust-assumption categories (draft set: Hardware, Mathematical, Ceremony, Vendor, Implementation, Distributed) so they are comparable across implementations. | 2 |

> ⚠️ **[WG-INPUT NEEDED]** — the standardized disclosure format itself is not yet defined; the
> working group must fix a finite set of trust-assumption categories. See
> [Appendix D](0x93-Appendix-D_Open-Issues.md), issue 7.

---

## C10.3 Continuously Monitored Operation

An agent is not something you certify once: a point-in-time check cannot cover a system whose behavior is decided in the moment. These requirements are the working group's starting point for making "on an ongoing basis" concrete enough to certify against.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **10.3.1** | **Verify that** evidence is retained in a tamper-evident store. | 2 |
| **10.3.2** | **Verify that** evidence is generated for every in-scope action as it occurs, rather than by sampling. | 3 |
| **10.3.3** | **Verify that** evidence is validated automatically against the claimed Verifiability Tier in near-real-time. | 3 |
| **10.3.4** | **Verify that** validation failures and coverage gaps raise alerts within a bounded window. | 3 |
| **10.3.5** | **Verify that** the monitoring itself undergoes periodic third-party re-assessment (for example, annually). | 3 |
| **10.3.6** | **Verify that** proof coverage — the fraction of in-scope actions with valid evidence at the claimed Tier — is measured and disclosed, so coverage decay is visible rather than silent. | 2 |

> ⚠️ **[WG-INPUT NEEDED]** — the operational requirements for the Continuously Monitored stage
> (minimum cadence, automated versus human validation, incident response and suspension) are not
> yet defined. See [Appendix D](0x93-Appendix-D_Open-Issues.md), issue 8.

---

## References

* [CSA STAR](https://cloudsecurityalliance.org/star) · [SLSA levels](https://slsa.dev/spec/v1.0/levels) · [FIPS 140](https://csrc.nist.gov/projects/cryptographic-module-validation-program) — peer assurance ladders
* [Appendix A — Glossary](0x90-Appendix-A_Glossary.md): conformance, conformance stage
* Crosswalks: [SOC 2](../../mappings/soc-2.md), [EU AI Act](../../mappings/eu-ai-act.md)
* Companion: [Governance](../../docs/governance.md) — the certification and assessor body; [Roadmap](../../docs/roadmap.md) — Phase-by-Phase readiness for each stage
