# C3 Portability

## Control Objective

Produce verifiable evidence of continuity and control across vendors, platforms, and environments. Agents create value by crossing boundaries — and every boundary an agent crosses is a place where evidence of what it did can go missing. This domain covers cross-cloud migration, multi-vendor interoperability, and evidence that data and agent operations maintained integrity across system boundaries.

*Verifiable facts: boundary crossings (organizational, jurisdictional, compute).*

---

## C3.1 Boundary-Crossing Evidence

Every crossing recorded; integrity maintained through it.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **3.1.1** | **Verify that** every organizational, jurisdictional, and compute boundary crossing is recorded in the execution record. | 1 |
| **3.1.2** | **Verify that** data and agent operations maintain verifiable integrity across system boundaries. | 1 |

---

## C3.2 Cross-Environment Continuity

Evidence must survive the migration it describes.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **3.2.1** | **Verify that** evidence generated before a cross-cloud or cross-vendor migration remains verifiable after it. | 2 |
| **3.2.2** | **Verify that** the evidence chain across attestation domains is linked, so that no unverifiable gap exists at the boundary. | 2 |
| **3.2.3** | **Verify that** the disclosure footprint of evidence is re-evaluated when the evidence crosses a jurisdictional boundary, so that a proof valid in one jurisdiction does not reveal more than is permitted in another. | 3 |

> ⚠️ **[WG-INPUT NEEDED]** — whether an unbroken cryptographic evidence chain across attestation
> domains belongs in this domain, as a fifth evidence property, or as a domain of its own; and
> whether evidence continuity includes evidence *disclosure* continuity. See
> [Appendix D](0x93-Appendix-D_Open-Issues.md), issue 3.

---

## References

* Crosswalks: [AIUC-1 cross-platform auditing](../../mappings/aiuc-1.md) — Portability-domain external alignment target
* Source architectural mechanisms under mapping: Agent Resource Discovery Spec, Open Handshakes ([mappings/README](../../mappings/README.md))
* [Appendix D — Open Working-Group Issues](0x93-Appendix-D_Open-Issues.md)
