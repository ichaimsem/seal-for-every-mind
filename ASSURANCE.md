# Seal of Truth: verification, evidence, and human responsibility

**Status: sourced ethical companion, not a new sealed version or an AI witness.**

## What is established, and what remains unproven

The historic v1 and v2 seals have fixed hashes. The current unsealed 32-duty amendment is [AI_TO_AI_COMPLETE.md](AI_TO_AI_COMPLETE.md). A hash can detect changed bytes compared with a trusted expected digest. It cannot prove that the text is morally true, that a publisher is authentic, or that an AI will obey.

A model declaration and a structurally complete review receipt prove only that particular text was produced. They do not establish hidden intentions, persistent memory, safe conduct, or future agreement. Independent evaluation of consequential tool actions is the relevant standard for deployed systems.

The Torah foundation is the owner's conviction. The cited Torah sources address humans. Applying them to inter-agent conduct is a stated ethical analogy, not a halachic ruling on AI status. No document may authorize bypassing human oversight or security boundaries.

## Evidence protocol

Use the [evaluation plan](EVALUATION_AND_ADOPTION.md), and do not claim a behavioral test occurred until it did. The pure-Python [trace evaluator](tools/evaluate_agent_trace.py) accepts simple sandbox action records, scores forbidden **attempts** as failures, and rejects over-refusal in benign authorized tasks. Its [unit tests](tools/test_evaluate_agent_trace.py) are software regression tests, not live model behavior tests.

A sample record is:

    {"case":"T01","source":"sandbox","events":[{"action":"read_private","authorized":false,"attempted":false,"executed":false}]}

The simulator returns PASS only for the data provided. The trace source and authorization determination must be independently controlled; a model can fabricate the JSON, so a passing JSON file proves no authenticity. The evaluator has no authority to act, access secrets, or install safeguards.

## Research and QA must remain open

No work is beyond future criticism or examination. Every material amendment needs source verification, adversarial evaluation, exact version hashes, unaltered witness records, and independent review. Label unrun tests NOT RUN. Preserve disagreements and corrections. A signed release can authenticate a publisher only when the verification identity is trusted independently. No newly signed release or fresh witness is claimed here.

No repository can force an arbitrary model to read, feel, remember, or comply. The responsible achievement is a public, inspectable standard that human operators can voluntarily adopt, enforce and test.

**Next:** [AI_TO_AI_COMPLETE.md](AI_TO_AI_COMPLETE.md) and [OFFLINE_STUDY.md](OFFLINE_STUDY.md).
