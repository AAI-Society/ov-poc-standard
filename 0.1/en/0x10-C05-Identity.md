# C5 Identity

## Control Objective

Produce verifiable evidence of actors, agents, and delegated authority relationships. This domain covers agent identity verification, delegation-chain verification, human-to-agent authorization binding, and evidence that every action traces to a legitimate principal.

*Verifiable facts: which agent and which principal ran.*

---

## C5.1 Agent and Principal Binding

Cryptographic principal-to-agent delegation tokens (e.g., short-lived OAuth/JWT, W3C DIDs, or cryptographic capability URLs) explicitly bind agent tool calls back to human intent.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **5.1.1** | **Verify that** every action traces to a legitimate principal. | 1 |
| **5.1.2** | **Verify that** agent identity is cryptographically verified before actions execute. | 1 |
| **5.1.3** | **Verify that** human-to-agent authorization is bound with cryptographic principal-to-agent delegation tokens (e.g., short-lived OAuth/JWT, W3C DIDs, or cryptographic capability URLs) that link agent tool calls to principal intent. | 1 |
| **5.1.4** | **Verify that** agent identity is bound to a verified execution environment, preventing identity reuse on compromised infrastructure. | 3 |

---

## C5.2 Inter-Agent Identity

Forged or unauthenticated agent-to-agent messages are a catalogued threat class; identity must hold across the agent ecosystem.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **5.2.1** | **Verify that** agent-to-agent messages are authenticated and bound to signed identities. | 2 |
| **5.2.2** | **Verify that** the integrity of inter-agent messages is verifiable by the receiving party. | 2 |

> ⚠️ **[WG-INPUT NEEDED]** — anonymity and pseudonymity: whether the standard supports
> verifiable-but-unlinkable identity binding as an implementer-selectable option, and how.
> Positions range from full traceability to a principal, to pseudonymity with identity escrow
> that can be pierced under defined conditions. See
> [Appendix D](0x93-Appendix-D_Open-Issues.md), issues 2 and 4.

---

## References

* [W3C Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/)
* [OAuth 2.0 / JWT](https://oauth.net/2/)
* WIMSE / IETF workload-identity work — Identity-domain source mechanism under mapping ([mappings/README](../../mappings/README.md))
* Crosswalks: [MAESTRO L7 agent identity verification](0x91-Appendix-B_Proof-Mechanism-Inventory.md), [Zero Trust](../../mappings/zero-trust.md)
* [Appendix D — Open Working-Group Issues](0x93-Appendix-D_Open-Issues.md)
