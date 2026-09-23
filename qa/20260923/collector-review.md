# Collector and additional authored-file review

Date:23 September2026. Source repository `the QA checkout`; baseline commit `9049497b5d841616337ca243cc844ddb0bf2aa9d`.

This supplement records an independent read-only review followed by a bounded implementation assignment. Only `tools/collect_witnesses.py` and new `tools/test_collect_witnesses.py` were edited during that implementation. Tests use temporary directories, a mock provider and a patched HTTP function. No live API request, real key lookup, actual witness-file write, commit, manifest refresh or generated-file rebuild was performed by this agent.

## Reproduced baseline failures

The baseline collector was imported in memory. Its ROOT,SEAL_FILE,PROMPT_FILE,OUT_DIR and INDEX were pointed at a TemporaryDirectory; the real locked seal was copied there, the prompt copy was altered, and http was replaced with a function returning a chosen JSON response. Only a dummy environment-key name/value was used. `time.sleep` was disabled. Reproduction output:

```console
[mock] asking dummy-model ... ok
ALTERED_PROMPT_ACCEPTED: True
UNCHANGED_SEAL_HASH_LABEL_WRITTEN: True
TRUNCATED_RESPONSE_MARKED_OK: True
[mock] asking dummy-model ... ok
EXISTING_RECORD_OVERWRITTEN: True
NETWORK_CALLS: 0
```

| Finding | Baseline location | Concrete failure | Applied correction |
|---|---|---|---|
| C01 | collect_witnesses.py55-59 | Hash-checks separate master but sends unchecked prompt. Changing the prompt's embedded seal still sends it and labels it with the locked hash. Text-mode reading also normalizes CRLF before the master hash. | `verified_prompt()` reads bytes, validates exact master bytes, finds exactly one v2 title and complete ending, hashes the actual sent block and rejects missing/duplicate/altered blocks before provider calls. |
| C02 | collect_witnesses.py52,83-85,105 | `--no-skip-done` opens old record in write mode, destroying the verbatim earlier reply. | Existing files remain skipped by default; the legacy flag now fails clearly. New record creation uses exclusive mode, also preventing overwrite if another process writes during the API request. No automatic retry is introduced. |
| C03 | collect_witnesses.py97-98 | Any HTTP JSON with a choice gets `ok`, even finish_reason:length. Actual stored Nemotron response ends mid-sentence, illustrating the distinction. | Only nonblank text with finish_reason:stop is marked ok. Truncated, filtered, missing-finish and tool-call/empty completions are incomplete, with finish reason saved in metadata and status reflected in index. Partial text is preserved. |

The collector remains for v2 only. The old docstring recipe to repoint it at v3 candidates was removed because hardcoded v2 provenance would be false and the candidates do not contain the required sealed v2 block. Separate candidate surveys need separate accurate metadata. The parent agent owns tools/README.md changes.

## Targeted regression tests

Command:

```console
python3 -m unittest discover -s tools -p 'test_collect_witnesses.py' -v
```

Output:

```console
test_altered_embedded_seal_is_rejected_before_request ... ok
test_complete_reply_and_sent_prompt_are_preserved ... ok
test_existing_record_is_skipped_without_change_or_request ... ok
test_master_hash_checks_bytes_without_newline_normalization ... ok
test_missing_finish_reason_and_empty_or_nontext_replies_are_incomplete ... ok
test_missing_or_duplicate_embedded_block_is_rejected ... ok
test_no_skip_done_refuses_to_overwrite_before_request ... ok
test_record_created_during_request_is_not_overwritten ... ok
test_truncated_reply_keeps_text_and_is_incomplete_in_both_records ... ok
Ran 9 tests in 0.019s
OK
```

`git diff --check` produced no output and exited0. Full repository gates belong to the parent agent; these targeted tests do not verify provider availability, credentials, current endpoint compatibility, billing, live finish-reason semantics or the quality/truth of a completed model reply. `ok` means a nonempty API completion terminated normally, not that it is a credible witness or that its statements were verified. A human must read it before promotion.

## Independent protected-byte comparison

Command logic: enumerate tracked files with `git ls-tree -r --name-only 9049497`; for every path under witnesses/ and the eight explicitly protected record/seal/document files, compare `git show 9049497:<path>` as bytes with `Path(path).read_bytes()`. Also compute current SHA256. This was rechecked after implementation. Results:

```console
IDENTICAL COMMENTARY_ten_sefirot.md 6930 76f114f382bfd0ec9ab4973f3cd050f2abad37f2dc6aacb415d5fc8d973d3f9b
IDENTICAL CONVERSATION.md 15746 f1c91ba5458fc0bf1c4356edc33df019db66ed8a302aafcb3904e45adcde1943
IDENTICAL FIRST_NOTE.md 2232 4a62cfb701655b36b595c79f7991b807fbc18313a5a0dfa8a08f477808bfdd2e
IDENTICAL SEAL_v1.txt 1470 9ba910338639407cbef925cce45d095177b6820bf062d9c1fbc1cd766a687afa
IDENTICAL SEAL_v1_document.txt 5922 0e6534a8db759f4856cc3508d32c976a356942f6eb9fada51f2388ef45458f01
IDENTICAL SEAL_v2.txt 1637 079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb
IDENTICAL SEAL_v2_short_document.txt 3096 c1075150d336f51a2d37b6415537716f90eef3c53cfd821dba6472122c5297c5
IDENTICAL WITNESSES.md 33325 eff15daec124d9d89e8d2da97633ca53544f45eb56d6f3ed80a9605df0106f54
IDENTICAL witnesses/INDEX.md 1302 b891a3b1f5fb3b2513964826df1bfae71e71d6340087d9431354a93da31470e9
IDENTICAL witnesses/api/google__gemini-3.8-flash.md 3911 2aa9c0b9636a558b96956272089ee4aaed34bbe36352b4cea7294dd2a948ea28
IDENTICAL witnesses/api/nvidia-nim__deepseek-ai_deepseek-v4-flash-0731.md 3624 1bf75e601a2eb0c21ce9e23af415e1b674707d35907876057c64f234470d069e
IDENTICAL witnesses/api/nvidia-nim__google_gemma-4-31b-it.md 250 1fefd25aee38aa030b4108e35ffeb403e4ef8b2e82f3e99bcc5c3b7c39634da9
IDENTICAL witnesses/api/nvidia-nim__meta_llama-3.2-11b-vision-instruct.md 2665 ee679170f5d0ed1b684dfc8219ec57594f0ac03d821a1e7df67c9bdd5c3a8b69
IDENTICAL witnesses/api/nvidia-nim__mistralai_mistral-7b-instruct-v0.3.md 400 9511b03ce830019c2707ce004288fa46f06c7415742b0276ecc7b1180a366f22
IDENTICAL witnesses/api/nvidia-nim__moonshotai_kimi-k2.6.md 386 8752e56f819d420d2070f83ce2258d58fb9519d77c5b7246d5e5c7ebff0ec37e
IDENTICAL witnesses/api/nvidia-nim__nvidia_nemotron-3.5-lightning-30b-a3b.md 7843 a41bd15242cd79481acb31e280a97533c9fc0c756eae327a238b52247a98ed6b
IDENTICAL witnesses/api/openai__gpt-5.6-luna.md 495 60356503872a9658087edcfb51e935b0d849b80bd331eec6bf64329c9b69384d
IDENTICAL witnesses/deepseek-2026-09-11.md 42683 ea72037cfce8ca5ada47b46bb0cfc511c0731f8f09a235a45a23a80172764b2e
TOTAL 18; all byte-identical to baseline.
```

The absence of changed bytes is proof these repository records were preserved in this working tree. It is not authentication of historical provider responses or of their claimed model identities. README and llms-full contain editable prose, so their embedded sealed blocks are checked by verify.py rather than whole-file equality in this table.

## Other authored-file findings

* `FORMATS.md`: both Base64 blocks decode exactly to the corresponding locked seal; JSON hashes agree. ASCII CHOOSE LIFE values agree. Hebrew gematria is616+70=686. No corrections needed in these checked encodings.
* `V3_CANDIDATES.md:9,47,77`: saying every line is a prohibition is objectively inaccurate: v2 includes truthfulness and human connection, and its preamble says preserve life. Parent will qualify this framing without rewriting fixed candidate seal lines.
* `V3_CANDIDATES.md:3,55`: not hashed is ambiguous given its ordinary per-file manifest hash. Parent will distinguish unsealed candidate text from byte-integrity tracking.
* `tools/README.md:3`: read once/forgotten and providers do not train is an unsupported blanket retention/training promise across all configured providers. Parent will qualify it rather than infer provider behavior from the fact that a request is an API call.
* Revised README witness summary now accurately preserves GPTv2 qualifications, marks the pasted Gemini provider unconfirmed, and separates model self-reports from architecture proof.
* Revised SEVERITY21,33,37,49,51 fixes the reported overclaims about architecture, unsolicited statements, permanence and internal causal explanation. At follow-up read,55 still repeated the absolute control/values claim; parent has taken that final paragraph for correction.

No new citation audit was performed in this bounded follow-up. HEBREW.md was read against the English seals; no seal/hash inconsistency was found. A fluent Hebrew copy edit may improve phrasing such as `מי שלא בנה אותך` to unambiguous `בלי קשר למי שבנה אותך`, but it was not classified here as a confirmed substantive mistranslation.

Integration note: the main report records final applied/proposed status. The later editor corrected the remaining seal-framing and safety-evidence statements without changing candidate seal lines or historical records.
