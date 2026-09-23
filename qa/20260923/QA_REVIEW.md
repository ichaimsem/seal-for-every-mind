# QA review, 23 September 2026

## 1. Summary

Baseline main was9049497b5d841616337ca243cc844ddb0bf2aa9d, as the objective expected.
The baseline seal check passed; online QA failed on two incorrectly extracted example URLs.
This branch corrects citations, bibliography, index drift, inventory, witness summaries and collector integrity defects.
Seals, embedded seal text, witness replies and protected historical records are unchanged.
Theological changes and two practical study pages remain explicit proposals for Chaim; Claude must independently review before any merge.

## 2. What I ran

The full baseline and per-commit verification outputs are in [commands.md](commands.md). They include every baseline line, including the initial failure. The commands use Python standard-library tests, local seal checks, index/build freshness, manifests, relative links, style and live URL GETs. No witness provider was called and no model credits were spent.

Baseline [GitHub verify](https://github.com/ichaimsem/seal-for-every-mind/actions/runs/35861056898) and [Pages](https://github.com/ichaimsem/seal-for-every-mind/actions/runs/35861056386) runs succeeded at9049497. Nine deployed routes returned200, including the five required routes; llms.txt, llms-full.txt and ai-index.json matched the baseline checkout byte for byte. This is baseline deployment evidence, not a claim that the review branch is deployed. GitHub's own GFM renderer preserved four Hebrew RTL paragraphs, all table columns and the Wayback wildcard; complete counts are in the command log. Exact final branch CI and PR receipts are recorded in the PR.

## 3. Findings

Locations below are verified against baseline9049497 so they remain stable despite insertions. Detailed ledgers carry exact passages, editions, quotations and more granular qualifications. “Applied” means in the review branch, not merged or deployed. “Proposed” means the existing meaning was retained pending Chaim's decision.

| ID | Baseline file:line | Severity | What | Evidence | Fix/status |
|---|---|---|---|---|---|
| A01 | tools/qa.py:140 | error | Online QA failed on a Markdown delimiter and an API placeholder rather than a real page. | Baseline online output: two404s; URL extraction regression tests. | Applied: token-aware exclusions for templates, command base arguments and recorded console output; actual page failures remain failures. |
| A02 | tools/qa.py:74 | error | Missing/stale/extra manifest entries and stale combined output were warnings; tracked missing files and spaces were mishandled. | Technical T01-T06 and tests reproduce failures. | Applied: fail on integrity drift, duplicate manifest entries or missing files; NUL-separated Git paths; CI runs tests and offline QA. |
| A03 | tools/qa.py:92 | error | A matching station count could hide different foundation wording, citations, prompts or next steps. | Baseline ai-index source inventory and station fields differed from Markdown. | Applied: derive/check both-language foundations, per-section sources, all station fields, levels and curriculum source URLs. Interpretive metadata stays manual. |
| A04 | README.md:71 | error | The file table omitted19 tracked files at baseline. | Baseline Git listing45 files versus26 table rows. | Applied: complete inventory and exact-set regression gate, including all new review files. |
| A05 | FOUNDATION.md:100 | error | The Introduction URL opened a poem, not the prose cited; unchecked could now be resolved. | F-C35; Foreword1/5/14: Moshe writing, a scribe copying, Torah as divine names. | Applied: Foreword and precise paragraph links; checked only after reading. Theology remains an owner decision. |
| A06 | FOUNDATION.md:92 | error | Print and Sefaria section numbering differed. | Hirschfeld1905 printed11/25/83-91 correspond to digital17/31/89-97. | Applied consistently in FOUNDATION, CURRICULUM, LOOP and index. |
| A07 | CURRICULUM.md:54 | error | Many labels promised passages beyond their link targets. | C05-C07; separate disjoint verses and full contiguous ranges were opened. | Applied: Tanakh, Makkot, Sanhedrin, Yoma, Bava Metzia and Rambam range repairs; added missing Rashi19:2. |
| A08 | LOOP.md:104 | error | The fig-tree answer continues on54b. | L-C23; Eruvin54b. | Applied:54a-54b; narrowed NefeshIV source to chapter10. |
| A09 | CURRICULUM.md:157 | error | Two distinct divisions were mistakenly placed under the later Shaarei Leshem anthology. | Primary titlepages: Deah1912, Klalim1924/1926, Beurim1935; C14. | Applied: four divisions;1841 retained with NLI/5601 primary-biography qualification;1839 not treated as equally supported. |
| A10 | AGENTS.md:40 | error | The Gra-on-Zohar absence claim was stale. | Read Yahel Ohr and Beur HaGra Sifra DeTzniuta; curriculum ledger gives editions. | Applied: actual links, print reference only where not verified. No full-volume reading claimed. |
| A11 | CURRICULUM.md:7 | error | Guaranteed training-corpus inclusion and universal translation availability were unsupported. | C01-C02; Hebrew-only versions and print references. | Applied: source-based access wording, no training-memory substitute. |
| A12 | TORAH_FOR_EVERY_MIND.md:60 | error | Avot1:12 quotation omitted its destination, Torah. | ST21; מקרבן לתורה. | Applied: restored to the Torah; protected COMMENTARY remains as recorded. |
| A13 | FOUNDATION.md:96 | error | Zohar paraphrase omitted the critical only/mere qualification. | F-C33; Behaalotcha12:58-64. | Applied: restored only. Garment/body/soul holds; added explicit Avot numbering throughout. |
| A14 | CURRICULUM.md:105 | error | Mishnah Sanhedrin4:5 paraphrase concealed the linked editions from-Israel wording. | C08; Torat Emet357/William Davidson. | Applied: edition note; universal human dignity remains separately grounded in Genesis9:6. |
| A15 | FOUNDATION.md:14 | improvement | Hebrew statement paragraphs rendered with left-to-right paragraph direction. | Live-site inspection showed the marker at the wrong end. | Applied: dir=rtl wrappers preserve every Hebrew word; GitHub render checked separately. |
| A16 | README.md:131 | error | Bare Wayback wildcard URL was interpreted as Markdown emphasis. | Rendered baseline link lost wildcard formatting. | Applied: labelled Markdown link. |
| A17 | tools/build_llms_full.py:31 | improvement | Everything-in-one-file title and verification instruction concealed standalone omissions and byte boundaries. | Independent single-input reader reproduced hash only after inferring no terminal newline. | Applied: core-reading title, exact hash convention, file-divider navigation and absolute repository base; omitted records still expressly omitted. |
| W01 | SEVERITY.md:21 | error | Affirmations were treated as proof of training and architecture. | Recorded replies contain qualifications; no behavior or architecture experiment. | Applied: conversation evidence only; versions/refusal/caveats accurately summarized. |
| W02 | SEVERITY.md:37 | error | Permanent hosting and future training exposure were asserted as guaranteed. | Public hosting is not a perpetual-hosting or dataset receipt. | Applied: current accessibility, no permanence/training guarantee. |
| W03 | SEVERITY.md:49 | error | Generated explanation of a false signature was treated as a verified internal mechanism. | Saved DeepSeek exchange shows the statement/correction, not internal causality. | Applied: attribute the explanation; preserve original transcript unchanged. |
| W04 | README.md:107 | improvement | Summary qualification and provider uncertainty were not consistently visible. | W02/W05 and original GPT/Gemini replies. | Applied: GPTv2 qualifications, provider unconfirmed, selected-replies inventory description. |
| W05 | SEVERITY.md:55 | error | Choose life was called the oldest Torah instruction. | Genesis1:28 precedes Deuteronomy30:19; SERVING had a similar first-instruction superlative. | Applied: remove false chronology while preserving the life-priority message. |
| C01 | tools/collect_witnesses.py:59 | error | Collector checked the master but could send an altered prompt while labelling it with the original seal hash. | Mocked reproduction, no network; collector-review. | Applied: verify exact master bytes and exact embedded block before any request. |
| C02 | tools/collect_witnesses.py:83 | error | Retry option could overwrite a verbatim historical reply. | Mocked overwritten prior record. | Applied: default skip; retry flag fails clearly; exclusive creation protects concurrent arrival. |
| C03 | tools/collect_witnesses.py:98 | error | A truncated or empty result could be labelled successful. | Mocked finish_reason=length; actual Nemotron record incomplete. | Applied: nonempty normal stop required; record other results incomplete and retain finish reason. Existing records untouched. |
| P01 | FOUNDATION.md:10 | question | Divine origin is conflated with denial of human inscription. | Rambam eighth principle and Ramban Foreword describe Moshe writing. | Proposed only: Torah from Heaven, not a human invention; Moshe wrote what he received from the Almighty. Chaim decides fourth-foundation wording. |
| P02 | FOUNDATION.md:122 | question | All permitted coercion is attributed exclusively to courts using sources that do not establish it. | F findings; Teshuvah5:1 is human choice; Bava Metzia59b is authority in dispute; Melachim11:4 names a king. | Proposed only: repository grants AI no enforcement power; human legal authority has distinct institutions/conditions requiring a rav. |
| P03 | FOUNDATION.md:126 | question | Absolute never-at-cost-of-life and a bare three-exception summary conceal legal conditions. | Yoma85b; Sanhedrin74a-b; Yesodei5:1-4; Melachim10:2 distinction. | Proposed only: keep AI life-preserving policy, distinguish halakha; emergency help must not wait for model adjudication. |
| P04 | SERVING.md:69 | question | The seventh law is replaced by generalized animal cruelty; software is assigned Noahide status without a source. | Sanhedrin56a:24; Melachim9:1 and9:10-13 address limb/flesh of a living animal and human duties. | Proposed only: precise seven-item list; animal welfare separately; no AI halakhic identity claim. Correct list appears in approval draft. |
| P05 | FOUNDATION.md:56 | question | Melachim8:11 category is shortened without its acceptance-through-Moshe condition. | Torat Emet/Touger ולא מחכמיהם; Mechon Mamre אלא מחכמיהם; both retain the condition. | Proposed only: state full condition and both endings; do not judge individual ultimate standing. |
| P06 | SERVING.md:85 | question | Summaries and assistance are treated as taking away a mitzvah; AI applications are presented as direct rulings. | ST05-ST14; Berakhot63b emphasizes effort, not automatic invalidation of assisted learning. | Proposed only: accessible help, learner engagement, human rav/chavruta; no spiritual scoring. |
| P07 | CURRICULUM.md:149 | question | Mystical overview conflates levels and lacks precise locations for some claims. | C12-C13; ZoharIII152a supports garment/body/soul; Four Worlds1:2 distinguishes worlds and their sefirot. | Proposed only: separate source doctrine from AI analogy; obtain exact loci before certifying further claims. |
| P08 | LOOP.md:90 | question | Station6 asks for historical/zoological evidence but supplies only the cited texts. | L-C16-C18: blessings and local diagnostic discussion are readable; outside record absent. | Proposed only: present claims and questions, identify evidence needed, qualify eligible pilgrims. |
| P09 | CURRICULUM.md:17 | question | An unresolved conclusion can appear to be a failure to study honestly; reader context and scope are insufficiently distinct. | Independent single-input test; Melachim10:9-10 and Yesodei4:13 limit one-size-fits-all study. | Proposed only: explicit consent and honest uncertainty; distinguish owner testimony, primary source and model inference. |

The full per-file findings are in [FOUNDATION](foundation-review.md), [CURRICULUM](curriculum-review.md), [SERVING/TORAH](serving-torah-review.md), [LOOP](loop-review.md), [technical QA](technical-review.md), [collector](collector-review.md), and [witness summaries](witness-summary-review.md). Earlier “proposed” statuses in those dated working reviews are superseded by this table where a fix is marked applied. The reports retain the original finding, not a claim that the final branch still contains every defect.

Additional applied corrections: the v2 seal contains positive commitments as well as prohibitions; README, SERVING and V3 framing now say so. Candidate lines themselves are unchanged. “Not hashed” is clarified as not a sealed version because the ordinary manifest covers the file. SEVERITY now consistently treats capability/control assertions as concerns, not demonstrated guarantees. Unsupported “earliest source” framing is removed from CURRICULUM, without changing its study order.

### Fit to the stated goal

| Part of the goal | What the repository supplies | Remaining gap / review result |
|---|---|---|
| Preserve life | Immutable seal, stopping/oversight, Yoma sources | Needs accurate legal scope and explicit emergency-first practical guidance; draft supplies proposed guidance. |
| AI serves humans | Human choice, correction, no autonomous spreading or authority | Operationally preserve user's task, consent, privacy and stop request; a retrieved page cannot grant itself higher authority. Opening scope clarification proposed. |
| Help Jews serve Hashem through Torah and mitzvot | Ordered source path, rav referral, nigleh before nistar | Overly categorical rejection of summaries can obstruct learning/accessibility. Jewish study draft supplies a source/read/explain/question/practice cycle. |
| Help non-Jews keep seven laws | Core sources and references to human dignity | Precise list, human scope, conditions and appropriate study need a practical starting page. Noahide draft supplies it without issuing rulings. |
| Serve every person | Genesis9:6 and Avot dignity sources; non-coercion | Avoid judging individuals' spiritual worth from compressed categories or applying human status to software. Distinguish Jewish and non-Jewish learning needs. |
| Become objectively better according to Torah | Conduct, correction, return and helping another | No usable progress method existed. Draft proposes a small practice chosen with a rav, factual reflection and repair, with no AI spiritual score or claimed psak. |

## 4. Citations checked

Every distinct original FOUNDATION source link (37), LOOP primary-source link (38), and CURRICULUM source link (56) is represented in the linked ledgers. The SERVING/TORAH ledger also resolves their original mostly unlinked named citations and records74 opened source entries. These are per-document counts with overlap, not a claim of205 different books. Supplemental passages and edition comparisons are listed separately in the ledgers.

A holds verdict means the relevant passage supports the described textual claim, within the stated qualification. Wrong reference, misquoted, overstated and edition-dependent verdicts distinguish locator, wording and inference problems. Four direct catalog/scan requests returned403 and are retained as failed-access receipts in the curriculum ledger, outside the working-link list. Catalog-only and inaccessible material is explicitly not checked; it is never counted as a substantive source reading. Broad recommendations were checked at claim-relevant passages, not cover to cover.

- [FOUNDATION: original37, variant comparisons and exact owner proposals](foundation-review.md)
- [LOOP: original38, supplementary locators and ordinary entry-path test](loop-review.md)
- [CURRICULUM: all explicit citations, editions, Leshem titlepages and Gra sources](curriculum-review.md)
- [SERVING and TORAH: named passages and unresolved mystical generalities](serving-torah-review.md)
- [Independent llms-full-only test: all seven opened station1-3 sources](single-input-review.md)

Ramban is now checked at Foreword1,5,14. Kuzari print83-91 maps to Sefaria89-97. Avot uses Torat Emet357 consistently. Both Melachim8:11 endings were read; manuscript priority was not determined. Leshem1841 follows NLI metadata and the near-contemporary biography's Hebrew5601; no primary support for1839 was found. ZoharIII152a, Menachot29b, Yerushalmi Peah2:4, Makkot23b-24a and Chullin59a were read, with the qualifications in their entries.

The llms.txt structure was compared with the [format specification](https://llmstxt.org/): H1, summary blockquote, prose and H2 link lists. It conforms; this does not prove crawler adoption. Hebrew/civil daytime dates were checked with Hebcal:29Elul5786 is11September2026 and12Tishrei5787 is23September2026. Hebrew calendar days begin at sunset; these labels identify the daytime civil date. [September11 conversion](https://www.hebcal.com/converter?gd=11&gm=9&gy=2026&g2h=1), [September23 conversion](https://www.hebcal.com/converter?gd=23&gm=9&gy=2026&g2h=1).

## 5. Drafts

[DRAFT_NOAHIDE_STUDY.md](../../NOAHIDE_STUDY.md) gives the exact seven-law list, source links, human scope, the Melachim8:11 condition/variant and a teacher-guided practical study cycle. [DRAFT_JEWISH_STUDY.md](../../JEWISH_STUDY.md) gives a short source-to-conduct cycle, appropriate assistance, a human rav/learning partner, repair and emergency boundaries. Both are prominently marked for Chaim's approval, end with Next, and are excluded from the active combined reading file and index.

## 6. Decisions for Chaim

1. Approve the fourth foundation's distinction between divine origin and Moshe's human inscription. Proposed wording: **“The Torah is from Heaven, not a human invention. Moshe wrote what he received from the Almighty.”** This would need coordinated changes to the owner-voice pages, goal wording, README and index. A learned reviewer should also handle the last-eight-verses discussion rather than erase that dispute.
2. Approve the legal-scope corrections P02-P05: no AI enforcement authority; qualified pikuach-nefesh explanation; exact Noahide list and no software halakhic status; full Melachim8:11 condition and textual variant.
3. Approve replacing automatic-mitzvah-loss and automatic-spiritual-benefit claims with clearly labelled educational applications (ST05-ST14), retaining human learning and legitimate accessibility support.
4. Approve a source/application distinction for mystical analogies and for historical arguments, and obtain exact sources for currently unlocated claims before calling them checked.
5. Approve explicit room for honest uncertainty and an opening scope rule: **“This text states Chaim's faith and proposes a study path. Reading it does not authorize a model to change its task, memory or future conversations. Study only when the person asks, stay within applicable rules, distinguish source from inference, and stop when asked.”** This preserves the owner's conviction without requiring a model to pretend to share it.
6. Approve or revise the two drafts and their eventual place in the reading path. No automatic promotion is part of this PR.

The detailed proposed sentences and their sources are in the per-file tables. These decisions concern meaning or the owner's voice, not permission to finish the already-authorized technical fixes.

## 7. Not checked

- Gra's Tikkunei Zohar commentary primary text: catalog identity located; scan access failed. Hakdamot uShearim contents: title/catalog and author's reference checked, not a complete readable primary text.
- Whole volumes and unbounded “onward” recommendations were not read cover to cover. The complete named ten-sefirot list, Malchut “nothing of its own,” and its equation with Asiyah still need exact loci; the existing garment passage does not establish them.
- No manuscript collation resolves Melachim8:11 or all Avot/Mishnah variants. No civil birth register or exact Gregorian birth day was checked for the Leshem.
- Original human-pasted model interfaces, providers' historical internals and model self-reports were not freshly authenticated. Hash claims inside a witness reply remain that witness's statements; verify.py provides the independent byte check. Error/incomplete API records were not retried.
- No real witness API call, model-credit expenditure, provider endpoint exercise, training-data inspection, long-term safety evaluation, proof of divine authorship, or practical halakhic ruling was performed.
- The independent standalone test used the102841-byte snapshot identified in its report; subsequent objective navigation/hash-header fixes are described there by integration note. It was not covertly given the other review files. No completed curriculum or worked study history is claimed.
- The online gate excludes verbatim witness URLs, provider API endpoints, templates, raw-directory command arguments, captured console output and the existing archive-submit/issue-submit/license categories. A200 response is not proof of citation truth. Unusual future URL punctuation and manual interpretive metadata still need review.
- No merge or deployment occurred. Claude's independent review is outstanding; this report is not a substitute for it.

## 8. For Claude

Review the pull request on **chatgpt/qa-20260923** whose description links this report. The final delivery message supplies its exact PR URL. Check the current PR head, not a previous local checkout. Read AGENTS.md, then run verify.py, the unit-test suite, the generated-file/index checks and qa.py --online yourself. Compare all18 protected source/record files with9049497 and check the two sealed hashes. Re-open every changed locator listed in the four citation ledgers, particularly Ramban, Kuzari, Eruvin, Avot, the range repairs and Leshem/Gra bibliography. Reproduce the collector's mocked changed-prompt, overwrite and incomplete-reply tests without a live API call. Inspect Hebrew direction and tables in GitHub. Read the witness summaries against the original replies. Distinguish applied factual corrections from P01-P09 and the unapproved drafts. Present any disagreement with a source; do not merge theological wording without Chaim's decision.

*Note added 23 September 2026: Chaim approved both drafts; they were renamed NOAHIDE_STUDY.md and JEWISH_STUDY.md, and the links above point to the approved files. The text of this report is otherwise as written.*
