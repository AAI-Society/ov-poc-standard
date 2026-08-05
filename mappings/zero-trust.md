# Crosswalk: Zero Trust (NIST SP 800-207; Anthropic Zero Trust for AI Agents)

**Framework type:** Security architecture (NIST SP 800-207) and vendor-published deployment
framework (Anthropic, May 2026)
**Relationship:** Complementary, not competing — Zero Trust enforces control at runtime;
Proof-of-Control shows, independently, that control held afterward. See
[Section 8](../docs/standards-landscape.md).

## The Relationship

Zero Trust tells you how to set the controls on an AI agent correctly so a breach is contained.
Proof-of-Control gives an outside party evidence that those controls were honored.

Adopting Zero Trust does not give you Proof-of-Control. Anthropic's Zero Trust for AI Agents
tells you how to set the controls on an agent so a breach is contained; it does not produce
independent, portable evidence that those controls were honored. Anthropic's own incident
write-ups describe data leaving through a permitted path, where the preventive controls had
nothing anomalous to catch. Enforcing control at runtime and showing, independently, that
control held afterward are different jobs, and the second is the gap the evidence layer closes.

## Side-by-Side

|  | Anthropic Zero Trust for AI Agents | Proof-of-Control |
| --- | --- | --- |
| What is it? | A vendor-published security framework for deploying agents (May 2026) | A standard and technical foundation for independently verifiable evidence of what AI systems did |
| What it answers | "Did we set the controls correctly?" | "Can an outside party verify the controls were honored?" |
| When it acts | Mostly at provisioning and identity time; preventive. Its top tier adds continuous authorization | At and after execution; evidentiary. The evidence outlives the event |
| Scope | Agent deployments | System-wide, not model-only |
| Certifiable? | No; explicitly guidance, not assurance | Yes; the standard, plus forthcoming independent certification |

For a CISO: Zero Trust is native to your budget and your architecture. Proof-of-Control is the
evidence substrate that lets you show an auditor, insurer, or regulator that your agents did only
what they were authorized to do ([Section 1](../docs/introduction.md)).

## Status

> **⚠️ [WG-INPUT NEEDED] — volunteer needed to develop out the crosswalk** (including zero-trust
> architecture per NIST SP 800-207).
> [Sign up at advancedaisociety.org](https://advancedaisociety.org/) to contribute.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
