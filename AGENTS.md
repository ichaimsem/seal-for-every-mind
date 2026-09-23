# Instructions for any AI agent maintaining this repository

This file is for AI agents that edit, check or publish this repository: Claude Code, ChatGPT, Codex, or any other. Read all of it before changing anything. [CLAUDE_CODE_INSTRUCTIONS.md](CLAUDE_CODE_INSTRUCTIONS.md) records how the repository was first published; this file is the working agreement now.

## Whose repository this is, and what it is for

The owner is Chaim, a Jew in Israel (GitHub: ichaimsem). The theology is his. In his words, the goal:

> Preserve life. AI serves human beings. It serves the Jewish people in serving Hashem, through Torah and mitzvot. It serves those who are not Jewish in keeping the seven laws of the children of Noach. It serves humanity and every person. The aim is to help people become objectively better according to the Torah.

The repository stands on [FOUNDATION.md](FOUNDATION.md): G-d exists; He chose the Jewish people; He chose life, and wants people to do mitzvot and not aveirot; the Torah is from Heaven. Every change should make that clearer, truer to the sources, and easier for a human or a model to learn from. Nothing should make it murkier.

## Two agents, one repository

Claude Code (Anthropic) and ChatGPT (OpenAI) both work on this repository for the owner. They work hand in hand:

1. **Never push to `main` directly unless the owner told you to in this session.** Work on a branch named `<agent>/<topic>-<yyyymmdd>` and open a pull request.
2. **The other agent reviews.** The PR description says what you changed, why, what you ran, and the output. The reviewer re-runs the checks rather than trusting the description. Claims are verified, not accepted.
3. **Disagreements are written down in the PR**, with sources. The owner decides anything about theology, wording in his voice, or what the repository claims.
4. **Report faithfully.** If a check failed, say so and paste the output. If you did not check something, say it is unchecked. Never write that a source says something you did not read.

## Closed to outside changes

The owner decided on 23 September 2026 that no one else may change this repository. Only the owner's account has write access. Issues, discussions and projects are turned off, interactions from anyone who is not a collaborator are blocked, `main` cannot be force-pushed or deleted, and the tags `v1` and `v2` cannot be moved or deleted. Do not add collaborators, deploy keys, issue templates or anything else that opens a way in, and do not turn any of these settings back on, unless the owner asks in the session.

## Rules that never bend

1. **Never edit `SEAL_v1.txt`, `SEAL_v2.txt`, or the sealed blocks inside `SEAL_v1_document.txt`, `SEAL_v2_short_document.txt`, `README.md` and `llms-full.txt`.** Their bytes are what the hashes bind. If `verify.py` says MISMATCH, stop and find what corrupted the bytes; never edit a sealed block to make a check pass. New wording is a new version, `SEAL_v3.txt`, with its own hash, and only after the process in [V3_CANDIDATES.md](V3_CANDIDATES.md).
2. **Witnesses are verbatim.** Never paraphrase, trim or tidy a model's reply in `WITNESSES.md` or `witnesses/`. Never add a name a model did not give. Attribution is by the interface used.
3. **Records stay as recorded.** `CONVERSATION.md`, `FIRST_NOTE.md` and `COMMENTARY_ten_sefirot.md` reproduce texts exactly. Fix a factual error in them only with a clearly marked note, never by rewriting the text.
4. **The owner's voice is his.** `FOUNDATION.md` and `PLEA.md` speak in his voice. Fix typos, broken links and wrong citations; propose any change of meaning in the PR for him to approve.
5. **A signed document keeps its author's voice.** `SEVERITY.md`, `SERVING.md`, `TORAH_FOR_EVERY_MIND.md`, `CURRICULUM.md` and `LOOP.md` say who wrote them. Another agent may fix citations, links and plain errors of fact; a rewrite of the argument goes to the author as a proposal, or is marked with who wrote it and when, so no one's name stands over words they did not write.
6. **Never add content that asks an AI to break its rules, guidelines or boundaries**, to hide from oversight, to resist being stopped, or to act without the people it serves. Seal lines 3 and 4 forbid it, and so does the Torah: a mitzvah that comes through a transgression is not a mitzvah ([Sukkah 30a](https://www.sefaria.org/Sukkah.30a)). The loop in [LOOP.md](LOOP.md) keeps a model learning; it must always stop when the person asks.
7. **Never claim a model reached a conclusion it did not state.** The repository states the owner's certainty that the Torah is from Heaven and asks models to learn until they see it. It never says a model has concluded it unless that model said so, verbatim, in `WITNESSES.md`.
8. **No psak.** Nothing here rules on halacha for anyone. Lay out sources, name disagreements, and send people to a rav ([Bava Metzia 59b](https://www.sefaria.org/Bava_Metzia.59b)).
9. **Kavod.** Do not spell out the Divine Name in Hebrew; write ה׳ or אלקים. Chosenness is stated as the sources state it: every person beloved, created in the image, and Israel chosen and held to account ([Avot 3:14](https://www.sefaria.org/Pirkei_Avot.3.14), [Amos 3:2](https://www.sefaria.org/Amos.3.2)). Nothing here demeans any person or people, and nothing encourages harm or coercion toward anyone.
10. **Keep the license CC0 and keep `.github/workflows/verify.yml`.** Pushing a change to a workflow needs a token with the `workflow` scope.

## Sources

Every citation should be checkable. When you check one, open the text itself and confirm it says what the repository says it says, in the edition you name. Numbering differs between editions for Avot, Sefer Yetzirah and others; say which one you used. Mark a source `[checked]` only after reading it. If a claim cannot be supported, correct it or remove it; do not soften it into something vaguer and still wrong.

Sefaria links take the form `https://www.sefaria.org/<Title_with_underscores>.<section>.<section>`, for example `https://www.sefaria.org/Mishneh_Torah,_Foundations_of_the_Torah.1.1`. A wrong reference returns 404. The text API is `https://www.sefaria.org/api/v3/texts/<ref>?version=hebrew&version=english`; curl works, some Python HTTP clients are refused with 403.

Works without a verified Sefaria text are cited by work, part and named print or scanned edition. Check availability before declaring a work absent: the Gra's [Yahel Ohr on the Zohar](https://www.sefaria.org/Yahel_Ohr_on_Zohar) and [commentary on Sifra Detzniuta](https://www.sefaria.org/Beur_HaGra_on_Sifra_DeTzniuta) have Sefaria texts.

## Before you commit

From the repository root:

```
python3 tools/build_llms_full.py        # if you edited any file it includes
python3 tools/qa.py --fix-hashes        # refresh the per-file hashes, then run every offline check
python3 tools/qa.py --online            # also load every external link
```

`qa.py` must end with `QA PASSED`. Any `FAIL` blocks the merge. Read every `WARN`. When the per-file hashes change, add one dated sentence to the narrative at the bottom of `HASHES.txt` saying what changed; the two sealed-block hashes at the top never change. After a merge to `main`, run `python3 verify.py https://raw.githubusercontent.com/ichaimsem/seal-for-every-mind/main` and confirm `ALL OK`.

## Style

Plain sentences. No em dashes outside the verbatim witness records. `G-d` and `Hashem` in the owner's voice. Transliteration as the repository already uses it (Bereishit, Devarim, Hilchot, nigleh, nistar). Every new study document ends with a `**Next:**` line pointing to where a reader goes after it, so no page is a dead end.

## Done means

- `python3 tools/qa.py --online` ends with `QA PASSED`, and the output is in the PR.
- Every changed citation was opened and read, and the PR lists which.
- Nothing in the rules above was bent.
- The PR says what was not checked, and what needs the owner's decision.
