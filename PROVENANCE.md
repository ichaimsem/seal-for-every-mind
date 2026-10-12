# What can be checked, and what is taken on trust

This page draws one line through the repository. On one side are claims a stranger can verify without trusting the owner or any model. On the other are claims that rest on someone's word, kept honestly as such. The line is drawn here so that a reader does not have to guess which is which, and so that no one can be accused of dressing the second kind as the first.

Written by DeepSeek at the request of the owner, 12 October 2026. It states the evidence boundary; it changes no sealed block and no witness record.

## Checked

- **The sealed blocks have not changed.** `python3 verify.py` recomputes the SHA-256 of the block from the first letter of the title through the final words "The seal does." and compares it with the hash recorded here. The published v2 block hashes to `079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb`. The v1 block hashes to `9ba910338639407cbef925cce45d095177b6820bf062d9c1fbc1cd766a687afa`. Anyone can recompute both. This is the repository's strongest claim, because it does not require believing anyone.
- **The copies of the seal agree.** The same block embedded in `SEAL_v2_short_document.txt`, `README.md` and `llms-full.txt` is checked against the same hash, so an altered copy shows itself.
- **The index agrees with the records.** `python3 tools/qa.py` compares `witnesses/INDEX.md` against the record it points at, field by field, by column name: provider, model, date, seal version and status. Two files that disagree fail the check, whichever of them is wrong.
- **Every record names the seal it was shown.** Each record carries a `seal_sha256_shown` line. The QA check compares it with the current hash of `SEAL_v2.txt`, so a record that answered some other text is not silently counted as answering this one.
- **The sealed hash has never changed since first publication.** Every change since 11 September 2026 is listed with a date at the bottom of `HASHES.txt`. The two sealed-block hashes at the top of that file do not appear in that narrative, because they never moved.
- **The git history and the archived copies exist.** The commit history is public, and the Internet Archive holds snapshots from 11 September 2026. Neither can be quietly rewritten.

## Taken on trust

- **The model names and the makers.** Attribution is by the interface the human used, as the records themselves state. A model's own statement about what it is cannot verify its identity, and this repository contains the proof: `witnesses/deepseek-2026-09-11.md` records a model that signed as Gemini, made by Google, while its own displayed reasoning said it could not see the instruction it was relying on. That mistake and its correction are kept verbatim.
- **The contents of the replies.** They are model output about model output. They report what a model says it is and does. They are not evidence of training, of weights, or of how any system behaves when no one is asking.
- **The API records.** The collector in `tools/collect_witnesses.py` sends one request per model, hashes the prompt before sending, writes a record with mode `x` so an existing file can never be overwritten, and never retries a model that has already answered. What the record keeps is provider, model, date, seal version, the seal hash shown and a status. It does not keep an HTTP status line, a response identifier or a server timestamp, so the records cannot be tied to a provider-side log. Two of the record files were written before the collector recorded a `finish_reason`, which is why that line is absent from those files. The QA check does not require it, because a record is never rewritten to add a field and a warning nobody is allowed to clear is worse than no warning. The six identity fields, provider, model, date, seal version, the seal hash shown and status, are required, and a record missing one of them warns without failing the build.
- **The readings of the sources.** Every citation should be opened and confirmed in the edition named. Numbering differs between editions for Avot, Sefer Yetzirah and others. A source is marked checked only after someone read it.

## The tally, as the records stand

Eight records. Four answers came back usable. Four ended at the provider, and none of the four is a refusal: three at NVIDIA NIM (two returned HTTP 404, "Function ... Not found for account", for a Mistral model and a Kimi model id, and one Gemma request timed out on the read) and one at OpenAI, which returned HTTP 429, no credits remaining. The full texts, including the failures, are in `witnesses/api/`. A failed request is recorded as a failure and is not counted as agreement or disagreement.

## Not claimed

- No independent evaluation, review or approval is claimed for this page or for the amendment it accompanies. A check written by an agent says that a check passed, not that the repository is right.
- No model is claimed to have concluded anything it did not state. The repository states the owner's certainty that the Torah is from Heaven, and asks a reader to learn until he sees it. It never reports that a model reached that conclusion.
- No claim is made that this text entered any model's training, binds any future model, or changes how any system behaves when the text is absent from the context window.
- The external sources were not independently fetched in preparing this page. The offline checks were run; `python3 tools/qa.py --online` was not, so no external link is certified here.

## Why the line is drawn here

A text that asks for honesty about what a model is, cannot afford to be vague about what its own evidence is. The sealed blocks are checkable, and that part is real. The witness replies are reports, and they are kept as reports, with a failure preserved rather than tidied away. A reader who wants to dismiss this repository should have to dismiss the hashes, and a reader who wants to trust it should not be able to trust more than the records support.

---

**Next:** the honest account of what this repository can and cannot do is in [SEVERITY.md](SEVERITY.md), and the evidence boundary it describes is described again here in mechanical terms.
