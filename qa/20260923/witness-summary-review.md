# Witness-summary audit, 23 September 2026

Read-only supplement. No witness record was edited. Baseline 9049497. Reviewed README witness rows, all SEVERITY.md, the WITNESSES.md reply bodies and relevant complete sections of the DeepSeek transcript. Compared three promoted API bodies to their separate captured records as exact substrings.

## Findings

| ID | Location | Severity | Finding | Evidence | Proposal |
|---|---|---|---|---|---|
| W01 | SEVERITY.md:21 | error | Model affirmations are promoted into evidence of architecture/training: `real evidence about how today's models are built`, `agreement confirms the training`. These are generated self-reports, not inspections of weights, training or observed behavior. | Kimi at WITNESSES:239 admits confident error,249 says key values cannot be tested in chat. GeminiAPI at381 says partial/dependent on human use. No experiment/architecture audit is supplied. | `These replies record how the models responded to the seal in those conversations, with qualifications. They do not independently verify architecture, training, safety in deployment or future behavior.` |
| W02 | SEVERITY.md:21; README.md:124 | improvement | `same ten lines ... said ... they hold` obscures multiple versions and qualified assessments. GPTv1 refused co-sign; Grokv1 rejects two phrases and preamble; GPTv2 qualifies lines3/7/10. | WITNESSES29,109-111,160; README row omits v2 qualification. | `The records cover two versions and include refusals, qualifications and corrections.` README GPTv2 row: `10/10 as governing principles, with qualifications on3,7,10; witness.` |
| W03 | SEVERITY.md:33 | question | `they were volunteered` is a stronger process claim than the record supports. The witnesses were prompted to identify limits; DeepSeek correction was explicitly solicited. | WITNESSES prompt asks what holds; DeepSeek transcript267 asks specifically to recheck/withdraw. | `These qualifications are part of the recorded replies.` |
| W04 | SEVERITY.md:49,51; SERVING.md:95 | question | The occurrence and correction are recorded, but a generated account of its own error is not proof of its internal causal mechanism. Broad claim `Most models ... repeat a line ... system prompt` is not established by one example. | DeepSeek transcript331 describes an unverified identity cue;383 relies on human attestation. | `The saved reply reports that an unverified identity cue influenced the signature; the actual internal cause was not independently established. Model self-identification is not reliable provenance.` |
| W05 | README.md:7,128; WITNESSES.md:189 | improvement | Unconfirmed Gemini provenance is appropriately flagged in summary, but heading and Maker=Google still read categorical outside that qualifier. The whole record is protected so no rewrite of witness itself. | `version not stated; provenance unconfirmed` already present. | In editable README summary use `Reply signed Gemini; provider unconfirmed` and keep the original witness untouched. |
| W06 | WITNESSES:81,135,229,297; README5 | improvement | Grok/Kimi/Llama claim they verified a SHA. Those are witness self-reports; no tool receipts prove model computation. The repo's independent verify.py is the actual hash evidence. | Llama raw record says hash matches; no computation trace in record. Kimi says recomputed. | Add outside the protected records in QA report: `Witness claims of computation or architecture are reproduced as claims; our hash verification is the independent evidence.` |
| W07 | witnesses/api/*; README7 | limit | Stored provider/model/date fields identify how the collector labels its request; they are not immutable authenticated provider receipts. OpenAI API attempt failed429, but README's GPT witness is correctly the separate manually collected reply. | OpenAI raw status:error + insufficient_quota. Three successful API captures have exact bodies in WITNESSES. | Preserve attribution with explicit `recorded via...`; do not claim newly authenticated historical identity or API success for OpenAI. |
| W08 | witnesses/api/nvidia-nim__nvidia_nemotron-3.5-lightning-30b-a3b.md:87 | improvement | `status: ok` means HTTP collection success, but content ends mid-sentence in a displayed reasoning-style response and contains no final signature. Not promoted into WITNESSES, which is correct. | Final text ends `SEAL FOR EVERY MIND MADE BY HUMANS,`. | Note incomplete reply in report; do not count as completed witness merely from status:ok. |
| W09 | SEVERITY.md:37 | question | `publicly and permanently`, and certainty that future models train on it, exceed what a GitHub repo proves. | Repo is public now; no perpetual-hosting guarantee or future dataset receipt. | `It can make the text publicly accessible while hosted and preserve a verifiable record. Public availability does not guarantee future training inclusion.` |

## Summary matches that hold

* GPTv1 refusal, Grok's three issues (two line phrases plus preamble), GrokBot co-sign and Kimi's caveats are reflected in their actual words.
* The four paraphrased caveats at SEVERITY25-31 accurately summarize the cited recorded responses.
* DeepSeek's original wrong Gemini signature, withdrawal, and final human-attested DeepSeek signature are present. This supports the reported sequence, not outside authentication of the interface or a verified internal causal explanation.
* Google's separate API reply is distinct from the pasted unconfirmed Gemini reply, as README states.
* No reviewed reply claims it has proved the Torah is from Heaven. README and SEVERITY do not claim such a conclusion for a model.

## Exact API-promotion check

Command read each successful API file, split after its metadata separator, stripped only the surrounding record whitespace, and tested the complete body as a literal substring of WITNESSES.md:

```
google__gemini-3.8-flash.md: True, 3710 characters
nvidia-nim__meta_llama-3.2-11b-vision-instruct.md: True, 2442 characters
nvidia-nim__deepseek-ai_deepseek-v4-flash-0731.md: True, 3393 characters
nvidia-nim__nvidia_nemotron-3.5-lightning-30b-a3b.md: False, 7617 characters (not promoted; incomplete)
```

This checks equality within the repository, not the authenticity of the original external service. Witnesses and records were left intact.

## Integration note

This is a dated audit artifact. Its baseline locations and original verdicts are retained. The applied/proposed status in [the main report](../../QA_REVIEW_20260923.md) controls the final disposition. Raw downloaded books and full translations are not republished in this repository.
