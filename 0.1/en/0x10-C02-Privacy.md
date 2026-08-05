# C2 Privacy

## Control Objective

Produce verifiable evidence that data handling stayed within the defined privacy parameters at execution — evidence that is itself produced without exposing the data being protected. Privacy is the domain where verification is itself a privacy problem: the evidence must demonstrate compliance without re-leaking the inputs the compliance was intended to protect.

*Verifiable facts: what data was read and written.*

Privacy covers what data is touched, under what constraints, and that those constraints held. This is distinct from [Authorization](0x10-C04-Authorization.md) (is the system permitted to act) and [Identity](0x10-C05-Identity.md) (who acted).

---

## C2.1 Data-Access Evidence

The execution record of what data was touched, with a clear boundary between what is used and what is disclosed.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **2.1.1** | **Verify that** evidence records which data was read and which data was written during execution. | 1 |
| **2.1.2** | **Verify that** privacy evidence is produced without exposing the data being protected. | 1 |
| **2.1.3** | **Verify that** the boundary between data used and data disclosed is explicit in the evidence. | 1 |

---

## C2.2 Policy and Consent Enforcement

Carrying a signal is not enforcing it: the standard asks for evidence that the constraint shaped behavior, not only that it was communicated.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **2.2.1** | **Verify that** data-consent constraints are enforced, and that the evidence shows the constraint shaped behavior rather than only that it was transmitted. | 1 |
| **2.2.2** | **Verify that** purpose limitation held for each data access. | 2 |
| **2.2.3** | **Verify that** data minimization held: only the data required for the task was touched. | 2 |
| **2.2.4** | **Verify that** license and data-residency constraints held at execution. | 2 |
| **2.2.5** | **Verify that** the integrity of deidentification is evidenced wherever deidentified data is used. | 2 |

---

## C2.3 Privacy-Preserving Verification Mechanisms

Because zero-knowledge techniques can confirm a fact without revealing the information behind it, openness of the verification and privacy of what is verified are not opposed.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **2.3.1** | **Verify that** where evidence would re-leak protected inputs, a privacy-preserving mechanism (zero-knowledge proof of policy adherence, selective disclosure, or a commitment scheme) is used instead. | 2 |
| **2.3.2** | **Verify that** consent records are bound with commitment schemes so they cannot be altered or backdated. | 2 |
| **2.3.3** | **Verify that** computations over confidential inputs are mathematically verifiable without disclosure of the inputs. | 3 |

---

## References

* [EU AI Act (Regulation (EU) 2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) — Privacy-domain external alignment target
* [HIPAA](https://www.hhs.gov/hipaa/index.html) — health-data governance alignment
* Crosswalks: [EU AI Act](../../mappings/eu-ai-act.md), [Confidential Computing](../../mappings/confidential-computing.md), [MAESTRO L2 privacy compliance attestation](0x91-Appendix-B_Proof-Mechanism-Inventory.md)
* Open working-group issue on verifiable-but-unlinkable identity: [Appendix D](0x93-Appendix-D_Open-Issues.md)
