# Roadmap and Timeline (informative)

*This is a supporting section. It is informative and carries no normative requirements.*

Two roadmaps live here, and they answer different questions for different readers. Part A is the
schedule for the standard itself: read it if you are tracking when this document lands. Part B is
a rollout guide for an organization adopting Proof-of-Control: read it if you are the one
deploying the cryptographic infrastructure.

Part B in particular uses four tiering words that are easy to run together. They mean different
things. This is the whole vocabulary:

| Word | What it grades or tracks | Defined in |
| --- | --- | --- |
| **Tier** | The evidence: how independently verifiable it is (1 to 4) | Verifiability Tiers, [Section 6](0x10-S06-Evidence-and-Grading.md) |
| **Stage** | The assessment: how rigorously conformance was checked (Self-Declared, Third-Party Assessed, Continuously Monitored) | Conformance, [Section 7](0x10-S07-Conformance.md) |
| **Phase** | The rollout: how an organization deploys the infrastructure over time (1 to 3) | This section, Part B |
| **Layer** | The surface: where in the agent stack a control sits (1 to 7) | System surface, [Section 5](0x10-S05-System-Surface.md) (MAESTRO) |

## Part A — For Anyone Tracking the Standard

This standard is developed the way ISO, NIST, IETF, and W3C develop standards: an open working
draft, public comment, working-group deliberation, revision, and implementation experience
feeding the next version. The target is a stable Version 1.0 six months after public comment
opens.

| Milestone | Target |
| --- | --- |
| Working Draft 1.0 opens for public comment | August 1, 2026 |
| Public comment window (60 days) | August 1 – September 30, 2026 |
| Revised draft, all public comment and ⚠️ [WG-INPUT NEEDED] items resolved | November 15, 2026 |
| Working-group ratification and final review | December 2026 – January 2027 |
| **Stable Version 1.0 published** | **February 1, 2027** |

These are targets for a public process, firm enough to signal the pace we intend to move at, and
the working group holds them. Open working-group decisions are marked `⚠️ [WG-INPUT NEEDED]`
throughout the document; a commenter can find every one by searching for that tag, and resolving
them is what the November 15 revised draft depends on. The document moves from the public-comment
file to a public repository over the course of the process.

The Certification and its accredited-assessor body ([Section 7](0x10-S07-Conformance.md)) are a
separate, later track. Standing up an accreditation body runs past the six-month window for the
standard itself, so its dates are set independently and are not part of the Version 1.0 target
above.

> ⚠️ **[WG-INPUT NEEDED]** — the schedule above is the working target, ratified by the working
> group at kickoff. The dates for the separate Certification and assessor-body track are still to
> be set.

## Part B — For Organizations Adopting Proof-of-Control

This rollout guide is contributed by Proof-of-Control co-chair Ken Huang. It sequences the
cryptographic proof mechanisms so that foundational infrastructure is in place before
higher-complexity mechanisms: an organization should not deploy zero-knowledge proofs or secure
multiparty computation before its hardware security module infrastructure and digital-signature
pipelines are operationally stable.

The rollout runs in three Phases over twenty-four months. Each Phase brings the organization to
readiness for one conformance Stage ([Section 7](0x10-S07-Conformance.md)). All of it applies to
Proof-of-Control implementations, Tiers 3 and 4 of the Verifiability Tiers, since the framework
addresses cryptographic verification only.

| Phase | Months | What you build | Brings you to |
| --- | --- | --- | --- |
| **Phase 1: Foundational infrastructure** | 1–6 | The cryptographic primitives every later mechanism depends on: HSM key management and signing, model and data provenance signing, tamper-evident logging, TEE runtime attestation, access-control formal verification, multi-signature change management | **Self-Declared readiness:** the infrastructure exists and the organization can self-declare against the standard |
| **Phase 2: Expanded proof coverage** | 7–12 | Proof coverage across data pipelines, agent-framework controls, and privacy-sensitive domains: provenance chains on all pipelines and RAG, tool-schema and workflow formal verification, ZKP for privacy compliance, TEE for confidential inference, PKI agent identity, third-party vetting attestation | **Third-Party Assessed readiness:** the implementation is mature enough for external assessment |
| **Phase 3: Maturation and ecosystem integration** | 13–24 | Governance integration and cross-organizational interoperability: cross-layer audit-evidence aggregation, delegation-chain verification, continuous compliance and board reporting, cross-organization proof interoperability, MPC evaluation for high-value gates (Research track) | **Continuously Monitored readiness:** conformance is verified on an ongoing basis |

The control-by-control detail for each Phase, with the MAESTRO Layer each control sits on,
follows.

### Phase 1: Foundational Infrastructure (Months 1–6)

Phase 1 establishes the cryptographic primitives on which all subsequent proof mechanisms
depend; every control in later phases either builds on or requires its outputs.

* Deploy hardware-security-module infrastructure for key management and all signing operations
  across the organization.
* Implement model and data provenance signing (Layer 1 and Layer 2 digital-signature controls).
* Deploy Merkle-anchored, cryptographically signed logging infrastructure (Layer 5
  tamper-evident logging).
* Establish TEE-based runtime attestation for model-serving infrastructure (Layer 4 runtime
  attestation).
* Implement access-control formal verification for the highest-risk RBAC/ABAC policies (Layer 6
  access control).
* Deploy multi-signature change management for all Agentic AI system modifications (Layer 6
  change management).

### Phase 2: Expanded Proof Coverage (Months 7–12)

Phase 2 extends proof coverage to data pipelines, agent-framework controls, and
zero-knowledge-proof infrastructure for privacy-sensitive compliance domains.

* Extend Merkle-anchored provenance chains to all data pipelines and RAG retrieval systems
  (Layer 2).
* Implement formal verification for tool schemas and bounded workflow specifications (Layer 3).
* Deploy ZKP infrastructure for privacy-compliance attestation where regulatory requirements
  justify the overhead (Layer 2 and Layer 6).
* Extend TEE attestation to confidential-computing environments for sensitive inference
  workloads (Layer 4).
* Implement PKI-based agent-identity infrastructure with TEE binding (Layer 7).
* Deploy hash-chained third-party vetting attestation with SLSA provenance (Layer 7).

### Phase 3: Maturation and Ecosystem Integration (Months 13–24)

Phase 3 integrates proof mechanisms with governance processes, extends to ecosystem controls,
and establishes cross-organizational verification interoperability.

* Deploy cross-layer compliance-audit evidence aggregation with hash-chained Merkle proof
  (Layer 6).
* Implement multi-signature delegation-chain verification for agent authority transfers
  (Layer 7).
* Integrate proof artifacts with continuous compliance monitoring and board reporting processes.
* Establish cross-organizational proof-verification interoperability with partners and
  regulators.
* Begin evaluation of MPC threshold signing for high-value federated authorization gates
  (Layer 4, Research track).
* Monitor ZKP tooling maturity for AI-specific applications and re-evaluate Research-rated
  controls for promotion.

### Success Metrics

An organization should track the following to assess implementation effectiveness and report to
boards and audit committees:

* **Proof coverage:** percentage of critical Agentic AI controls with active, production proof
  mechanisms (target: 100% of Proven-rated controls by the end of Phase 2).
* **Attestation freshness:** percentage of runtime attestations current within organizational
  thresholds (for example, 24 hours for high-risk systems).
* **Verification latency:** time for an independent verifier to validate a proof artifact for a
  given control (target: under 60 seconds for signature or attestation verification).
* **Audit efficiency:** reduction in manual evidence-collection time for regulatory audits
  through automated proof generation (baseline versus post-Phase 2).
* **Incident-detection improvement:** reduction in time to detect tampered logs or configuration
  drift through cryptographic monitoring (baseline versus post-Phase 1).

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
