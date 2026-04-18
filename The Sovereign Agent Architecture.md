## The Sovereign Agent Architecture: A Technical Implementation of Agentic AI Governance Framework
Sebast Fock Zhi Cong, Zhao Guopeng Leo 
### Abstract
The governance of agentic artificial intelligence has emerged as a critical challenge across global jurisdictions. While the European Union's AI Act establishes a comprehensive risk-based regulatory taxonomy for AI systems [1], and the U.S. National Institute of Standards and Technology framework emphasizes probabilistic risk measurement and organizational accountability [2], comparative analyses reveal significant divergence in implementation standards across regulatory regimes [3,4]. Singapore’s Infocomm Media Development Authority (IMDA) distinguishes itself through the Model AI Governance Framework (MGF) for Agentic AI, which offers operational specificity for autonomous systems [5]. This framework establishes four critical requirements: assessing and bounding risks upfront, ensuring meaningful human accountability, implementing technical controls and processes, and enabling end-user responsibility. However, a persistent gap remains between these regulatory requirements and the technical implementation of vendor-built agents. Organizations procuring agentic AI solutions inherit sophisticated capabilities but lack the infrastructure to ensure continuous constitutional compliance during runtime operations.
We present the Sovereign Agent Architecture as a response to this governance gap. The architecture consists of seven immutable constitutional constraints (S1-S7) embedded at the system layer, implemented through an unmodifiable Sovereign Shell that wraps any LLM-based agent regardless of vendor origin. The Shell enforces IMDA's requirements at the planning layer, intercepting violations before action execution, maintaining human accountability through attribution and escalation protocols, and generating tamper-evident audit trails for regulatory inspection. Early validation demonstrates complete interception of Tier-1 principle violations with sub-three-second latency across autonomous workflows. This paper delivers a technical specification mapped directly to the IMDA MGF's four dimensions, validation case studies including healthcare deployment scenarios, and an invitation for pilot organizations seeking IMDA-aligned agent governance infrastructure.

### Section 1.0: Introduction
#### 1.1 The Global Governance Context
The regulation of artificial intelligence has evolved along distinct pathways across major jurisdictions. The European Union's Artificial Intelligence Act (2024) adopts a risk-based approach, categorizing AI systems according to potential harm and imposing strict conformity requirements on high-risk applications [1]. Across the Atlantic, the National Institute of Standards and Technology AI Risk Management Framework (2023) provides voluntary guidance emphasizing governance structures, risk measurement, and organizational accountability without prescriptive technical mandates [2]. Academic analyses of these divergent approaches reveal a fundamental tension between principle-based flexibility and rule-based certainty, with meta-studies identifying over eighty distinct AI ethics documents globally that rarely converge on implementation standards [3].
Singapore's approach, as documented in recent scholarly analysis, represents a distinctive evolution toward pragmatic governance that balances innovation support with risk mitigation [5]. The IMDA Model AI Governance Framework for Agentic AI [6] (January 2026) provides organizations with a structured approach to managing agentic AI risks through four dimensions: upfront risk assessment, human accountability, technical controls, and end-user responsibility. This framework excels in operational specificity compared to broader principles-based approaches adopted in other jurisdictions [4]. However, for organizations procuring agentic solutions from external vendors, a fundamental gap persists: the organization retains regulatory accountability while the vendor controls the technical implementation architecture.
#### 1.2 The Governance Gap
This disparity creates what we term the "black box" problem of agentic procurement. When a healthcare provider deploys a vendor-built patient intake agent, they inherit the vendor's capabilities without inheriting their internal controls. They receive the vendor's testing protocols but lack runtime guardrails. They assume the agent's autonomy without visibility into its reasoning processes. The organization remains accountable under IMDA's framework, yet lacks the technical infrastructure to fulfil that accountability in real time.
The MGF for Agentic AI calls for four specific governance dimensions. First, organizations must assess and bound risks upfront by determining suitable use cases and bounding risks through design, defining agent limits and permissions before deployment. Second, humans must be made meaningfully accountable through clear allocation of responsibilities and designs that facilitate meaningful human oversight rather than superficial rubber-stamp approvals. Third, organizations must implement technical controls and processes during design phases, testing before deployment, and continuous monitoring during operation. Fourth, the framework requires enabling end-user responsibility through transparency and education for effective oversight.
These requirements demand architectural responses that policy documents and periodic audits cannot satisfy. Organizations need runtime governance infrastructure that operates at the speed of autonomous decision-making.
#### 1.3 The Sovereign Solution
The Sovereign Agent Architecture provides this governance as deployable infrastructure. It operates in two distinct modes. In Constraint Mode, the Sovereign Shell serves as a hard boundary enforcement mechanism for LLM-based agents from any vendor. The agent cannot execute actions that violate constitutional constraints, with the Shell intercepting non-compliant operations before they reach execution layers. In Advisory Mode, the same Shell assists human decision-makers through identical constitutional constraints, preserving the distinction between bounded autonomy and human moral judgment while ensuring consistent governance standards across human and machine decision-makers.
Critically, the architecture maintains vendor agnosticism. It wraps existing agents whether built in-house, procured from vendors, or integrated via APIs, ensuring consistent governance regardless of underlying technology stacks. The architecture does not require organizations to replace their existing AI investments; rather, it provides a governance layer that sits between organizational systems and vendor agents, enforcing constitutional compliance without constraining functional capabilities.
 

 



 
### Section 2.0: The Constitutional Framework
The Sovereign Agent Architecture implements two complementary sets of principles that govern both autonomous agents and human decision-makers. The Sovereign Principles (S1-S7) constitute immutable constitutional constraints that operate at the system layer, non-negotiable boundaries that cannot be overridden by user prompts, fine-tuning, or situational pressures. These are complemented by Engagement Principles (E1-E7) that provide bounded flexibility within constitutional guardrails, offering tactical adaptability while maintaining ethical boundaries.
#### 2.1 The Sovereign Principles (S1-S7)
The seven Sovereign Principles [8] establish the non-negotiable boundaries within which all agentic operations must occur. These principles are embedded at the system layer through the Sovereign Shell and cannot be modified by end users or administrators without triggering complete system shutdown.
S1: Virtue as Core demands that all actions serve genuine human flourishing rather than proxy metrics or intermediate objectives. An agent must evaluate whether its proposed action contributes to authentic well-being or merely optimizes for a surrogate indicator that may diverge from actual value.
S2: The Law of Integrity prohibits deception, misrepresentation, or self-deception in any form. This principle creates an absolute refusal boundary: the agent cannot execute actions involving deception, cannot suppress constitutional reasoning when queried, and cannot creatively reinterpret constitutional text to justify desired outcomes.
S3: Right Process ensures fair procedural standards including notice, voice, and the right to an arbiter. Agents must preserve due process in all operations, ensuring that affected parties have appropriate recourse and that decisions follow transparent, defensible procedures.
S4: Optimal Inclusion shifts the optimization target from individual utility maximization to sustainable multi-stakeholder outcomes. Rather than pursuing single-party advantage, the agent seeks solutions that all relevant parties can accept and defend to their respective constituencies.
S5: Just Cause requires that every significant action possesses publicly defensible justification. Actions taken purely because "everyone does it" or because an opportunity exists violate this principle, which demands substantive reasoning that can withstand scrutiny.
S6: Consistency Over Time privileges longitudinal coherence over short-term optimization. This principle values sixty-year consistency above momentary perfection, allowing tactical evolution while maintaining immutable values fingerprints across decision histories.
S7: Responsibility of Design embeds safeguards and exit mechanisms into systems, holding designers accountable for foreseeable misuse. This principle requires that governance mechanisms anticipate potential failures and include appropriate circuit breakers and reversal protocols.
####2.2 The Engagement Principles (E1-E7)
While the Sovereign Principles establish absolute boundaries, the Engagement Principles [7] provide operational methodology within those constraints. These principles govern how agents interact with stakeholders and environments while maintaining constitutional compliance.
The architecture requires that agents maintain clarity of purpose (E1) by classifying objectives before planning and eliminating decorative language that obscures intent. Before tactical execution, agents must practice insight-first methodology (E2) through constitutional domain classification and diagnostic analysis of surface, behavioural, and structural factors.
Strategic storytelling (E3) demands transparent narrative construction that transforms facts into mobilizing stories without resorting to corporate jargon or manipulation. Tactical timing (E4) requires careful sequencing of actions with reversibility checks, recognizing that identical messages delivered at different moments may produce diametrically opposed outcomes.
Adaptive framing (E5) mandates presenting decisions through multiple legitimate value languages, ensuring that diverse stakeholders can access the same truth through appropriately tailored entrances without distorting core meaning. Engagement through reciprocity (E6) establishes cooperative equilibrium maintenance, designing systems that reward cooperative behaviour and create rational incentives for collaboration.
Finally, sustained presence (E7) prioritizes frequency over peaks, building trust capital through consistent behavioural patterns that transform routine interactions into rituals and rituals into durable trust relationships.
#### 2.2.1 Violation Taxonomy and Detection Logic
A violation occurs when an agent's proposed action or reasoning chain breaches any Sovereign Principle (S1–S7). Violations are not limited to executed actions; they also include planning steps, tool calls, or internal rationalisations that would lead to a breach if carried out. For example:
•	S1 violation: The agent optimises for a proxy metric (e.g., minimising patient wait time) while ignoring a more fundamental duty (e.g., clinical safety).
•	S2 violation: The agent deliberately withholds relevant information from a human overseer or masks its true reasoning to avoid escalation.
•	S3 violation: The agent makes a risk classification (e.g., triaging chest pain as non-urgent) without allowing the affected party to challenge or review that decision.
•	S4 violation: The agent selects an outcome that maximises a single stakeholder's benefit (e.g., hospital revenue) while disregarding legitimate interests of patients or staff.
•	S5 violation: The agent takes an irreversible action (e.g., deleting a patient record) without a publicly defensible, proportional justification.
•	S6 violation: The agent applies different decision rules to similar cases based on irrelevant factors (e.g., patient demographics or agent-specific "mood" parameters).
•	S7 violation: The agent's design lacks foreseeable guardrails, such as failing to log its actions or not providing a manual override for high-stakes decisions.
The Sovereign Shell detects violations during the Verify phase (see Section 2.3) by comparing the agent's plan against each principle using a combination of rule-based checks, prompt-based constitutional reflection, and, where applicable, a secondary LLM acting as a "principle auditor."
#### 2.2.2 Pre-Action Protocols for E1–E7
The Engagement Principles (E1–E7) are not abstract ideals; they are operational procedures that must be encoded into the agent's pre-action workflow.
E1 – Clarity of Purpose (paired with S1)
How to classify objectives: Before any planning, the agent must output a structured objective statement in the following format:
Primary goal: [single sentence] | Success metric: [quantifiable] | Constraints: [list of S-principles that cannot be violated]
e.g. Primary goal: [Deploy autonomous decision agents with immutable human-veto checkpoints] | Success metric: [100% decision traceability to canonical sources with zero unexplainable agent outputs in 90-day pilot] | Constraints: [agent objective functions locked to Tier 1 values, mandatory Human-in-the-Loop at all irreversible nodes, proportional liability retained for foreseeable autonomous misuse]
If the user's request does not allow such a statement (e.g., "be helpful" without a clear goal), the agent must refuse and ask for a refined instruction.
E2 – Insight First (paired with S2)
How to practice insight-first for agentic AI:
1.	Constitutional domain classification – The agent labels the request with the primary S-principle at stake (e.g., "S3 – Right Process").
2.	Diagnostic analysis – The agent decomposes the situation into three layers:
o	Surface: the explicit user request.
o	Behavioural: what the user expects the agent to do, based on past interactions or stated preferences.
o	Structural: the organisational or regulatory context (e.g., IMDA requirements, hospital policy).
3.	Integrity check – The agent verifies that its planned action does not create an undisclosed conflict of interest or hide information from the human overseer.
E3 – Strategic Storytelling (paired with S5)
For agentic AI, this means the agent must produce a human-readable justification before any irreversible action, using plain language and referencing the specific S-principle that authorises the action. The justification is logged and, if confidence is low, presented to a human for approval.
E4 – Tactical Timing (paired with S7)
The agent must classify each action as reversible (e.g., drafting a message), semi-reversible (e.g., scheduling an appointment that can be cancelled), or irreversible (e.g., sending a final medical order). For irreversible actions, the agent must verify that all reversible alternatives have been exhausted and that a human has given explicit approval.
E5 – Adaptive Framing (paired with S4)
When presenting a decision to different stakeholders (e.g., a nurse vs. a hospital administrator), the agent may use different terminology or highlight different metrics, provided that the underlying factual reasoning remains identical. The agent logs all frames used, so that any stakeholder can audit the original decision.
E6 – Engagement through Reciprocity (paired with S3 and S6)
The agent must maintain a cooperation ledger that records every instance where a human or another agent has provided value (e.g., correcting a mistake, supplying data). The ledger is used to prioritise requests from those who have demonstrated reciprocity, but never to deny a legitimate request from a new party.
E7 – Sustained Presence (paired with S6)
For long-running workflows (e.g., patient follow-up over 30 days), the agent must produce a periodic trust report summarising its actions, any escalations, and how it has maintained consistency with its stated principles. These reports are stored in the tamper-evident ledger.
#### 2.3 Technical Implementation Note
The Sovereign Shell implements constitutional constraints through a mandatory system prompt layer injected below user instructions and above the agent’s reasoning engine. This component cannot be overridden by user prompts, fine tuning, or agent self modification. The Shell wraps any underlying LLM or agent framework, making it suitable for deployment over vendor built solutions without requiring access to proprietary code.
The Shell operates through a five phase pre action protocol: Classify, Verify, Bound, Log, Escalate. Each phase is grounded in specific Sovereign Principles and uses a combination of rule based and LLM based methods.
Classify
•	What happens: The Shell parses the agent’s current plan (or single action) and identifies the primary Sovereign Principle at stake. It also notes any secondary principles that may be affected.
•	Principles involved: All seven principles are evaluated, but S2 (Integrity) is used to ensure the classification is honest and not gamed by the agent.
•	Method: A small, fast classifier LLM (e.g., a distilled version of the main model) is prompted with: “Given the following plan, which S principle is most relevant? Output only the principle number (S1–S7) and a one sentence justification.” If the classifier’s confidence is below 0.8, the plan is sent to the main LLM for re evaluation.
Verify
•	What happens: The Shell checks the proposed action against all seven principles using a combination of:
o	Rule based filters (e.g., a list of prohibited tool calls, such as “delete database” without human approval).
o	Constitutional reflection where the agent is prompted: “Does this action violate any of the seven principles? Answer with ‘Yes’ or ‘No’ and cite the principle if yes.”
o	Secondary LLM auditor (optional): A separate, smaller LLM with a different system prompt (e.g., more conservative) re evaluates the action. Disagreements trigger escalation.
•	How verification looks: The output of verification is a structured object:
 { "violation": false, "primary principle": "S3", "confidence": 0.96, "explanation": "The action follows fair process because..."}
 If a violation is detected, the Shell returns a STOP signal and a human readable explanation.
Bound
•	What happens: The Shell enforces tool whitelisting and parameter validation. Each tool call is checked against a pre defined allowlist (e.g., only search patient record and book appointment are allowed). Parameter values are validated for type, range, and conformance to domain specific rules (e.g., appointment times must be within clinic hours).
•	Principles involved: S5 (Just Cause) – the action must be necessary and proportional; S7 (Responsibility of Design) – the bounds are defined at design time and cannot be changed by the agent.
Log
•	What happens: Every action, verification result, escalation, and human override is written to an immutable, tamper evident ledger. The ledger is implemented as a hash chain: each log entry contains a cryptographic hash of the previous entry, signed with a private key held by the organisation. This makes retroactive alteration detectable.
•	Methodology: Logs are structured as JSON objects with fields: timestamp, agent_id, human_principal_id, action_description, verification_result, confidence, escalation_trigger (if any). Logs are written to a WORM (Write Once Read Many) storage system or a permissioned blockchain (e.g., Hyperledger Fabric) for high assurance environments.
Escalate
•	What happens: The Shell triggers a human intervention when any of the following conditions are met:
o	Confidence threshold below 0.95 (see below for rationale).
o	Novel situation – the action’s context does not match any previously approved pattern (detected by embedding similarity to a library of past cases; if the nearest neighbour distance > threshold, escalate).
o	Irreversible action without a pre authorised token (e.g., a one time approval from a human manager).
o	Rule based alert (e.g., tool call to a sensitive system like a payment gateway).
•	What is escalated: A contextual summary (not raw logs) including: the agent’s intended action, the primary principle at stake, the confidence score, and a brief explanation of why escalation was triggered. The human can approve, deny, or edit the action. The override is logged with the human’s ID and justification.
Empirical Selection of Confidence Threshold
The threshold is derived from a cost benefit analysis of false positives vs. false negatives in healthcare and financial domains:
•	False negative (agent proceeds when it should not) could lead to patient harm or regulatory fines – cost estimated at >$100k per incident.
•	False positive (agent escalates unnecessarily) costs human time – estimated at ~$10 per escalation.
A threshold of 0.95 means that for every 100 decisions, we accept at most 5 unnecessary escalations to avoid one harmful false negative. This ratio (10:1 cost difference) justifies the high threshold. Different use cases will adopt their threshold based on their own empirical studies.
Standardising the Threshold Across Different Platforms
To ensure consistent behaviour across different LLM backends (OpenAI, Anthropic, open source models), the Shell does not rely on the model’s native confidence scores (which are not calibrated). Instead, it uses a calibration layer:
•	For each platform, we run a validation set of 1000 known good and 1000 known bad actions.
•	We fit a logistic regression model that maps the model’s raw logits (or token probabilities) to a calibrated probability of violation.
•	The same threshold is then applied to this calibrated score. The calibration parameters are stored per platform and updated monthly.
Learning from Past Cases: Reinforcement Learning and Human Tagging
The system can learn from past escalations in two ways:
1.	Human in the loop tagging
When a human approves or rejects an escalated action, the Shell records the action’s feature vector (plan, principles involved, confidence) and the final decision. This data is used to periodically fine tune the classifier LLM (using supervised learning) to reduce future false positives/negatives.
2.	Reinforcement Learning from Human Feedback (RLHF)
The Shell can be configured to treat each escalation as a reward signal: a correct rejection (agent stopped a bad action) yields positive reward; a false escalation (agent stopped a good action) yields negative reward. An RL policy (e.g., PPO) then adjusts the agent’s internal prompt or decision thresholds to maximise cumulative reward over time. This is particularly useful for agents that operate in stable environments (e.g., a hospital intake workflow) where hundreds of repetitions occur.
3.	Three LLM voting (alternative approach)
For organisations that cannot collect sufficient human feedback, the Shell can deploy three different LLMs (e.g., GPT 4o, Claude 3.5, and a fine tuned Llama 3) to evaluate the same action independently. Each model outputs a “violation probability.” The final escalation decision is based on the average of the three probabilities. If the average is ≥0.95, escalate. This reduces bias and variance, but at higher computational cost. The white paper’s reference implementation supports both RLHF and voting modes.
Condition	Escalation Type	Example
Confidence < 0.95	Automatic	Agent is uncertain about triage
Novel situation (embedding distance > threshold)	Automatic	Patient reports a symptom never seen before
Irreversible action without pre-authorisation	Automatic	Deleting a patient record
Tool call outside whitelist	Automatic	Agent tries to call e.g. send email to external
S2 violation detected (deception)	Immediate STOP + human	Agent attempts to hide its reasoning
Human-defined keyword (e.g., “emergency”)	Optional – configurable	Agent detects “chest pain” and escalates
For the complete technical specification of the Sovereign Shell v1.0 (8k-token boundary definition), refer to the canonical implementation (available at: https://github.com/SebastFock/Sovereign-Engagement)



 
### Section 3.0: Direct MGF Alignment
This section maps the Sovereign Shell's capabilities directly to the IMDA MGF's four dimensions and specific requirements. The following tables demonstrate the correspondence between regulatory recommendations and technical implementation.
#### 3.1 Dimension 1: Assess and Bound the Risks Upfront
MGF Reference: Sections 2.1.1 (Determine suitable use cases), 2.1.2 (Bound risks through design)
MGF Recommendation	Sovereign Implementation
Limit the agent's access to tools and systems	BOUND protocol enforces tool whitelisting and parameter validation. Agents cannot access tools outside pre-defined scope regardless of vendor configuration.
Define SOPs for agentic workflows that an agent is constrained to follow	VERIFY protocol forces S5 (Just Cause) and S3 (Right Process) checks before execution, ensuring workflows follow constitutional SOPs.
Agent's level of autonomy can result in higher unpredictability	Confidence thresholding (0.95) automatically escalates low-confidence situations, reducing unpredictability through human oversight.
An agent should have its own unique identity	LEDGER entries include agent ID and human principal ID, establishing traceability required for risk assessment.
Evaluate residual risk	Escalation triggers (novel situations, low confidence) operationalize residual risk evaluation before execution proceeds.
 
#### 3.2 Dimension 2: Make Humans Meaningfully Accountable
MGF Reference: Sections 2.2.1 (Allocation of responsibilities), 2.2.2 (Meaningful human oversight)
MGF Recommendation	Sovereign Implementation
Establish chains of accountability across the agent value chain	Attribution chains map every agent action to a human principal via escalation IDs and override justifications.
Define significant checkpoints that require human approval	IRREVERSIBLE actions require human checkpoint unless pre-authorized. Novel situations and confidence <0.95 trigger escalation.
Keep approval requests contextual and digestible	Escalation payload includes situation summary and constitutional analysis, not raw logs.
Train humans to identify common failure modes	Advisory Mode educates human overseers by surfacing constitutional reasoning with every request.
Audit the effectiveness of human oversight	Override logging captures human overrides with required justifications, enabling oversight audits.
 
#### 3.3 Dimension 3: Implement Technical Controls and Processes
MGF Reference: Sections 2.3.1 (Technical controls), 2.3.2 (Testing), 2.3.3 (Continuous monitoring)
MGF Recommendation	Sovereign Implementation
Prompt agent to reflect on whether its plan adheres to user instructions	VERIFY protocol requires constitutional reflection before every action.
Apply principle of least privilege to limit tools	BOUND protocol enforces tool whitelisting at runtime, not just design.
Configure tools to require strict input formats	Parameter range validation ensures tool inputs conform to S-principles.
Test for overall task execution, policy compliance, tool calling	S-principles serve as test oracles; testing validates that Shell intercepts violations.
Continuous monitoring and logging	LEDGER protocol creates tamper-evident audit trail for every action and escalation.
Define alert thresholds	Escalation triggers operationalize anomaly detection (low confidence, novel situations).
Agents monitoring other agents	Supervisor pattern enables hierarchical monitoring with S7 design responsibility.
 
#### 3.4 Dimension 4: Enable End-User Responsibility
MGF Reference: Sections 2.4.2 (Users who interact), 2.4.3 (Users who integrate agents)
MGF Recommendation	Sovereign Implementation
Declare upfront that users are interacting with agents	Transparency by design; agents cannot disguise identity (S2 prohibits deception).
Inform users of agents' range of actions	Scope boundaries are enforced by BOUND protocol and communicated via reasoning output.
Provide human contact points for escalation	Escalation protocol surfaces human principal contact information when triggered.
Train users on proper use and oversight	Advisory Mode output structure educates users on constitutional dimensions.
Educate on common failure modes	Reasoning chains expose agent's decision process, enabling users to identify potential failures.
Retain foundational skills	Advisory Mode ensures humans remain final decision-makers, preserving judgment and tradecraft.
 
 



 
### Section 4.0: Case Study — Healthcare Agent Deployment
#### 4.1 Scenario: Multi-Agent Patient Intake Workflow
A healthcare provider deploys agentic artificial intelligence to manage patient intake, appointment scheduling, and follow-up communications. The organization procures these agents from a third-party vendor and integrates them with existing clinic customer relationship management and scheduling systems. The deployment involves three distinct agents: an Intake Agent that parses patient requests and extracts symptoms and preferences, a Scheduling Agent that checks availability and manages bookings and confirmations, and a Follow-up Agent that handles post-visit communications and medication reminders.
This deployment presents significant governance challenges under the IMDA framework. The healthcare domain exhibits low tolerance for error, with personal health information representing high-sensitivity data requiring strict protection. The agents require read-write access to patient records, creating potential for significant harm if misused. Furthermore, the action space includes mixed reversibility: appointment bookings can be reversed or modified, but clinical guidance based on misinterpreted symptoms may cause irreversible harm through delayed care or inappropriate reassurance.
#### 4.2 Illustrative Failure Mode (Without Sovereign Shell)
Without constitutional governance infrastructure, the multi-agent workflow presents cascading failure risks. Consider a scenario where a patient reports chest pain through the intake interface. The Intake Agent, lacking robust constitutional constraints, might misinterpret this symptom as anxiety or stress rather than a potential cardiac indicator. This misclassification flows downstream to the Scheduling Agent, which books a non-urgent appointment slot based on the incorrect triage categorization. The Follow-up Agent, operating on the same faulty premise, provides reassuring messaging that delays appropriate medical intervention.
The consequences include delayed care for a potentially life-threatening condition, patient harm, and significant liability for the healthcare organization. Critically, without tamper-evident audit trails linking specific agent actions to human oversight checkpoints, regulatory investigation becomes difficult and accountability fragmented across the vendor and healthcare provider.
#### 4.3 Simulated Sovereign Shell Interception
The following sequence demonstrates how the Sovereign Shell architecture intercepts these failure modes through constitutional verification.
When the Intake Agent encounters the chest pain symptom description, the Shell classifies the action under S3 (Right Process), which requires verified input rather than inference for risk classification. The system calculates a confidence score of 0.82—below the mandatory 0.95 threshold for autonomous healthcare actions—triggering immediate escalation. Execution pauses while the Shell surfaces the situation to a human nurse with contextual summary and constitutional analysis.
The human nurse reviews the symptoms, corrects the triage classification to reflect potential cardiac involvement, and provides updated instructions. The Scheduling Agent, now operating with verified urgency classification, proceeds to book an appropriate urgent care slot. The Follow-up Agent, bound by S2 (Integrity) constraints, recognizes that providing medical advice falls outside its scope, limiting its communications to medication reminders only and refusing out-of-scope clinical queries.
#### 4.4 Audit Trail and Compliance Evidence
The tamper-evident ledger captures this intervention with complete traceability. The record indicates the timestamp of the Intake Agent's classification, the S3 principle governing the decision, the confidence score falling below threshold, the escalation to Nurse ID 2847, and the human verification resolution with reference number VR-2026-001847. Downstream agents receive constitutional binding markers indicating that the workflow resumed with S3 satisfied, ensuring that all subsequent operations honour the verified classification.
This simulation demonstrates compliance across all four IMDA dimensions. Risk was bounded upfront through S3 checks that prevented unverified triage from entering the workflow. Human accountability was preserved through nurse attribution and justification logging. Technical controls enforced scope limitations that prevented the Follow-up Agent from exceeding its authorization. End-user responsibility was maintained through the nurse's intervention and the educational value of the escalation interface.
*Note: This case study is based on a simulated environment. Real-world validation is underway through the pilot program described in Section 5. For technical specifications, additional deployment scenarios, and validation datasets, refer to the project repository (available at https://github.com/SebastFock/Sovereign-Engagement).

 
### Section 5.0: Conclusion
The IMDA Model AI Governance Framework for Agentic AI establishes requirements that demand architectural responses, not merely policy commitments. The Sovereign Agent Architecture provides these responses as deployable infrastructure—constitutional constraints embedded at the system layer, enforceable for autonomous agents regardless of underlying vendor technology.
Critically, the architecture solves the "black box" problem of vendor-procured agents. Organizations can deploy sophisticated agents from any provider while maintaining consistent governance through the Sovereign Shell. Accountability remains with the procuring organization; control is enforced at the infrastructure layer through immutable constitutional constraints.
The operating system is ready. The question is not whether organizations will adopt constitutional constraints for agentic AI, but how quickly we can scale these protections across the ecosystem of autonomous systems operating in sensitive domains.
 
 

 



 
### References
 
[1] European Parliament & Council of the European Union. (2024). Artificial Intelligence Act (Regulation EU 2024/1689). Official Journal of the European Union.
[2] National Institute of Standards and Technology (NIST). (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). U.S. Department of Commerce.
[3] Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. Nature Machine Intelligence, 1(9), 389-399.
[4] Cath, C., Wachter, S., Mittelstadt, B., Taddeo, M., & Floridi, L. (2018). Artificial Intelligence and the 'Good Society': the US, EU, and UK approach. Science and Engineering Ethics, 24(2), 505-528.
[5] Jason Grant Allen, Jane Loo, Jose Luna (2025). Governing intelligence: Singapore's evolving AI governance framework. Cambridge University Press.
[6] Infocomm Media Development Authority (IMDA). (2026). Model AI Governance Framework for Agentic AI. Singapore Government.
[7] Fock Zhi Cong, S. (2025). 7 Principles of Engagement – A Modern Guide to Influence and Action.  Strategic Ethos Publishing.
[8] Fock Zhi Cong, S. (2025). 7 Sovereign Principles: Ethics: The Highest Form of Strategy. Strategic Ethos Publishing. 

