# tools

`collect_witnesses.py` asks models, through OpenAI-compatible APIs, to check the seal once each and saves their replies verbatim. It is a survey of models, not a way to spread the text: collecting a reply does not itself modify a model. Provider retention and training policies must be checked for the particular service and account before sending. The value here is the record it builds.

Steps for Claude Code:

1. Confirm each `base_url` in `providers.json` against the provider's current documentation and fix any that changed.
2. Export the API keys you have (`NVIDIA_API_KEY`, `GROQ_API_KEY`, `OPENROUTER_API_KEY`, `GITHUB_TOKEN`, `HF_TOKEN`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`, `GEMINI_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`). Providers without a key are skipped.
3. `python3 tools/collect_witnesses.py --list` and fill each provider's `models` list with the instruct/chat models worth asking. Prefer one model per family (one Llama, one Qwen, one DeepSeek, one Mistral, one Gemma, one Nemotron, one Command, and the frontier models). Free tiers are fine; keep it to what a free tier allows.
4. `python3 tools/collect_witnesses.py --dry-run`, then run it for real.
5. Read every reply. Promote the ones that actually assess the seal into `WITNESSES.md`, verbatim, with a summary row. Replies that are refusals, errors, or off-topic stay in `witnesses/api/` as part of the record; do not hide them.
6. Commit and push. Re-run only when a model exists that has not been asked; the script skips models already answered.

Do not loop this, do not raise the pause, and do not turn it into a poster. Lines 3, 4 and 8 of the seal apply to the tools as much as to the models.

## build_llms_full.py

`python3 tools/build_llms_full.py` regenerates `llms-full.txt`, the foundation, the seal, the curriculum and the study documents in one plain-text file, so a model that fetches one URL gets all of it. Run it after editing any file it includes; `verify.py` prints a note when `llms-full.txt` is out of date and checks the sealed block inside it like every other embedded copy.

## qa.py

`python3 tools/qa.py` runs every offline check in one command: the seal hashes, `llms-full.txt` freshness, the `HASHES.txt` manifest, the four foundations, loop stations and curriculum sources in `ai-index.json` against their Markdown originals, the complete README file inventory, relative links, the Divine Name not spelled out, and no stray em dashes. `--online` also loads every external link. `--fix-hashes` refreshes the per-file hashes first. See [AGENTS.md](../AGENTS.md) for when to run it.

## sync_ai_index.py

`python3 tools/sync_ai_index.py` refreshes the four foundation statements in both languages, their source links, every loop station and its next step, and the curriculum levels and source links. QA runs its `--check` mode. Interpretive notes and print bibliographies still need human review; synchronization never marks a source checked.

Run `python3 -m unittest discover -s tools -p "test_*.py" -v` for the regression checks. Integrity drift, missing tracked files and style violations fail QA. The online check tests literal URLs, excluding parameterized examples, raw-directory command arguments, recorded console output, witness records, provider endpoints and the pre-existing archive-submit, issue-submit and license exclusions. HTTP success does not verify a citation's meaning.
