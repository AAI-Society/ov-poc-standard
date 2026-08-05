# C6 Security

## Control Objective

Produce verifiable evidence of system integrity and access-control enforcement. This domain covers hardware attestation, runtime integrity verification, confidential compute, on-chip compliance, and evidence that security controls held during execution.

*Verifiable facts: integrity of the execution environment and that controls held; tools invoked.*

---

## C6.1 Execution Environment Integrity

Evidence that the environment the agent ran in is the environment that was authorized, and that the declared controls held while it ran.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **6.1.1** | **Verify that** evidence shows the declared security controls held during execution. | 1 |
| **6.1.2** | **Verify that** every tool invocation is recorded with its arguments in the execution record. | 1 |
| **6.1.3** | **Verify that** runtime integrity of the execution environment is attested (e.g., TEE or remote attestation) and comparable against an authorized reference value. | 2 |
| **6.1.4** | **Verify that** hardware attestation covers the components on which higher-layer controls depend. | 3 |

---

## C6.2 Isolation and Confidential Execution

Proof of process isolation is required whenever agents execute generated code or interact with un-sanitized external tools.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **6.2.1** | **Verify that** process isolation is proven whenever the agent executes generated code or interacts with un-sanitized external tools. | 1 |
| **6.2.2** | **Verify that** sensitive inference workloads run in confidential-compute environments with verifiable attestation. | 2 |
| **6.2.3** | **Verify that** on-chip compliance mechanisms, where claimed, carry independently verifiable attestation. | 3 |

---

## References

* [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/) and OWASP AIVSS — Security-domain alignment targets
* [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — Security-domain external alignment target
* [MITRE ATLAS](https://atlas.mitre.org/)
* Crosswalks: [Confidential Computing](../../mappings/confidential-computing.md), [MAESTRO L4 runtime attestation](0x91-Appendix-B_Proof-Mechanism-Inventory.md), [OWASP](../../mappings/owasp.md), [NIST AI RMF](../../mappings/nist-ai-rmf.md)
