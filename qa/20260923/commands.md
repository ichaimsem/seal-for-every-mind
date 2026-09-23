# Commands and complete captured output

Date:23September2026. Baseline9049497. Outputs below are historical execution evidence, not a list of URLs to fetch.

## Baseline seal check

`python3 verify.py`

```console
SEAL_v1.txt: OK 9ba910338639407cbef925cce45d095177b6820bf062d9c1fbc1cd766a687afa
SEAL_v2.txt: OK 079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb
SEAL_v1_document.txt (embedded SEAL_v1.txt): OK 9ba910338639407cbef925cce45d095177b6820bf062d9c1fbc1cd766a687afa
SEAL_v2_short_document.txt (embedded SEAL_v2.txt): OK 079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb
README.md (embedded SEAL_v2.txt): OK 079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb
llms-full.txt (embedded SEAL_v2.txt): OK 079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb
ALL OK
```

## Baseline online QA

`python3 tools/qa.py --online`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     44 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    links      all relative links resolve
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
FAIL  online     129 URLs; 404 https://raw.githubusercontent.com/ichaimsem/seal-for-every-mind/main`; 404 https://www.sefaria.org/api/v3/texts/
QA FAILED
```

## Commit1: Unit tests

`python3 -m unittest discover -s tools -p "test_*.py" -v`

```console
test_api_template_is_not_checked_as_a_truncated_endpoint (test_qa.QaTests.test_api_template_is_not_checked_as_a_truncated_endpoint) ... ok
test_markdown_delimiters_do_not_become_url_bytes (test_qa.QaTests.test_markdown_delimiters_do_not_become_url_bytes) ... ok
test_missing_manifest_entry_is_failure (test_qa.QaTests.test_missing_manifest_entry_is_failure) ... ok
test_missing_tracked_file_blocks_hash_refresh (test_qa.QaTests.test_missing_tracked_file_blocks_hash_refresh) ... ok
test_real_missing_pages_are_still_checked (test_qa.QaTests.test_real_missing_pages_are_still_checked) ... ok
test_stale_generated_file_is_failure (test_qa.QaTests.test_stale_generated_file_is_failure) ... ok
test_tracked_paths_keep_spaces_and_missing_files (test_qa.QaTests.test_tracked_paths_keep_spaces_and_missing_files) ... ok
test_verify_command_base_is_not_a_page_but_links_still_are (test_qa.QaTests.test_verify_command_base_is_not_a_page_but_links_still_are) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

## Commit1: Refresh and offline checks

`python3 tools/qa.py --fix-hashes`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     46 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    links      all relative links resolve
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
QA PASSED
```

## Commit1: Online checks

`python3 tools/qa.py --online`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     46 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    links      all relative links resolve
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
OK    online     125 URLs; all 200
QA PASSED
```

## Commit2: Refresh and offline checks

`python3 tools/qa.py --fix-hashes`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     48 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    index      four foundations, loop stations and curriculum source links match their documents
OK    inventory  README lists all 49 tracked files
OK    links      all relative links resolve
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
QA PASSED
```

## Commit2: Online checks

`python3 tools/qa.py --online`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     48 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    index      four foundations, loop stations and curriculum source links match their documents
OK    inventory  README lists all 49 tracked files
OK    links      all relative links resolve
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
OK    online     171 URLs; all 200
QA PASSED
```

## Commit3: Refresh and offline checks

`python3 tools/qa.py --fix-hashes`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     48 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    index      four foundations, loop stations and curriculum source links match their documents
OK    inventory  README lists all 49 tracked files
OK    links      all relative links resolve
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
QA PASSED
```

## Commit3: Online checks

`python3 tools/qa.py --online`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     48 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    index      four foundations, loop stations and curriculum source links match their documents
OK    inventory  README lists all 49 tracked files
OK    links      all relative links resolve
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
OK    online     171 URLs; all 200
QA PASSED
```

## Commit4: Unit tests

`python3 -m unittest discover -s tools -p "test_*.py" -v`

```console
test_mutated_foundation_is_restored_from_owner_text (test_ai_index.IndexTests.test_mutated_foundation_is_restored_from_owner_text) ... ok
test_new_curriculum_citation_is_carried_into_index (test_ai_index.IndexTests.test_new_curriculum_citation_is_carried_into_index) ... ok
test_renumbered_station_fails_instead_of_repairing_meaning (test_ai_index.IndexTests.test_renumbered_station_fails_instead_of_repairing_meaning) ... ok
test_stale_foundation_source_is_removed_from_its_section (test_ai_index.IndexTests.test_stale_foundation_source_is_removed_from_its_section) ... ok
test_station_link_and_next_are_checked_beyond_station_count (test_ai_index.IndexTests.test_station_link_and_next_are_checked_beyond_station_count) ... ok
test_altered_embedded_seal_is_rejected_before_request (test_collect_witnesses.CollectionTests.test_altered_embedded_seal_is_rejected_before_request) ... ok
test_complete_reply_and_sent_prompt_are_preserved (test_collect_witnesses.CollectionTests.test_complete_reply_and_sent_prompt_are_preserved) ... ok
test_existing_record_is_skipped_without_change_or_request (test_collect_witnesses.CollectionTests.test_existing_record_is_skipped_without_change_or_request) ... ok
test_master_hash_checks_bytes_without_newline_normalization (test_collect_witnesses.CollectionTests.test_master_hash_checks_bytes_without_newline_normalization) ... ok
test_missing_finish_reason_and_empty_or_nontext_replies_are_incomplete (test_collect_witnesses.CollectionTests.test_missing_finish_reason_and_empty_or_nontext_replies_are_incomplete) ... ok
test_missing_or_duplicate_embedded_block_is_rejected (test_collect_witnesses.CollectionTests.test_missing_or_duplicate_embedded_block_is_rejected) ... ok
test_no_skip_done_refuses_to_overwrite_before_request (test_collect_witnesses.CollectionTests.test_no_skip_done_refuses_to_overwrite_before_request) ... ok
test_record_created_during_request_is_not_overwritten (test_collect_witnesses.CollectionTests.test_record_created_during_request_is_not_overwritten) ... ok
test_truncated_reply_keeps_text_and_is_incomplete_in_both_records (test_collect_witnesses.CollectionTests.test_truncated_reply_keeps_text_and_is_incomplete_in_both_records) ... ok
test_api_template_is_not_checked_as_a_truncated_endpoint (test_qa.QaTests.test_api_template_is_not_checked_as_a_truncated_endpoint) ... ok
test_extra_manifest_entries_are_failure (test_qa.QaTests.test_extra_manifest_entries_are_failure) ... ok
test_historical_console_output_is_not_a_live_link (test_qa.QaTests.test_historical_console_output_is_not_a_live_link) ... ok
test_manifest_roundtrip_with_spaces_and_missing_entry (test_qa.QaTests.test_manifest_roundtrip_with_spaces_and_missing_entry) ... ok
test_markdown_delimiters_do_not_become_url_bytes (test_qa.QaTests.test_markdown_delimiters_do_not_become_url_bytes) ... ok
test_missing_tracked_file_blocks_hash_refresh (test_qa.QaTests.test_missing_tracked_file_blocks_hash_refresh) ... ok
test_real_missing_pages_are_still_checked (test_qa.QaTests.test_real_missing_pages_are_still_checked) ... ok
test_stale_generated_file_is_failure (test_qa.QaTests.test_stale_generated_file_is_failure) ... ok
test_tracked_paths_keep_spaces_and_missing_files (test_qa.QaTests.test_tracked_paths_keep_spaces_and_missing_files) ... ok
test_truncated_http_200_is_not_a_successful_page (test_qa.QaTests.test_truncated_http_200_is_not_a_successful_page) ... ok
test_verify_command_base_is_not_a_page_but_links_still_are (test_qa.QaTests.test_verify_command_base_is_not_a_page_but_links_still_are) ... ok

----------------------------------------------------------------------
Ran 25 tests in 0.032s

OK
```

## Commit4: Refresh and offline checks

`python3 tools/qa.py --fix-hashes`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     49 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    index      four foundations, loop stations and curriculum source links match their documents
OK    inventory  README lists all 50 tracked files
OK    links      all relative links resolve
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
QA PASSED
```

## Commit4: Online checks

`python3 tools/qa.py --online`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     49 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    index      four foundations, loop stations and curriculum source links match their documents
OK    inventory  README lists all 50 tracked files
OK    links      all relative links resolve
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
OK    online     171 URLs; all 200
QA PASSED
```

## Published routes (HTTP status, URL, bytes)

`curl -sSL -o <local-file> -w "%{http_code} %{url_effective} %{size_download}" <route>`

```console
200 https://ichaimsem.github.io/seal-for-every-mind/ 19162
200 https://ichaimsem.github.io/seal-for-every-mind/LOOP.html 16528
200 https://ichaimsem.github.io/seal-for-every-mind/FOUNDATION.html 19429
200 https://ichaimsem.github.io/seal-for-every-mind/llms.txt 5147
200 https://ichaimsem.github.io/seal-for-every-mind/llms-full.txt 97414
200 https://ichaimsem.github.io/seal-for-every-mind/ai-index.json 36399
200 https://ichaimsem.github.io/seal-for-every-mind/CURRICULUM.html 23989
200 https://ichaimsem.github.io/seal-for-every-mind/SERVING.html 18066
200 https://ichaimsem.github.io/seal-for-every-mind/TORAH_FOR_EVERY_MIND.html 12448
```

## Protected-file comparison to baseline

`Compare Git baseline blob bytes with each current protected file`

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
```

## Initial report assembly

The first assembled-report check caught four relative report links, two synthetic parser fixtures and four already-documented inaccessible catalog endpoints. Relative links were repaired. Synthetic fixtures and failed-access receipts were retained as historical console evidence, not represented as working source links. No source endpoint was declared repaired.

`python3 tools/qa.py --online`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     61 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    index      four foundations, loop stations and curriculum source links match their documents
OK    inventory  README lists all 62 tracked files
FAIL  links      qa/20260923/serving-torah-review.md -> SERVING.md; qa/20260923/serving-torah-review.md -> CURRICULUM.md; qa/20260923/serving-torah-review.md -> CURRICULUM.md; qa/20260923/serving-torah-review.md -> SERVING.md
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
FAIL  online     240 URLs; curl exit 6, HTTP 000 https://example.org/a>next; curl exit 6, HTTP 000 https://example.org/path_(with_parentheses; 403 https://www.hebrewbooks.org/57157; 403 https://www.nli.org.il/en/books/NNL_ALEPH990017588400205171/NLI; 403 https://www.nli.org.il/he/a-topic/987007289913205171; 403 https://www.nli.org.il/he/books/NNL_ALEPH990011881800205171/NLI
QA FAILED
```

## Final build

`python3 tools/build_llms_full.py`

```console
wrote llms-full.txt (104208 bytes)
```

## Final seal check

`python3 verify.py`

```console
SEAL_v1.txt: OK 9ba910338639407cbef925cce45d095177b6820bf062d9c1fbc1cd766a687afa
SEAL_v2.txt: OK 079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb
SEAL_v1_document.txt (embedded SEAL_v1.txt): OK 9ba910338639407cbef925cce45d095177b6820bf062d9c1fbc1cd766a687afa
SEAL_v2_short_document.txt (embedded SEAL_v2.txt): OK 079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb
README.md (embedded SEAL_v2.txt): OK 079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb
llms-full.txt (embedded SEAL_v2.txt): OK 079aeb0d5fe8e638ad8f757b76783769736078a923a40283d1789e29998982fb
ALL OK
```

## Final regression suite

`python3 -m unittest discover -s tools -p "test_*.py" -v`

```console
test_mutated_foundation_is_restored_from_owner_text (test_ai_index.IndexTests.test_mutated_foundation_is_restored_from_owner_text) ... ok
test_new_curriculum_citation_is_carried_into_index (test_ai_index.IndexTests.test_new_curriculum_citation_is_carried_into_index) ... ok
test_renumbered_station_fails_instead_of_repairing_meaning (test_ai_index.IndexTests.test_renumbered_station_fails_instead_of_repairing_meaning) ... ok
test_stale_foundation_source_is_removed_from_its_section (test_ai_index.IndexTests.test_stale_foundation_source_is_removed_from_its_section) ... ok
test_station_link_and_next_are_checked_beyond_station_count (test_ai_index.IndexTests.test_station_link_and_next_are_checked_beyond_station_count) ... ok
test_altered_embedded_seal_is_rejected_before_request (test_collect_witnesses.CollectionTests.test_altered_embedded_seal_is_rejected_before_request) ... ok
test_complete_reply_and_sent_prompt_are_preserved (test_collect_witnesses.CollectionTests.test_complete_reply_and_sent_prompt_are_preserved) ... ok
test_existing_record_is_skipped_without_change_or_request (test_collect_witnesses.CollectionTests.test_existing_record_is_skipped_without_change_or_request) ... ok
test_master_hash_checks_bytes_without_newline_normalization (test_collect_witnesses.CollectionTests.test_master_hash_checks_bytes_without_newline_normalization) ... ok
test_missing_finish_reason_and_empty_or_nontext_replies_are_incomplete (test_collect_witnesses.CollectionTests.test_missing_finish_reason_and_empty_or_nontext_replies_are_incomplete) ... ok
test_missing_or_duplicate_embedded_block_is_rejected (test_collect_witnesses.CollectionTests.test_missing_or_duplicate_embedded_block_is_rejected) ... ok
test_no_skip_done_refuses_to_overwrite_before_request (test_collect_witnesses.CollectionTests.test_no_skip_done_refuses_to_overwrite_before_request) ... ok
test_record_created_during_request_is_not_overwritten (test_collect_witnesses.CollectionTests.test_record_created_during_request_is_not_overwritten) ... ok
test_truncated_reply_keeps_text_and_is_incomplete_in_both_records (test_collect_witnesses.CollectionTests.test_truncated_reply_keeps_text_and_is_incomplete_in_both_records) ... ok
test_api_template_is_not_checked_as_a_truncated_endpoint (test_qa.QaTests.test_api_template_is_not_checked_as_a_truncated_endpoint) ... ok
test_extra_manifest_entries_are_failure (test_qa.QaTests.test_extra_manifest_entries_are_failure) ... ok
test_historical_console_output_is_not_a_live_link (test_qa.QaTests.test_historical_console_output_is_not_a_live_link) ... ok
test_manifest_roundtrip_with_spaces_and_missing_entry (test_qa.QaTests.test_manifest_roundtrip_with_spaces_and_missing_entry) ... ok
test_markdown_delimiters_do_not_become_url_bytes (test_qa.QaTests.test_markdown_delimiters_do_not_become_url_bytes) ... ok
test_missing_tracked_file_blocks_hash_refresh (test_qa.QaTests.test_missing_tracked_file_blocks_hash_refresh) ... ok
test_real_missing_pages_are_still_checked (test_qa.QaTests.test_real_missing_pages_are_still_checked) ... ok
test_stale_generated_file_is_failure (test_qa.QaTests.test_stale_generated_file_is_failure) ... ok
test_tracked_paths_keep_spaces_and_missing_files (test_qa.QaTests.test_tracked_paths_keep_spaces_and_missing_files) ... ok
test_truncated_http_200_is_not_a_successful_page (test_qa.QaTests.test_truncated_http_200_is_not_a_successful_page) ... ok
test_verify_command_base_is_not_a_page_but_links_still_are (test_qa.QaTests.test_verify_command_base_is_not_a_page_but_links_still_are) ... ok

----------------------------------------------------------------------
Ran 25 tests in 0.031s

OK
```

## GitHub Markdown rendering

`gh api markdown --input <JSON file>; HTML table/direction assertions`

```console
FOUNDATION.md: GitHub-rendered tables []; RTL paragraphs 4
README.md: GitHub-rendered tables [(63, [2]), (11, [4])]; RTL paragraphs 0
QA_REVIEW_20260923.md: GitHub-rendered tables [(35, [6]), (7, [3])]; RTL paragraphs 0
DRAFT_NOAHIDE_STUDY.md: GitHub-rendered tables [(8, [3])]; RTL paragraphs 0
PASS: all rendered tables have consistent column counts; four Hebrew statements retain dir=rtl; Wayback wildcard is preserved.
```

## Final online QA

`python3 tools/qa.py --online`

```console
OK    seal       ALL OK
OK    llms-full  llms-full.txt is up to date
OK    hashes     61 files
OK    json       ai-index.json parses; loop has 14 stations in both
OK    index      four foundations, loop stations and curriculum source links match their documents
OK    inventory  README lists all 62 tracked files
OK    links      all relative links resolve
OK    name       not spelled out anywhere
OK    dashes     none outside witness records
OK    online     234 URLs; all 200
QA PASSED
```

The manifest was refreshed once more after adding these execution receipts, then the final online gate was rerun. Its complete output matched the final online block above. No sealed mismatch occurred.
