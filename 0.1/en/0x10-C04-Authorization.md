# C4 Authorization

## Control Objective

Produce verifiable evidence that the system acted within the permissions it was granted. This domain covers delegation-chain verification, scope and policy enforcement, signed authorization tokens checked against granted permissions, and the traceability of whether each agent action stayed within its authorized boundary — proving not just that the tool was authorized, but that its *evaluated payload parameters* matched the exact structural schema at execution time.

*Verifiable facts: authority granted, decisions within or against it, delegation validity.*

---

## C4.1 Authority and Scope Enforcement

Authority is scoped to the action, not to the actor: permission tied to the specific operation, its configuration, and its limits at the time it acts cannot be replayed against a different action.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **4.1.1** | **Verify that** the authority granted to the agent is recorded as evidence before actions execute. | 1 |
| **4.1.2** | **Verify that** every action is evaluated against the permissions granted, and that the decision (within or against the boundary) is evidenced. | 1 |
| **4.1.3** | **Verify that** out-of-scope actions are rejected at the interception boundary and that the rejection is evidenced. | 1 |
| **4.1.4** | **Verify that** the evaluated payload parameters of each tool invocation matched the exact structural schema authorized at execution time. | 2 |
| **4.1.5** | **Verify that** authority is scoped to the specific operation, its configuration, and its limits at the time of action, not carried as a broad standing identity. | 2 |
| **4.1.6** | **Verify that** human approval and override decisions are evidenced, bound to the approver's identity, and include the raw, true intent that was presented for approval. | 2 |

---

## C4.2 Delegation

Delegation validity is a verifiable fact; escalation through the chain must be provably impossible.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **4.2.1** | **Verify that** signed authorization tokens are checked against granted permissions for each action. | 1 |
| **4.2.2** | **Verify that** the validity of each delegation in the chain is verified and evidenced. | 1 |
| **4.2.3** | **Verify that** a delegated agent cannot accumulate permissions exceeding the delegator's, and that the delegation logic is verified to prevent privilege escalation. | 2 |
| **4.2.4** | **Verify that** a relying party can confirm a delegation is policy-compliant without seeing the full delegation chain, where confidentiality requires it. | 3 |

> ⚠️ **[WG-INPUT NEEDED]** — whether identity-binding is owned by the Identity domain or by
> Authorization with Identity as an input (working-group lean: Authorization owns it, Identity as
> an input). See [Appendix D](0x93-Appendix-D_Open-Issues.md), issue 1.

---

## References

* [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/) — excessive agency, tool misuse
* [SOC 2 Type II](../../mappings/soc-2.md) — Authorization-domain external alignment target (proving runtime execution matched policy)
* Crosswalks: [MAESTRO L3/L6/L7 controls](0x91-Appendix-B_Proof-Mechanism-Inventory.md), [CSA AARM](../../mappings/csa-aarm.md)
* [Appendix D — Open Working-Group Issues](0x93-Appendix-D_Open-Issues.md)
