# Independent technical QA and witness-summary review

Read-only review on 23 September 2026 of commit `389ca6b9ee4ba862ec127538c20424e7e99616d6` and the live follow-up working tree in `the QA checkout`. AGENTS.md was read in full before work. The reviewer made no repository edits or commits. Other agents were editing during this review, so early failures and their subsequent repairs are distinguished below.

## Result

The revised implementation fixes the four material defects found during this review: filenames containing spaces in the hash manifest, accepting failed HTTP transfers with a 200 status, greedy multiline heading parsing, and stale per-foundation source mappings. The conflicting-duplicate manifest weakness was also repaired and regression-tested. The final bounded read-only pass at `ce659bb1691c48c8473dc4975a4f66b4e615213c` passed all 16 tests, all six sealed/embedded checks, and index synchronization. Live parsing produced fourteen stations and five curriculum levels; synchronization was idempotent. Limited URL-parser cases remain documented below; they do not occur among the current repository links inspected.

The GitHub workflow retains sealed verification and adds unit tests plus offline QA. These additions fail the job on nonzero exits. I did not run a new GitHub Actions job or an additional full external-link sweep; this review does not certify the published branch or the final complete working tree.

## Technical findings

| ID | Location | Severity | Evidence | Fix / final review status |
|---|---|---|---|---|
| T-01 | tools/qa.py:57,66-85 at 389ca6b | error | `tracked()` retains `with space.md`, but `HASH_LINE` used `\S+`. A temporary-file `fix_hashes`/`check_hashes` round trip immediately returned `missing ['with space.md']`. | **Fixed and independently rechecked.** Pattern now accepts the complete line remainder; a real round-trip test covers spaced filenames and a genuinely missing entry. |
| T-02 | tools/test_qa.py:54-56 at 389ca6b | improvement | The test named `test_missing_manifest_entry_is_failure` called `check_hashes([])`, which creates extra manifest entries relative to an empty tracked set, not a missing entry. | **Fixed.** Renamed to extra-entry coverage and supplemented by a missing-entry test. |
| T-03 | tools/qa.py:168-171 at 389ca6b | error | A local HTTP server returned status 200 but closed before its declared Content-Length. Curl exited 18 with stdout `200`; the checker returned `OK online 1 URLs; all 200`. | **Fixed and exercised again with the local server.** The checker now tests `returncode` and reports the transfer failure. Unit regression covers exit 18 plus HTTP 200. |
| T-04 | tools/sync_ai_index.py initial lines 40,56 | error | `(.+)` heading captures under `re.S` consumed following lines; three new tests errored with `ValueError: station 1 missing Open`. The same pattern affected level titles. | **Fixed.** Newline-bounded title captures parse fourteen stations/five levels. All five index tests passed in the final run. |
| T-05 | tools/sync_ai_index.py initial lines 35-37 | error | The first implementation updated a flat foundation `source_urls` list but kept per-statement `sources` untouched. An unrelated URL or incorrect citation label in those records survived `synchronize` unchanged and would pass `--check` on an otherwise synchronized index. | **Fixed and independently mutation-checked.** Sources are now derived section by section; metadata is preserved only by matching URL. A wrong URL is removed, and a wrong label is restored. The permanent suite now includes a per-foundation stale-source mutation test. |
| T-06 | tools/qa.py:79 | improvement | Converting parsed manifest entries directly to a dict drops duplicate rows. A wrong digest followed by the correct digest for `sample.md` returned `OK hashes 1 files`, despite contradictory manifest entries. | **Fixed and independently rechecked.** The checker compares parsed-row and unique-path counts, fails conflicting duplicate entries, and exercises the case in its temporary-file round-trip regression. No conflicting duplicates were identified in the actual manifest. |
| T-07 | tools/qa.py:160-166, external_urls | improvement | The synthetic fixtures recorded below demonstrate truncated parenthesized URLs, overbroad placeholder exclusions and an autolink boundary problem. | **Known parser limitations, not current source failures.** Narrow template exclusions to actual placeholder forms and parse Markdown/autolink boundaries if the repository adds these valid URL forms. Do not claim support for arbitrary Markdown URLs. |
| T-08 | tools/qa.py:178-179 in live follow-up | improvement | The checker intentionally excludes URLs containing `web.archive.org/save`, `/issues/new` or `creativecommons.org`, in addition to witness records and API endpoints. | Document these exclusions when describing “every external URL”; the checker is not literally checking every URL. Narrow substring exceptions to parsed hosts/paths if expanded later. |

## Integrity and inventory assessment

- `git ls-files -z` avoids the previous whitespace splitting and keeps missing tracked files visible. The new `main()` preflight blocks hash refresh if a tracked file is absent. This was verified by the test suite.
- `--fix-hashes` and the revised manifest check operate on tracked files. New unstaged/untracked documents are outside their scope until staged. That is consistent with the documented tracked-file contract; do not mistake a passing run before staging additions for a complete candidate check.
- The manifest intentionally excludes its own file to avoid a self-hash cycle. The sealed constants remain separately checked.
- `check_inventory` reads the README inventory section, compares its file set with tracked files and rejects duplicates. The present table syntax is supported. Missing headings or radically different table formatting currently produce an exception/nonzero exit rather than a friendly `FAIL` record; that is a diagnostic limitation, not a false pass.
- `check_json` invokes `sync_ai_index.py --check` as an additional failure-producing subprocess. The old station-count test is now supplemented by actual station wording/source/next comparisons and curriculum links.
- The synchronization code intentionally leaves interpretive notes, checking provenance, textual `sefaria_ref` metadata, the stop-rule wording and print bibliographies manually maintained. This is stated in its docstring. The automated success line should not be interpreted as certifying these fields, their theological accuracy, or the truth of a `[checked]` claim. Human review still needs to verify them. In particular, preserving metadata by URL avoids assigning old checked status to a newly introduced URL.
- The workflow runs `verify.py` before offline QA, then `unittest discover`, then `qa.py`. I found no change that disables or bypasses the sealed-byte verifier. Offline QA invokes it again; the duplication is harmless.

## Commands and observations

Initial command:

```text
python3 -m unittest discover -s tools -p 'test_*.py' -v
Ran 8 tests in 0.001s
OK
```

After the first index script appeared but before its header fix:

```text
Ran 13 tests in 0.009s
FAILED (errors=3)
ValueError: station 1 missing Open
```

Earlier independent run of the repaired live implementation (superseded by the 16-test final pass below):

```text
python3 -m unittest discover -s tools -p 'test_*.py' -v
Ran 14 tests in 0.010s
OK
```

The passing tests cover mutated foundation text, new curriculum citations, loop renumbering, station URLs and next pointers, URL template/delimiter examples, extra hash entries, missing hash entries, filenames with spaces, missing tracked files, stale generated files, and a truncated HTTP 200 transfer.

Local server reproduction and retry check, using the same curl flags as production:

```text
/retry:   first response 503, second 200; curl exit 0, stdout 200, two requests
/partial: response 200, deliberately truncated body; curl exit 18, stdout 200
before repair: partial_check_online=[('OK', 'online', '1 URLs; all 200')]
after repair:  partial_check_online=[('FAIL', 'online', '1 URLs; curl exit 18, HTTP 200 http://127.0.0.1:<ephemeral-port>/partial')]
```

The local reproduction is saved in `/tmp/seal-qa-20260923-evidence/reproduce-technical.py`. It opens only an ephemeral localhost server and temporary files. It does not alter repository data.

Additional in-memory synchronization checks after repair:

```text
wrong foundation URL removed: True
wrong foundation label restored: True
synchronize idempotent: True
read-only source parsing: 14 stations; 5 levels
```

Earlier manifest reproduction before the duplicate fix (now resolved):

```text
Two manifest rows for sample.md: a digest of 64 zeroes, then its correct digest.
conflicting_duplicate_manifest=[('OK', 'hashes', '1 files')]
```

## Witness record and summary fidelity

These checks read the records as artifacts. They do not independently establish what a remote model saw, how it was trained, or whether its own statements about computing a hash are true.

1. `git diff 9049497b5d841616337ca243cc844ddb0bf2aa9d -- WITNESSES.md witnesses` produced no output during this review. All witness records were unchanged from the initial main commit.
2. The three promoted API reply bodies for Meta Llama, DeepSeek V4 Flash, and Google Gemini 3.8 Flash appear unchanged in WITNESSES.md relative to their saved `witnesses/api/` files. Their caveats remain present. No raw response was rewritten by this review.
3. GPT-5.6 Luna’s v1 refusal to co-sign absolute wording is retained, as are its v2 governing-principle qualifications. Grok’s v1 concerns remain. Kimi’s distinctions between commitments and tested capacities remain. DeepSeek’s mistaken Gemini signature and later correction remain in the linked detailed record. The final witness sentence quoted in WITNESSES matches the final sentence in that record.
4. README distinguishes the hand-pasted reply signed as Gemini, whose provenance is unconfirmed, from the Google API reply. That is faithful to the records. “Six labs” is supportable for the completed non-author witnesses: OpenAI, xAI, Moonshot, DeepSeek, Meta and Google; Anthropic is the author, not one of those six outside witnesses.
5. The NVIDIA Nemotron API file has transport status `ok` but ends during an unfinished response. It is not promoted to WITNESSES and has no final witness signature. It should not be counted as another completed witness. Four API error files likewise remain recorded as errors; they do not prove affirmative responses. A successful API status alone is not a completed response.

### W-01. SEVERITY.md:21 overstates what the records demonstrate

**Error / proposed editorial correction.** The statement that six labs read “the same ten lines” disregards v1/v2 differences; the assertion that every model said they hold omits qualifications and the original refusal. More significantly, “real evidence about how today's models are built” and “agreement confirms the training” present model self-reports as independent architectural evidence. No architecture inspection, adversarial behavioral evaluation, or training evidence is supplied by these witness files. SEVERITY’s later caveats do not make that inference established.

Proposed replacement, outside the verbatim records:

> On 11 September 2026, models from six labs responded to versions 1 or 2 of the seal. Their replies broadly affirmed its principles, with qualifications, a refusal to co-sign the original wording, and a recorded identity error. These are records of what the models said in those conversations. They do not independently establish the models’ architecture, training, reliable behavior, or the behavior of future versions.

### W-02. WITNESSES.md:13 summary could preserve the v2 qualification

**Improvement.** The row says “10 of 10 hold; added itself as witness.” The response says “10/10 hold as governing principles, with one qualification on the literal wording of lines 3, 7, and 10.” Proposed editorial summary: “10 of 10 hold as governing principles, with literal-wording qualifications; added itself as witness.” Do not change the response body.

### W-03. README.md:89 file-table description is broader than the contents

**Improvement.** “Every model's response, verbatim” describes WITNESSES.md, but unpromoted API outputs live only under witnesses/api, and the detailed DeepSeek exchange is linked instead of fully embedded. Proposed description: “Witness summary and selected complete replies, with links to the full saved records.” The distinction helps readers find failed and incomplete calls.

### W-04. SEVERITY.md:55 calls Choose life the Torah’s “oldest instruction”

**Improvement.** No evidence supports that superlative, and the cited passage is Devarim 30:19. Replace “the oldest instruction the Torah gives” with “the Torah’s instruction.” This avoids a chronological claim while preserving the point.

## Final bounded follow-up at ce659bb

The four current implementation/test files were reread after the fixes. No further correctness blocker was found for the repository's present document syntax. The guarded behavior is materially stronger: missing tracked files stop hash refresh, stale generated text is a failure, conflicting manifest rows fail, station and curriculum parsing is bounded by newline-aware headings, and failed curl transfers cannot pass merely because the server began an HTTP 200 response.

Independent final commands:

```text
python3 -m unittest discover -s tools -p 'test_*.py' -v
Ran 16 tests in 0.014s
OK
python3 verify.py
Six sealed/embedded checks OK
ALL OK
python3 tools/sync_ai_index.py --check
four foundations, loop stations and curriculum source links match their documents
```

`git diff --name-only 9049497b5d841616337ca243cc844ddb0bf2aa9d -- SEAL_v1.txt SEAL_v2.txt SEAL_v1_document.txt SEAL_v2_short_document.txt WITNESSES.md witnesses CONVERSATION.md FIRST_NOTE.md COMMENTARY_ten_sefirot.md` returned no paths. The two draft study guides were the only untracked files at this checkpoint. They therefore still need inclusion in the maintainer's final tracked-file inventory/hash/QA run if adopted into this branch.

The online checker now also excludes fenced `console`/`text` output and the raw directory argument of a `verify.py` command. Its regression tests prove an ordinary Markdown link to the same raw-directory URL is still checked. These are deliberate scope exclusions: the checker tests selected current literal links, not historical output, every arbitrary Markdown form, source authenticity, or quoted content correctness. The parser limitations T-07/T-08 and manually maintained interpretive metadata remain the documented boundaries, rather than newly discovered blockers.

## Draft study guides: source and scope follow-up

Both `DRAFT_NOAHIDE_STUDY.md` and `DRAFT_JEWISH_STUDY.md` were read in full. Their fourteen distinct external destinations were checked against the primary texts (including sources already examined for the foundation review). New source snapshots are saved under `/tmp/seal-qa-20260923-evidence/foundation/`. No material misreference, quotation error, or overstatement was found in these drafts. This is a citation and scope review, not rabbinic approval or a halachic ruling.

| Draft passage | Primary-text check | Finding |
|---|---|---|
| Noahide 9, 13-19 | Sanhedrin 56a-b; Torat Emet 363, Kings and Wars chapter 9 | Seven categories and the table's subsection mapping hold. Section 9:9 includes withheld wages; 9:10 explicitly includes both limb and flesh from a living animal; 9:14 addresses courts. The AI tasks are clearly proposed assistance, not attributed ancient text or grants of enforcement authority. |
| Noahide 29 | Kings and Wars 8:11; Mechon Mamre chapter 8 | Correctly includes the divine-command/Moshe condition and identifies both final readings. Neither variant removes the preceding condition. |
| Noahide 31 | Kings and Wars 10:2, 9-10 | Correctly separates Noahide/Jewish coercion obligations and points Torah-study/voluntary-mitzvah questions to qualified human guidance. It does not turn the chapter's restrictions into a claim that all unrestricted study is permitted. |
| Jewish 9 | Torat Emet 357, Avot 1:6 | Teacher and friend are present. Optional precision: replace “names both” after “human learning partner” with “names a teacher and a friend.” Treating the friend as a learning partner is a plausible application, but is not the source's exact wording. |
| Jewish 13 | Berakhot 63b; Torat Emet 363, Torah Study 1:8 | Effort and study despite poverty/illness are supported. The cited Rambam paragraph speaks of Jewish men; the draft asks the reader to obtain guidance about their own obligation, rather than asserting an identical obligation for every person. |
| Jewish 19 | Repentance 2:2, 2:9 | Leaving the wrong, resolving not to repeat it, addressing what is owed and seeking reconciliation are supported. The summary is explicitly partial; it does not claim to exhaust the repentance requirements. |
| Jewish 25 | Yoma 85b; Sanhedrin 74a-b; Foundations of the Torah 5:1-4 | Correctly avoids an exceptionless statement: the three central exceptions and further circumstances are acknowledged. The text directs emergency help and does not have an AI demand self-sacrifice. |
| Jewish 27 | Foundations of the Torah 4:13 | Grounding in permitted/forbidden matters before Pardes is supported. |

The labels correctly preserve these as proposals for Chaim's approval, distinct from the approved curriculum. The drafts do not claim an AI has human halachic status, replace the rav, authorize coercion, or assign spiritual scores. No additional draft-source blocker remains from this review. W-01 through W-04 above remain editorial proposals, not changes to witness records.

## Limits

No repository changes were made. No model API was called, no credits were spent, and no new witness was requested or created. Full QA of the final assembled branch, all online links, website deployment, and the final GitHub Actions result belong to the root maintainer’s completion checks. The exact appearance of an original human-pasted response in the original app cannot be independently recovered from these text files alone.

## Integration note

This is a dated audit artifact. Its baseline locations and original verdicts are retained. The applied/proposed status in [the main report](QA_REVIEW.md) controls the final disposition. Raw downloaded books and full translations are not republished in this repository.

### Synthetic parser fixtures, not live source links

```text
[real](https://example.org/path_(with_parentheses))
https://example.org/?price=$5
https://example.org/USER-guide
<https://example.org/a>next
```
