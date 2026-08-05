# C1 Provenance

## Control Objective

Produce verifiable evidence of origin and lineage: where inputs came from, which exact model state produced an output, what computation substrate executed the work, and how an immutable custody chain links origin to the action record. Provenance covers the backward-looking chain — whether the training data was licensed, whether the model is what the vendor claims it is, and whether the computation was performed on the data it claims to have used. It answers the question: can you show the chain of custody from origin to output?

*Verifiable facts: which model ran, and its lineage, artifact and supply-chain origin.*

Provenance is distinct from the other five domains: [Identity](0x10-C05-Identity.md) covers who the actor was, and [Authorization](0x10-C04-Authorization.md) covers whether the system acted within the permissions it was granted; no single domain answers "who did what, provably" on its own. In some ways this is the first thing the standard focuses on — "what came in?" — because the other domains follow from it: "what happened to/with what came in, and how?"

---

## C1.1 Model and Artifact Provenance

Each action must bind to a specific model state rather than a product label alone. This is especially critical for systems that change after deployment.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **1.1.1** | **Verify that** evidence identifies the exact model state (e.g., a cryptographic digest of weights and configuration) that produced each output, rather than a product label alone. | 1 |
| **1.1.2** | **Verify that** the hash of deployed model weights is checked against a signed manifest at load time, and that the check is evidenced. | 1 |
| **1.1.3** | **Verify that** the signature chain over model artifacts validates unbroken from training origin through any fine-tuning steps, with signing keys from authorized providers. | 2 |
| **1.1.4** | **Verify that** unattested models, tools, and artifacts cannot be admitted into the execution stack, and that rejection events are evidenced. | 2 |
| **1.1.5** | **Verify that** model supply-chain provenance is carried in a supply-chain attestation format (e.g., SLSA provenance) covering intermediate build and fine-tuning steps. | 3 |

---

## C1.2 Input and Data Lineage

Where inputs came from, and the custody chain that links origin to the action record.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **1.2.1** | **Verify that** the origin of every input that steers agent behavior is recorded at ingestion. | 1 |
| **1.2.2** | **Verify that** an immutable custody chain links input origin to the action record. | 1 |
| **1.2.3** | **Verify that** each transformation applied to data feeding the agent is recorded in an append-only, hash-linked record with pointers to inputs and outputs. | 2 |
| **1.2.4** | **Verify that** training-data lineage and licensing attestations are available for the model in use. | 3 |

---

## C1.3 Compute Substrate Provenance

What executed the work, evidenced rather than asserted.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **1.3.1** | **Verify that** evidence identifies the computation substrate that executed the work. | 2 |
| **1.3.2** | **Verify that** substrate identification is independently verifiable (e.g., hardware attestation) rather than operator-asserted. | 3 |

---

## C1.4 Privacy-Preserving Provenance

Where [Privacy](0x10-C02-Privacy.md) requires minimization, conformant provenance uses derived rather than raw evidence.

| # | Description | Level |
| :--------: | ------------------------------------------------------------------------------------------------------------------- | :---: |
| **1.4.1** | **Verify that** provenance evidence uses derived, hash-bound, or selectively disclosable forms rather than raw payload retention where data minimization applies. | 1 |
| **1.4.2** | **Verify that** provenance evidence for confidential inputs can be validated without revealing the underlying data. | 2 |

---

## References

* [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/)
* [Sigstore](https://www.sigstore.dev/)
* [C2PA — Coalition for Content Provenance and Authenticity](https://c2pa.org/)
* [MITRE ATLAS](https://atlas.mitre.org/) — training-time poisoning and supply-chain threats
* Crosswalks: [MAESTRO L1/L2 controls](0x91-Appendix-B_Proof-Mechanism-Inventory.md), [OWASP](../../mappings/owasp.md), [MITRE ATLAS](../../mappings/mitre-atlas.md)
