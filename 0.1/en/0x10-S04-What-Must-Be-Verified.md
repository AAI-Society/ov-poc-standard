# Section 4 — What Must Be Verified (normative)

***This section answers:*** *What must be verified? — The six domains of verification, each with
its verifiable facts: Provenance, Privacy, Portability, Authorization, Identity, and Security.*

This section defines what a conformant implementation produces evidence about. It sets the
boundary of what is verifiable, enumerates the six domains of verification with their verifiable
facts, and states the threat model: what Proof-of-Control defends against and what is out of
scope. The six domain definitions here were authored by the working group. Items marked as open
working-group issues are not yet normative.

## The Determinism Boundary

Verification under this standard establishes deterministic facts about execution, not the
probabilistic content of what a model generated. The proposition "this model, given this input,
produced this output at this time, in this environment, and passed it to this tool, which took
this action within this authorization scope" is a set of deterministic facts, each true or false,
and each remains verifiable even though the model itself is non-deterministic.

A conformant implementation MUST produce evidence only about deterministic facts of execution. It
MUST NOT represent the following as verified: the correctness of an output, the model's reasoning
or intent, fairness, or future or counterfactual behavior. Verifiability does not require
reproducibility: a tamper-evident record of a historical event is verifiable without re-running
it.

## Verification, Not Validation

Proof-of-Control performs verification, not validation, and the distinction is deliberate. In
systems-engineering terms (ISO/IEC 42001, IEEE), verification asks whether the system was built
and run right: did it execute within the authorized boundaries. Validation asks whether it was
the right system: whether those boundaries, and the outputs they produced, were the correct
choice. Proof-of-Control delivers the first. It does not deliver the second.

This is worth stating plainly, because the boundary is easy to mistake for validation.
Proof-of-Control shows that an agent stayed inside the control boundaries that were set. It does
not judge whether those boundaries were the right ones, or whether the output was good, fair, or
wise. That judgment, regulatory review, ethical evaluation, human oversight, is validation, and
it stays a human responsibility. Verification and validation are complementary, not sequential:
the standard supplies the evidence, and people still make the decision.

For the same reason, Proof-of-Control does not prevent every harm. It evidences and gates
control-boundary adherence, so an unauthorized action is rejected and every action is
attributable. But an action that stays within the agent's authorized bounds and is still harmful,
for example one induced by a prompt injection that never exceeds the agent's permissions, is a
safety question that cryptographic verification does not rule out. What Proof-of-Control does is
exact: it makes the boundary real and the record of what happened undeniable. It does not make
the model itself trustworthy.

To produce verifiable evidence across the six domains, conformant agent architectures MUST
implement explicit, out-of-band Action Interception Gateways. Verification evidence MUST be
generated at the interception boundary before, during, and after tool invocation, preventing
unverified side effects.

## The Six Domains of Verification

The six domains are the areas the standard produces evidence about. Each domain lists its
verifiable facts, the true-or-false statements an implementation makes evidence for; the working
groups author and extend the facts. A conformant implementation MUST declare which domains it
makes claims in, and MUST produce evidence for each verifiable fact it claims. It MAY make claims
in a subset of the domains.

The controls a domain verifies can include deterministic checks on the agent's actions and
outputs, such as rate limits, invariants, schema, and policy.

### Provenance

*Verifiable facts: Which model ran, and its lineage, artifact and supply-chain origin.*

Verifiable evidence of origin and lineage: where inputs came from, which exact model state
produced an output, what computation substrate executed the work, and how an immutable custody
chain links origin to the action record.

Provenance is distinct from the other five domains. The record of what actions occurred is the
core of Proof-of-Control itself (evidence of what the system did). Identity covers who the actor
was; Authorization covers whether the system acted within the permissions it was granted.
Provenance covers the backward-looking chain: where the inputs came from, whether the training
data was licensed, whether the model is what the vendor claims it is, and whether the computation
was performed on the data it claims to have used. It answers the question: can you show the chain
of custody from origin to output?

Each is a distinct provenance question that does not fit cleanly into the other five domains
alone. Where Privacy requires minimization, conformant provenance uses derived, hash-bound,
selectively disclosable evidence rather than raw payload retention. The domain is especially
critical for systems that change after deployment, where each action must bind to a specific
model state rather than a product label alone. No single domain answers who did what provably on
its own; Identity, Authorization, and Provenance address that question together while the action
record remains the core of Proof-of-Control. In some ways, this is the first thing the standard
should focus on: "What came in?" We end up otherwise with a GIGO situation. The other domains
follow from this: "What happened to/with what came in and how?"

### Privacy

*Verifiable facts: What data was read and written.*

Verifiable evidence that data handling stayed within the defined privacy parameters at execution
that is produced without exposing the data being protected. Covers data consent enforcement,
purpose limitation, data minimization, license and data residency compliance, and integrity of
deidentification. Demonstrate a clear boundary between what is used and what is disclosed.
Privacy is the domain where verification is itself a privacy problem. The evidence must
demonstrate compliance without re-leaking the inputs that the compliance was intended to protect.
Cryptographic mechanisms include zero-knowledge proofs of policy adherence, selective disclosure,
commitment schemes for consent records and mathematically verifiable computation of confidential
inputs. Privacy covers what data is touched, under what constraints and that those constraints
are held. This is distinct from Authorization (is the system permitted to act) and Identity (who
acted).

### Portability

*Verifiable facts: Boundary crossings (organizational, jurisdictional, compute).*

Verifiable evidence of continuity and control across vendors, platforms, and environments. Covers
cross-cloud migration, multi-vendor interoperability, and evidence that data and agent operations
maintained integrity across system boundaries.

### Authorization

*Verifiable facts: Authority granted, decisions within or against it, delegation validity.*

Prove not just that the tool was authorized, but that its *evaluated payload parameters* matched
the exact structural schema at execution time. Verifiable evidence that the system acted within
the permissions it was granted. Covers delegation-chain verification, scope and policy
enforcement, signed authorization tokens checked against granted permissions, and the
traceability of whether each agent action stayed within its authorized boundary.

### Identity

*Verifiable facts: Which agent and which principal ran.*

Verifiable evidence of actors, agents, and delegated authority relationships. Covers agent
identity verification, delegation chain verification, human-to-agent authorization binding, and
evidence that every action traces to a legitimate principal. Utilize Cryptographic
Principal-to-Agent Delegation Tokens (e.g., short-lived OAuth/JWT, W3C DIDs, or cryptographic
capability URLs) to explicitly bind agent tool calls back to human intent.

### Security

*Verifiable facts: Integrity of the execution environment and that controls held; tools
invoked.*

Verifiable evidence of system integrity and access control enforcement. Covers hardware
attestation, runtime integrity verification, confidential compute, on-chip compliance, and
evidence that security controls held during execution. Require proof of process isolation
whenever agents execute generated code or interact with un-sanitized external tools.

## ⚠️ [WG-INPUT NEEDED] Open Working-Group Issues (not yet normative)

Three questions are under active working-group discussion. They are recorded here so the draft
reflects the live debate, and they carry no normative force until resolved. Issue 2 emerged
directly from the working-group contribution reproduced verbatim below; issue 1 is closely
related to it; issue 3 arose separately, from Advait Patel's cross-cloud attestation point.

1. **Identity and Authorization overlap** — whether identity-binding is owned by the Identity
   domain or by Authorization, with Identity as an input. (Working-group lean: Authorization owns
   it, Identity as an input.) The delegation-and-authority binding described in the contribution
   below bears directly on this. **⚠️ [WG-INPUT NEEDED]**
   * *"I recommend we keep Authorization separated using Identity as an input to it. Identity
     provides the authenticated principal. Authorization evaluates the runtime context and action
     boundaries."*
2. **Anonymity and pseudonymity** — whether the standard supports verifiable-but-unlinkable
   identity binding as an implementer-selectable option, and how. Positions range from full
   traceability to a principal, to pseudonymity with identity escrow that can be pierced under
   defined conditions (for example a subpoena). Design intent is that the implementer can select
   the option that fits the use case. This issue emerged directly from the contribution below.
   **⚠️ [WG-INPUT NEEDED]**
   * *"I strongly advocate for verifiable unlinkability so enterprises can deploy agents without
     disclosing customer PII or corporate identities to third-party vendors. The best way to
     secure information is to not hand it out unnecessarily. :-)"*
3. **Portability — evidence continuity across boundaries** — Bob Blessing-Hartley raises whether
   an unbroken cryptographic evidence chain across attestation domains (for example a cross-cloud
   migration, where each side is tamper-evident but no link exists between them) belongs in the
   Portability domain, as a fifth evidence property, or as a domain of its own. (Raised
   separately by Advait Patel.) When evidence crosses a vendor or jurisdictional boundary, the
   disclosure footprint of that evidence changes. A ZK proof valid in one jurisdiction may reveal
   more than is permitted when surfaced in another jurisdiction. Is it worth scoping early
   whether evidence continuity includes evidence disclosure continuity? **⚠️ [WG-INPUT NEEDED]**
   * *"When an agent moves across clouds or vendor boundaries, I believe the evidence chain must
     remain unbroken."*
4. **Working-group contribution, Bob Blessing-Hartley (verbatim, the source of issues 1 and 2
   above):**

   > "As drummond.reed@gmail.com pointed out, pure anonymity makes accountability impossible. If
   > an agent goes rogue or commits fraud, and there is zero cryptographic link back to a
   > principal, the system breaks down. I think we need to separate/clarify these concepts:
   >
   > Privacy (Data Minimization): The agent only reveals the minimum necessary information to
   > complete a task. (e.g., Proving the principal is over 18, without revealing their exact
   > birthdate or name). I hate this example, it is so tired but it is one everyone understands.
   >
   > Pure Anonymity: An agent's actions cannot be linked to the principal, or even to other
   > actions taken by the same agent. Drummond is right, this leads to no control at all.
   >
   > Pseudonymity (Unlinkability): The agent acts under an identifier that is not inherently tied
   > to a real-world human, but can be linked back to the principal under specific,
   > cryptographically enforced conditions.
   >
   > Here are some examples where Unlinkability is of value:
   >
   > Anti-Price Discrimination: A procurement agent negotiating prices for a massive enterprise.
   > If the seller knows the agent belongs to Apple or Google, the price goes up.
   >
   > Whistleblowing / Investigative Agents: Agents deployed to gather data on government or
   > corporate malfeasance or human rights abuses.
   >
   > Healthcare & Research Data: Agents acting on behalf of patients to negotiate data-sharing
   > agreements for clinical trials. The authorization must be legally binding, but the
   > principal's identity must remain completely shielded from the data consumer. I did some work
   > on a system that never (or has not yet!) gone live doing precisely this.
   >
   > Micro-transactions & Web Browsing: Agents paying for paywalled articles or services on
   > behalf of a user. The vendor needs to know the token is valid, but shouldn't be able to
   > build a surveillance profile of the human's reading habits. I am a big fan of, if I had paid
   > for a service, I should not be the product.
   >
   > How this is accomplished should be flexible, not technology bound, per se. As Drummond
   > pointed out, Identity Escrow is a valid one (When I am in the ZK mindspace I call these
   > disclosure packages.) Escrow requires trust of a set of people which means people need to
   > know what they are buying into and who can disclose what, to whom. ZKP directly enables
   > "verifiable but unlinkable identity binding." Using ZKPs, a principal can issue a delegation
   > credential to an agent. When the agent acts, it presents a ZKP to the relying party that
   > mathematically proves: "I have been authorized by a legitimate, verified principal who holds
   > the required credentials." The proof validates the authority without ever revealing the
   > identifier of the principal. Peer decentralized DIDs are also an interesting approach.
   >
   > So… The Verifiable Unlinkability scenario ends up the most technically complex aspect of
   > this because two things need to be proved:
   >
   > Delegated authority from a legitimate principal
   >
   > An agent has to prove that it holds the private keys to execute the action being performed.
   >
   > This is where ZKP becomes the proof of control. Instead of handing over the delegation token
   > from the "principal", the agent runs a cryptographic algorithm locally to generate a ZKP
   > which asserts to the verifier of an action:
   >
   > I, the agent, (feels weird using the pronoun "I") have a valid delegation signature from a
   > trusted issuer/principal.
   >
   > That issuer/principal meets your requirements (for example they are a qualified investor)
   >
   > I, the thing that is communicating with you with the identity DID:xyz mathematically control
   > the specific private key delegated to this capability.
   >
   > Note that there are actually multiple phases to this, I have only touched upon the ZKP
   > piece. On a high level the flow is 1. Delegation to Agent, 2. Handshake with Verifier (maybe
   > using a peer DID), 3. The ZKP stuff above and finally 4. the verifier checks the math and
   > says all good and there is not a drop of traceable footprint for data brokers to consume."
   > **⚠️ [WG-INPUT NEEDED]**

## The Threat Model

The threat model states, for each known agent threat, what Proof-of-Control defends against and
what is explicitly out of scope. It is the same threat set as the
[Section 2](0x10-S02-Why-Verification-Matters.md) landscape, viewed differently: Section 2 lists
what can go wrong; this section states what the standard does about each and where its boundary
sits. The threats are the 27 catalogued in Section 2 (drawn from
[MITRE ATLAS](../../mappings/mitre-atlas.md), NIST AI 100-2, and the
[OWASP LLM and Agentic Top 10s](../../mappings/owasp.md), which converge on the same core
classes), plus two evidence-model threats, evidence repudiation and trust opacity, from the
[MAESTRO](../../mappings/maestro.md) threat-modeling work. Threats marked "not addressed" are the
honest edge of the claim, and they match the determinism boundary above: Proof-of-Control
verifies what an agent did, not whether the output was correct, fair, or wise.

*Coverage key: 🟢 Full · 🔵 Strong · 🟡 Partial · ⚪ Not addressed. Coverage rates how much of the
threat the evidence reaches; the two detail columns say exactly what it reaches and where the
boundary is.*

| Threat | Coverage | What Proof-of-Control defends against | Out of scope |
| --- | --- | --- | --- |
| Prompt injection / goal hijacking | 🟡 Partial | Gates and records the out-of-bounds action the injection attempts; evidence of what the agent did | The injection itself; an in-bounds harmful action is a safety question |
| Poisoned / bent goals | 🔵 Strong | Attests the integrity of the goal specification; evidence the goal that ran is the goal authorized | A subtly wrong objective that never alters the spec |
| System prompt leakage | ⚪ Not addressed | Can record that an output occurred | Whether the model discloses its own instructions |
| Memory & context poisoning | 🔵 Strong | Verifies provenance of memory writes and reads; evidence of lineage; gates unattested sources | A validly sourced but misleading note |
| Vector / embedding / RAG weakness | 🟡 Partial | Provenance of retrieved data; evidence of what informed the decision | The relevance or quality of what was retrieved |
| Training-time data / model poisoning | 🔵 Strong | Verifies which model and weights ran (attested provenance) | The training process itself, which is pre-deployment |
| Poisoned supply chain / tools / MCP | 🔵 Strong | Attests which weights, tools, and artifacts loaded; unattested cannot be admitted | Whether an attested artifact is itself trustworthy upstream |
| Identity & privilege abuse / spoofing | 🔵 Strong | Cryptographic identity; binds every action to a principal; verifiable delegation chain | Credential theft or social engineering at the human layer |
| Context-blind authorization | 🔵 Strong | Verifies the authorization decision and boundary adherence; records that the boundary held | Whether the authorized boundary was correctly defined |
| Excessive agency / over-permission | 🔵 Strong | Evidences what authority was exercised and whether actions stayed in bounds; gates over-scope | Whether the grant was too broad |
| Insecure inter-agent communication | 🔵 Strong | Verifies message authenticity and integrity; binds messages to signed identities; evidences the delegation chain | Latency or performance cost of evidence at boundaries |
| Tool misuse | 🔵 Strong | Evidences every tool call and its arguments; gates disallowed calls | A valid in-scope call that is ill-advised |
| Unexpected code execution | 🟡 Partial | Evidences code-execution calls and gates them by authorization | Malice within permitted execution, which needs sandboxing |
| Unsafe actuation | 🟡 Partial | Gates and records actuation within a signed safety envelope | Whether a within-envelope action is safe, and whether the envelope was set correctly |
| Improper output handling | 🟡 Partial | Evidences the output and where it flowed | Validating and sanitizing the output, which is the consuming system's job |
| Sensitive info / PHI exfiltration | 🔵 Strong | Evidences data access and boundary crossings; gates unauthorized egress | Covert side-channel exfiltration; whether the privacy policy itself is adequate |
| Autonomy creep | 🔵 Strong | Evidences the signed autonomy envelope and every change; gates out-of-envelope actions | Quality degradation within the envelope |
| Rogue agents / behavioral drift | 🟡 Partial | Produces the attributable evidence trail that makes drift detectable and provable after the fact | Detecting the misaligned pattern itself |
| Scope creep / lifecycle | 🔵 Strong | Signed passport and change-control evidence; gates unreviewed changes | Whether the classification is correct |
| Audit tampering | 🟢 Full | Records are tamper-evident, generated by the mechanism at execution, not operator-narrated | Insider compromise at the silicon layer, disclosed via trust assumptions |
| Cascading failures / fail-open | 🟡 Partial | Evidences failure and deny events; at the top tier the system fails closed | Preventing propagation across a multi-agent system, which is architecture |
| Coverage decay / resilience | 🔵 Strong | Continuous self-verification; an ongoing rather than point-in-time record | Discovering new attack classes, which is red-teaming |
| Human-agent trust exploitation / approval fatigue | 🟡 Partial | Evidences the raw, true intent presented for approval and the approval decisions | The human fatigue and social engineering itself |
| Undisclosed AI / consent | 🔵 Strong | Verifiable consent and disclosure record; gates on consent | Whether the disclosure content was adequate |
| Misinformation / hallucination | ⚪ Not addressed | Nothing; correctness is out of scope | Whether the output is correct; correctness is a range, not a point |
| Hidden bias | ⚪ Not addressed | Can preserve a tamper-evident record of verdicts for a separate review | Assessing or correcting fairness, which is validation |
| Unbounded consumption / DoS | 🟡 Partial | Evidences consumption and calls; a budget or rate cap set as a boundary can gate | Availability defense, which is mostly infrastructure |
| Evidence repudiation | 🟢 Full | Cryptographic evidence is independently verifiable and non-repudiable; the operator cannot deny an action occurred | Disputes about the meaning or significance of an action, only whether it occurred |
| Trust opacity | 🔵 Strong | Trust-assumption disclosure makes residual trust visible and comparable | Eliminating all trust assumptions; the standard requires disclosure, not elimination |

Four rows read "not addressed" or record-only — system-prompt leakage, misinformation, hidden
bias, and the semantic half of several others. Naming them is what keeps the standard credible:
Proof-of-Control shows what happened, not whether it was right.

---

*Proof-of-Control is stewarded by the [Advanced AI Society](https://advancedaisociety.org/) —
**[join at advancedaisociety.org](https://advancedaisociety.org/)**.*
