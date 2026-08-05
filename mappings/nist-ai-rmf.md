# Crosswalk: NIST AI RMF (and NIST AI 100-2)

**Framework type:** AI risk-management / governance framework (NIST)
**Relationship:** Complementary — Proof-of-Control produces the evidence that makes
risk-framework requirements checkable rather than merely asserted. See
[Section 8](../0.1/en/0x10-S08-Mapping-to-Existing-Standards.md).

## The Relationship

NIST AI RMF governs how organizations identify, measure, and manage AI risk. Governance
frameworks tell an organization *what to manage*; they do not, by themselves, produce
independent evidence of what an agent did that holds when the operator is the threat.
Proof-of-Control is the evidence layer that sits alongside the RMF and feeds it: the
independently verifiable, tamper-evident record that lets an RMF-aligned control be *checked*,
by a party that need not trust the operator.

In the by-domain mapping, NIST AI RMF is an **external alignment target for the Security
domain**.

**NIST AI 100-2** (Adversarial Machine Learning taxonomy) is, separately, one of the three
threat catalogs from which the Proof-of-Control threat model is drawn
([Section 4](../0.1/en/0x10-S04-What-Must-Be-Verified.md)), alongside
[MITRE ATLAS](mitre-atlas.md) and the [OWASP Top 10s](owasp.md).

## Peer Assurance Ladder

NIST Continuous Monitoring sits at a comparable bar to the Proof-of-Control **Continuously
Monitored** conformance stage ([Section 7](../0.1/en/0x10-S07-Conformance.md)):

| Proof-of-Control Stage | NIST peer |
| --- | --- |
| Continuously Monitored | NIST Continuous Monitoring |

## Design Alignment

The standard's Interoperable design principle names NIST AI RMF explicitly: Proof-of-Control
points to and complements it rather than duplicating it — no repeat work; it produces the
evidence that makes its requirements checkable
([Section 1](../0.1/en/0x10-S01-Introduction.md)).

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
