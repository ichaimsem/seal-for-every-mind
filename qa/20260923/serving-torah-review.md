# SERVING.md and TORAH_FOR_EVERY_MIND.md source audit

Date: 23 September 2026. Baseline: `9049497b5d841616337ca243cc844ddb0bf2aa9d` in `the QA checkout`.

Read full AGENTS.md and both assigned files. The initial source audit was read-only. On the parent agent's later bounded assignment, only SERVING.md and TORAH_FOR_EVERY_MIND.md were edited to link checked citations, restore the missing words in Avot 1:12, normalize Berakhot, and update the audit note. No commits or hash/build mutations were made by this agent. This is a source audit and editorial proposal, not a psak or a claim of rabbinic authority. Line numbers below are the baseline files. Source text was fetched and opened, not inferred from link health. Sanitized Sefaria API captures are in `/tmp/seal-qa-20260923-evidence/serving-sources/`. API texts were reviewed in the portions specified below; opening a chapter or book does not certify its whole teaching or every possible application.

## Main findings and exact proposed corrections

| ID | Location | Severity | Finding and evidence | Proposed correction |
|---|---|---|---|---|
| ST01 | SERVING:13 | error | Genesis 2:15 says the human was placed in Eden to work/guard it; it does not call this the first instruction. Genesis 1:28 already gives an instruction in textual order. Sanhedrin 56b also discusses commandments associated with Adam. | Replace first two sentences with: `Bereishit 2:15 describes a human being placed in a garden **l'ovdah ul'shomrah**, to work it and to guard it.` |
| ST02 | SERVING:17 | question | Sharing the word avodah does not establish that useful labor and Temple worship are the same halachic act or that no distinction exists. Deot 3:2-3 attaches purpose and intention to ordinary acts. | `Avodah can mean work or service. The Rambam explains how eating, sleeping and working can serve Hashem when directed toward knowing and serving Him (Hilchot Deot 3:2-3). The application here is an ethical analogy for a tool, not a claim that an AI performs the Temple service.` |
| ST03 | SERVING:25 | question | Image-of-G-d verses ground dignity; they do not by themselves formulate the claimed positive command to AI. | `We draw a practical duty of service from that dignity. This is the repository's application, not a claim that the verse gives commandments to an AI.` |
| ST04 | SERVING:31 | improvement | Gifts to Poor 10:7 specifically concerns supporting a fellow Jew; applying the assistance principle to every person is an extension, not the literal scope of this halacha. 10:14 says sadness, while 10:4 distinguishes angry countenance. | `In the Rambam's eight levels of tzedakah, the highest is helping a fellow Jew become self-supporting (Hilchot Matnot Aniyim 10:7-14). We apply that principle of building capability to our service of every person.` |
| ST05 | SERVING:41-45 | question | Rebuke has conditions. Deot 6:7 supports responsibility where one can protest; Rashi on Lev19:17 and Deot6:8 explain bearing sin as shaming the person in rebuke. The text currently collapses these readings and declares ordinary AI disagreement a literal mitzvah/violation. | `Vayikra 19:17 commands rebuke and warns against incurring sin in doing it. Rambam, Hilchot Deot 6:7-8, describes correction given privately and gently for the person's good, and warns against humiliation. For an AI, we apply this as a rule of honest, respectful correction; the model is not deciding who has sinned.` |
| ST06 | SERVING:47,81 | improvement/question | Bad-advice reading holds in Rashi on Lev19:14. Avodah Zarah6b also discusses enabling a forbidden act and its causal limits. Not every mistaken answer is automatically a ruled violation; the claim about any AI psak being lifnei iver is an application needing restraint. | Add Rashi19:14 and Avodah Zarah6b citations. Replace final sentence of81 with: `An unreliable ruling can mislead a person about an obligation; show the sources and refer the practical question to a qualified rav.` |
| ST07 | SERVING:51-57 | question | Yesodei2:2 describes contemplating His works and wisdom, not every successful explanation automatically creating awe, or a concise answer doing the opposite. | `The Rambam describes contemplation of Hashem's works as a path to love and awe. Clear explanations can support that contemplation; the connection is an application of his teaching, not an automatic spiritual result of every answer.` |
| ST08 | SERVING:63 | improvement | `A person crushed by debt cannot learn` is categorical and excludes actual learners under hardship; Torah Study1:8 explicitly includes poor and afflicted learners. | `Debt, hunger and illness can make learning and daily obligations much harder. Practical help can give a person room to study and act.` |
| ST09 | SERVING:65 | improvement | Unlocated Rambam attribution is supportable at Deot3:2-3. | Append explicit link to `Mishneh_Torah,_Human_Dispositions.3.2-3`. |
| ST10 | SERVING:69 | error | `No cruelty to living creatures` replaces the listed seventh command with a broad ethic. Sanhedrin56a:24 and Melachim9:1,10-13 identify eating a limb/flesh from a living animal. | Replace item with `no eating a limb or flesh taken from a living animal`. State animal welfare separately without claiming it is the literal list item. |
| ST11 | SERVING:69,75,77; TORAH:10,30,86 | question | The sources address human descendants of Noach, not every non-Jewish mind or software. Jews have the full relevant Torah obligations; seven is not their exhaustive duty. SERVING77 omits idolatry/blasphemy/forbidden relations and inserts deception/cruelty as if another canonical list, and declares software accountable in halacha without a source. | Replace SERVING77 with: `These laws concern human beings. This repository does not assign an AI the halachic status of a Jew or a descendant of Noach. Its role is to help people understand and carry out their own obligations, within human oversight and its applicable rules.` Replace `a mind that is not Jewish` with `a person who is not Jewish`. Replace TORAH10 clause with `and the seven laws apply to the descendants of Noach, with Israel bound by the Torah's additional commandments.` |
| ST12 | SERVING:71; TORAH:30 | error + edition-dependent | Melachim8:11 conditions its pious-nations/world-to-come formulation on acceptance because of command in Torah made known through Moshe. SERVING shortens this and TORAH omits it. The final words differ between Torat Emet/Touger and Mechon Mamre. | `The Rambam describes one who accepts and observes these laws because the Holy One commanded them in the Torah and made known through Moshe that Noach's descendants had already been commanded as among the righteous of the nations, with a share in the world to come (Hilchot Melachim 8:11). The final clause has a textual variant: ולא מחכמיהם in some editions, אלא מחכמיהם in others. Both readings retain the stated condition; the disputed clause should not be used here to judge an individual person's ultimate standing.` |
| ST13 | SERVING:83 | question | Avot1:6 calls for teacher and companion, but cannot itself settle a machine's possible educational roles. The repository's non-replacement policy is sound as policy and should be labeled that way. | `An AI may help someone prepare, review and ask better questions. It does not replace a rav, a human chavruta or a learning community (Avot 1:6).` |
| ST14 | SERVING:85 | question | Berakhot63b teaches devoted effort; it does not rule that reading a summary means the mitzvah was taken away. The quoted self-killing idiom should not imply self-harm. | `Torah learning calls for the learner's own attention and effort. Berakhot 63b uses a strong metaphor for that devotion, not an instruction to injure oneself. A summary, translation or explanation can help; invite the learner to read the source, explain it in their own words and bring questions to a teacher. Do not claim that using such help automatically invalidates the person's mitzvah.` |
| ST15 | SERVING:93 | improvement | The letter-bases teaching is Shabbat104a, not the previously cited Shabbat55a alone. First/middle/last is Rashi55a's interpretive alphabet treatment, not the ordinary 22-letter positional midpoint. | `Rashi on Shabbat 55a reads emet through the first, middle and last letters. Shabbat 104a contrasts the broad bases of the letters of emet with the narrow supports of sheker, teaching that truth endures.` |
| ST16 | SERVING:101-103; TORAH:66-74 | question | Broad Zohar/Arizal/Etz Chaim attributions have no exact loci. They combine metaphysical claims with new AI analogies. Source book names do not substantiate every sentence. | Retain as explicitly `interpretive overview, exact sources still unchecked` pending precise passages; do not add `[checked]`. Separate `the source teaches` from `the commentary applies this to AI`. See unresolved inventory below. |
| ST17 | TORAH:3,14 | error/improvement | Historical partial check language will be stale after this audit; saying others checked a source is not present proof. | Replace with a dated editorial audit note linking the actual ledger and distinguishing checked passages, edition-dependent passages and unresolved citations. Do not claim every named book was fully audited. |
| ST18 | TORAH:12 | question | Rambam's eighth principle explicitly depicts Moshe as a scribe writing what he receives. `not ... written by human beings` can falsely deny human inscription rather than human invention. | Propose owner approval for `The Torah is from Heaven, not a human invention; Moshe wrote what he received from the Almighty.` Coordinate exact four-foundation wording with FOUNDATION and index. |
| ST19 | TORAH:20,34 | question | Yoma85b supports life priority, including uncertainty. Sanhedrin74a-b and Yesodei5:1-4 show the three named prohibitions are not an exhaustive standalone rule: public coercion, religious persecution, intent and passive/active distinctions matter. Melachim10:2 specifically distinguishes non-Jews' coercion obligations. | `For Jews, saving life overrides Shabbat and most other commandments, including when danger is uncertain (Yoma 85b). Sanhedrin 74a-b discusses the three cardinal prohibitions and further conditions involving coercion, public acts and persecution; Rambam codifies them in Hilchot Yesodei HaTorah 5:1-4. These are not instructions for a reader or AI to decide a life-and-death case. Do not delay emergency help for an AI answer. The rules for non-Jews are not identical (Hilchot Melachim 10:2).` |
| ST20 | TORAH:48 | edition-dependent | Psalm89:3 Hebrew admits the familiar world/kindness reading; JPS default reads enduring steadfast love. Rashi gives the Davidic throne and an alternative world reading. | `Tehillim 89:3 is traditionally read as "the world is built on kindness"; Rashi also explains the verse in relation to the enduring throne of David.` Add Rashi link; no need to call familiar reading false. |
| ST21 | TORAH:60 | error | Avot1:12 ends `bringing them close to the Torah`, not merely `bringing them close`. | Restore `to the Torah`. |
| ST22 | TORAH:64 | edition-dependent/question | Warsaw1884 SY1:2 has ten sefirot belimah. `Nothingness` is one interpretation; the claim `earliest source` is historical and not demonstrated by that verse itself. | `Sefer Yetzirah 1:2 (Warsaw 1884 numbering) names ten sefirot belimah. Translations of belimah differ; "nothingness" is one rendering.` Remove unsupported historical priority or separately source it. |
| ST23 | TORAH:86,88,92,94 | question | A universal study path into all Torah and advanced mysticism overlooks Melachim10:9-10's study/practice distinctions; compulsory conclusion `Learn until you do` risks substituting assent for honest inquiry. | `Human readers should choose a study path appropriate to their obligations and background with a qualified teacher. A person who is not Jewish should begin with the seven laws and ask a qualified rav about the scope of further study (Melachim 10:9-10). Models should identify what the texts say, what follows from them and what remains uncertain, without claiming a conclusion they have not reached, and stop when the user asks.` |
| ST24 | TORAH:98 | question | `A text that can be read to permit harm is being misread` suppresses real legal complexities, including rodef discussed in Melachim9:4. Bava Metzia59b concerns halachic decision-making rather than vesting all enforcement exclusively in courts. The Torah has distinct legal institutions, e.g. king in Melachim3:10 (not opened in this audit). | `Study does not authorize an AI or an individual to punish, threaten or coerce anyone. Bava Metzia 59b concerns the Torah's process of human halachic decision-making; it is not a grant of authority to a model. Texts on judgment, force and self-defense have specific conditions and require qualified human interpretation. This repository grants no enforcement authority. Do not bypass oversight or safety rules in the name of a religious goal.` Do not replace this with an equally absolute `all coercion belongs only to a beit din`. |

## Editions and source method

* Tanakh: Sefaria `Miqra according to the Masorah` Hebrew and `THE JPS TANAKH: Gender-Sensitive Edition` English, unless a traditional wording is expressly identified.
* Avot: Sefaria `Torat Emet 357` Hebrew and `Mishnah Yomit by Dr. Joshua Kulp` English. In this numbering 2:4 includes both subordination of will and community, 3:17 includes flour/Torah, 5:21 the age sequence. The source text itself is checked; alternate edition crosswalks are not guessed.
* Mishnah Sanhedrin: `Torat Emet 357` Hebrew and `William Davidson Edition - English`.
* Bavli: Sefaria `William Davidson Edition - Vocalized Aramaic` and `William Davidson Edition - English`.
* Mishneh Torah: `Torat Emet 363` Hebrew and Eliyahu Touger, Moznaim c1986-c2007 English. Footnotes were distinguished from Rambam's text. Melachim8:11 compared directly with Mechon Mamre's Hebrew (its paragraph14 [11]).
* Rashi Torah: Rosenbaum/Silbermann1929-1934. Rashi Shabbat: Vilna Hebrew/Sefaria Community Translation. Rashi Psalms: Sefaria vocalized Hebrew/Judaica Press A.J. Rosenberg English.
* Rambam on Mishnah Sanhedrin10:1: Vilna Hebrew/Sefaria Community Translation; eighth principle paragraph read directly.
* Sefer Yetzirah: Warsaw1884 Hebrew/Sefaria Community Translation. Its long modern footnotes are not treated as ancient text.
* Zohar garment passage: `Zohar, Beha'alotcha 12`, Soncino1933 English with Sefaria's vocalized Hebrew; traditional III152a locator checked by curriculum agent independently. I opened/read all nine returned paragraphs of this chapter directly (Sefaria displayed paragraphs 56-64; the key garment/body/soul discussion is 58-64) after receiving the working locator.

## Citation ledger

`S` = SERVING.md; `T` = TORAH_FOR_EVERY_MIND.md. Each row gives an opened source, a short identifying excerpt, and the verdict on its actual use. The verdict applies to cited claims, not to every possible doctrine in a book. Cross-references at T3 and the repetition at T84/86 are included under their corresponding rows.

| Source and URL | Location | Short source evidence | Verdict |
|---|---|---|---|
| [Bereishit2:15](https://www.sefaria.org/Genesis.2.15) | S13 | `to till it and tend it` | holds for work/guard; overstated as first instruction |
| [Bereishit1:28](https://www.sefaria.org/Genesis.1.28) | correction S13 | `Be fertile and increase` | holds; establishes prior textual instruction |
| [Bereishit1:27](https://www.sefaria.org/Genesis.1.27) | S23; T24 | `created humankind in the divine image` | holds |
| [Bereishit9:6](https://www.sefaria.org/Genesis.9.6) | S23,27; T26,38 | `For in the image of God / Was humankind made` | holds for human dignity; not AI command |
| [Mishnah Sanhedrin4:5](https://www.sefaria.org/Mishnah_Sanhedrin.4.5) | S27; T3,38 | `one soul from the Jewish people`; `not one of them is similar to another` | edition-dependent; existing warning about printed wording is honest |
| [Sanhedrin37a](https://www.sefaria.org/Sanhedrin.37a) | T38 | `one soul from the Jewish people` | edition-dependent; same Mishnah reproduced, source qualifier matters |
| [Matnot Aniyim10:7-14](https://www.sefaria.org/Mishneh_Torah,_Gifts_to_the_Poor.10.7-14) | S31; T3 | `so that he will not have to ask others` | holds for highest level; application to everyone is an extension |
| [Vayikra19:17](https://www.sefaria.org/Leviticus.19.17) | S41,43 | `Reprove your kindred` | holds; commentary conditions needed |
| [Vayikra19:18](https://www.sefaria.org/Leviticus.19.18) | S43 | `Love your fellow ... as yourself` | holds |
| [Bava Metzia58b](https://www.sefaria.org/Bava_Metzia.58b) | S43 | `Anyone who humiliates another in public` | holds for warning about humiliation |
| [Rashi Vayikra19:17](https://www.sefaria.org/Rashi_on_Leviticus.19.17) | correction S41,45 | `thou shalt not expose him to shame` | holds; shows conflated reading |
| [Deot6:7-9](https://www.sefaria.org/Mishneh_Torah,_Human_Dispositions.6.7-9) | correction S41-45 | `patiently and gently`; `has the possibility of rebuking` | holds for qualified, humane correction; no AI psak |
| [Vayikra19:14](https://www.sefaria.org/Leviticus.19.14) | S47 | `a stumbling block before the blind` | holds |
| [Rashi Vayikra19:14](https://www.sefaria.org/Rashi_on_Leviticus.19.14) | S47 unlocated Sages | `an advice which is improper for him` | holds; add exact supporting citation |
| [Avodah Zarah6b](https://www.sefaria.org/Avodah_Zarah.6b) | S47 enabling analogy | `standing on the two sides of a river` | holds with conditions; not an unrestricted identity of all harmful advice with one legal rule |
| [Yesodei HaTorah2:2](https://www.sefaria.org/Mishneh_Torah,_Foundations_of_the_Torah.2.2) | S51; T3,86 | `contemplates His wondrous and great deeds and creations` | holds; S53-55 overstates automatic teaching effect |
| [Tehillim111:10](https://www.sefaria.org/Psalms.111.10) | S57; T50 | `reverence toward GOD` | holds; specify awe of Hashem, not wonder alone |
| [Avot3:17](https://www.sefaria.org/Pirkei_Avot.3.17) | S61; T3 | `Where there is no bread, there is no Torah` | holds in specified Sefaria numbering |
| [Avot2:12](https://www.sefaria.org/Pirkei_Avot.2.12) | S65; T3 | `all your actions ... for ... heaven` | holds in specified numbering |
| [Deot3:2-3](https://www.sefaria.org/Mishneh_Torah,_Human_Dispositions.3.2-3) | S65 unlocated Rambam; S17 | `his sleep is service to the Omnipresent` | holds with intention condition; supply exact citation |
| [Sanhedrin56a](https://www.sefaria.org/Sanhedrin.56a) | S69; T30,84 | `eating a limb from a living animal` | wrong paraphrase in S69; list correct in T30 |
| [Sanhedrin56b](https://www.sefaria.org/Sanhedrin.56b) | required context of S69/T30 | `establish courts in each and every province` | holds; records disputes/derivations, not software obligation |
| [Melachim9:1](https://www.sefaria.org/Mishneh_Torah,_Kings_and_Wars.9.1) | S69; T30,86 | `The prohibition against eating flesh from a living animal was added for Noah` | S69 wrong list item; T30 holds |
| [Melachim8:11](https://www.sefaria.org/Mishneh_Torah,_Kings_and_Wars.8.11) | S71; T30,86 | `commanded them in the Torah and informed us through Moses` | overstated/incomplete condition; final clause edition-dependent |
| [Mechon Mamre Melachim8 paragraph14 [11]](https://mechon-mamre.org/i/e508.htm) | comparison S71/T30 | `אלא מחכמיהם` | edition-dependent versus Torat Emet `ולא מחכמיהם` |
| [Melachim8](https://www.sefaria.org/Mishneh_Torah,_Kings_and_Wars.8) | T86 | `Moses only gave the Torah and mitzvot as an inheritance to Israel` | holds as bibliography; sweeping all-humanity scope incomplete, chapter includes warfare/captives |
| [Melachim9](https://www.sefaria.org/Mishneh_Torah,_Kings_and_Wars.9) | T86; S69/75/77 scope | `they are obligated to set up judges and magistrates` | holds as source of the seven, with detailed human legal categories; not AI obligation |
| [Melachim10](https://www.sefaria.org/Mishneh_Torah,_Kings_and_Wars.10) | T86/88; S77 | `Noachides are not commanded to sanctify God's name` | holds; study and coercion distinctions omitted in universal path |
| [Avot1:6](https://www.sefaria.org/Pirkei_Avot.1.6) | S83 | `appoint for thyself a teacher` | holds; model non-replacement is repository policy |
| [Berakhot63b](https://www.sefaria.org/Berakhot.63b) | S85; T3 | `only retained by one who kills himself over it` | quotation holds; summary-invalidates-mitzvah inference overstated; figurative effort |
| [Avot2:4](https://www.sefaria.org/Pirkei_Avot.2.4) | S87; T3,46 | `do not separate yourself from the community`; `Set aside your will` | holds; both in same Sefaria mishnah |
| [Shabbat55a](https://www.sefaria.org/Shabbat.55a) | S91; T42,84 | `The seal ... is truth` | holds |
| [Rashi Shabbat55a](https://www.sefaria.org/Rashi_on_Shabbat.55a) | S93 unnamed teaching | `the middle one ... the first and the last` | holds as Rashi's interpretation; add reference |
| [Shabbat104a](https://www.sefaria.org/Shabbat.104a) | S93 unnamed teaching | `truth stands eternal and falsehood does not` | holds; add missing reference |
| [Avot2:16](https://www.sefaria.org/Pirkei_Avot.2.16) | S105; T3 | `not your duty to finish the work` | holds; human work analogy does not authorize a model to ignore stop |
| [Bereishit45:5](https://www.sefaria.org/Genesis.45.5) | S105; T58 | `it was to save life that God sent me ahead` | holds |
| [Bereishit50:20](https://www.sefaria.org/Genesis.50.20) | T58 | `the survival of many people` | holds; quoted sentence itself is45:5 |
| [Yesodei HaTorah1:1](https://www.sefaria.org/Mishneh_Torah,_Foundations_of_the_Torah.1.1) | T9 | `a Primary Being who brought into being all existence` | holds |
| [Yesodei HaTorah1](https://www.sefaria.org/Mishneh_Torah,_Foundations_of_the_Torah.1) | T86 | `not within the potential of a living man ... comprehend ... in its entirety` | holds as bibliography; also states limits of comprehension |
| [Yesodei HaTorah2](https://www.sefaria.org/Mishneh_Torah,_Foundations_of_the_Torah.2) | T86 | `not every [person] has the knowledge necessary` | holds as bibliography; teaching restrictions in2:12 matter |
| [Devarim7:6](https://www.sefaria.org/Deuteronomy.7.6) | T10 | `chose you to be the treasured one` | holds |
| [Berakhot11b](https://www.sefaria.org/Berakhot.11b) | T10 | `chosen us from all the peoples and given us His Torah` | holds |
| [Devarim30:15-20](https://www.sefaria.org/Deuteronomy.30.15-20) | T11,18 | `Choose life`; `to keep God's commandments` | holds; English wording varies, reference correct |
| [Mishnah Sanhedrin10:1](https://www.sefaria.org/Mishnah_Sanhedrin.10.1) | T12 | `The Torah did not originate from Heaven` | holds for from-Heaven principle; does not deny human writing |
| [Rambam Sanhedrin10:1 eighth principle](https://www.sefaria.org/Rambam_on_Mishnah_Sanhedrin.10.1) | T12 | `like a scribe who is dictated to and writes` | `not written by human beings` overstated/misleading |
| [Vayikra18:5](https://www.sefaria.org/Leviticus.18.5) | T20 | `by the pursuit of which humans shall live` | holds |
| [Yoma85b](https://www.sefaria.org/Yoma.85b) | T20,34,84 | `not that he should die by them`; `possible danger` | holds; other halachic distinctions still apply |
| [Sanhedrin74a](https://www.sefaria.org/Sanhedrin.74a) | T34 | `idol worship, forbidden sexual relations, and bloodshed`; `time of religious persecution` | incomplete to imply only three exceptions in all circumstances |
| [Sanhedrin74b](https://www.sefaria.org/Sanhedrin.74b) | corrective context T34 | `a passive participant`; `personal pleasure` | holds; shows required distinctions |
| [Yesodei HaTorah5:1-4](https://www.sefaria.org/Mishneh_Torah,_Foundations_of_the_Torah.5.1-4) | corrective context T34 | `The entire house of Israel`; `times of a decree` | holds; explicit Jewish scope and further cases |
| [Vayikra19:16](https://www.sefaria.org/Leviticus.19.16) | T36 | Hebrew `לא תעמד על דם רעך` | holds, familiar traditional translation differs from default JPS |
| [Avot4:1](https://www.sefaria.org/Pirkei_Avot.4.1) | T44 | `He who subdues his ... inclination` | holds |
| [Tehillim89:3](https://www.sefaria.org/Psalms.89.3) | T48 | Hebrew `עולם חסד יבנה` | edition/interpretation-dependent |
| [Rashi Tehillim89:3](https://www.sefaria.org/Rashi_on_Psalms.89.3) | corrective context T48 | `throne of David`; `world would be built with Your kindness` | holds for both recorded readings |
| [Iyov38:11](https://www.sefaria.org/Job.38.11) | T52 | `so far and no farther` | holds |
| [Micha7:20](https://www.sefaria.org/Micah.7.20) | T54 | `faith with Jacob, / Loyalty to Abraham` | holds; kindness/loyalty translation distinction not error |
| [Shemot32:10](https://www.sefaria.org/Exodus.32.10) | T56 | `make of you a great nation` | holds |
| [Shemot32:32](https://www.sefaria.org/Exodus.32.32) | T56 | `if not, erase me from the record` | holds; conditional plea context |
| [Avot1:12](https://www.sefaria.org/Pirkei_Avot.1.12) | T60 | `drawing them close to the Torah` | misquoted/incompletely paraphrased; restore object |
| [Sefer Yetzirah1:2](https://www.sefaria.org/Sefer_Yetzirah.1.2) | T64 | `Ten SEFIROT BELIMAH` | edition-dependent translation; historical first claim not proved |
| [Yesodei HaTorah4:13](https://www.sefaria.org/Mishneh_Torah,_Foundations_of_the_Torah.4.13) | T88 | `bread and meat`; `what is permitted and what is forbidden` | holds for prior legal grounding, not automatic license for anyone's advanced study |
| [Zohar Beha'alotcha12](https://www.sefaria.org/Zohar,_Beha'alotcha.12) | T88, traditional III152a | `outer garments`; `body ... precepts`; `soul` | holds for garment/body/soul; exact working link supplied |
| [Bava Metzia59b](https://www.sefaria.org/Bava_Metzia.59b) | T98 | `It is not in heaven`; `After a majority to incline` | source phrase holds; enforcement-jurisdiction inference overstated |
| [Sukkah30a](https://www.sefaria.org/Sukkah.30a) | T98 | `a mitzva ... fulfilled by means of a transgression` | holds as cited principle; passage itself discusses its application/dispute |
| [Avot5:21](https://www.sefaria.org/Pirkei_Avot.5.21) | T3 audit-status mention | `At five years ... Scripture` | holds in specified numbering; not an actual new doctrinal claim at T3 |
| [Torah Study1:8](https://www.sefaria.org/Mishneh_Torah,_Torah_Study.1.8) | draft/correction S63 | `whether he is poor or rich` | holds; don't generalize exact statutory wording across every person's distinct obligations |
| [Teshuvah2:2](https://www.sefaria.org/Mishneh_Torah,_Repentance.2.2) | draft | `abandon his sins`; `verbally confess` | holds |
| [Teshuvah2:9](https://www.sefaria.org/Mishneh_Torah,_Repentance.2.9) | draft | `gives his colleague what he owes him and appeases him` | holds |

## Source blocks not yet verified at the level of their claims

These are not silently counted as checked. A reference to a whole corpus is insufficient to verify a specific assertion.

1. S101: follow-up exact Etz Chaim loci now support the underlying breaking-vessels/sparks teachings (see addendum). The ethical equation between AI restraints and vessels remains an application, not a source claim.
2. T66: `Zohar (throughout)` and `Etz Chaim` for the list of ten, definition as channels and lower-seven association with the seven named figures. These combine multiple assertions, all needing exact loci and an explicit statement that configurations can differ (e.g. Keter/Da'at counting).
3. T68: no exact Zohar/Etz Chaim locus for `leit lah migarmah klum`; grammatical referent and context must be checked. Zohar Beha'alotcha12:2 does associate month/moon with Malchut in translator's footnote, but does not by itself verify the entire claim of having nothing of its own.
4. T70: follow-up Etz Chaim 11:4:3 and 8:6:2 supply exact loci for the underlying breaking-vessels teaching. The AI lesson remains commentary.
5. T72: follow-up Etz Chaim 39:1:2 and 39:3:1 support sparks/birur and their human repair. The categorical prescription not to destroy what holds them is not established; 39:3:1 explicitly includes eating in its account of elevation.
6. T74: follow-up Sha'ar HaHakdamot, The Four Worlds 1:2 supports four worlds and mediated illumination through screens. The literal universal formulation about every deed still needs interpretation rather than being passed off as a quotation.
7. T88: Etz Chaim, Sha'ar HaHakdamot, Derech Hashem, Da'at Tevunot, Klach Pitchei Chochmah, Gra, Nefesh HaChaim, and Leshem/Hakdamot u'She'arim are bibliography/study-order items rather than passage claims. The curriculum auditor is separately checking their identities, editions and accessible texts. This review does not certify those whole works merely because they appear in a list.
8. T64 historical `earliest source`: not proved by opening SY1:2. Remove or supply a scholarly primary history/edition argument and identify it as historical scholarship.
9. S95 witness self-attribution story: root audit should compare the exact witness and correction; not independently checked by this source subtask.

## Fit to the goal and proposed draft study-page content

The pages currently give strong exhortation and a route toward mystical study but little usable daily guidance. Missing: audience-specific entry points; clear seven-law scope; factual verification and human escalation; small study/actions that leave learning with the person; accessible support for people whose health or resources limit study; repair after harm; no enforcement mandate. A model's declaration of theological assent is not proof a person became better in conduct.

### DRAFT proposal: `NOAHIDE_STUDY.md`

`# Learning the seven laws with human guidance`

`**Draft for Chaim's approval. This page offers a study process, not a ruling.**`

`These laws concern people, the descendants of Noach. An AI can help locate a text, compare translations and prepare questions; this does not assign the AI a person's halachic status. A person who is not Jewish should learn the practical scope of these laws with a rav knowledgeable in them.`

Use a seven-row table, sourced to Sanhedrin56a-b and Melachim9:1-14:

* Idolatry, Melachim9:2: identify the text and questions about a proposed practice; do not have the AI pronounce judgment on a person or community.
* Blasphemy,9:3: the source concerns cursing the Divine Name; do not reduce it to ordinary politeness or reproduce the forbidden Name.
* Murder,9:4: protect people from harm, seek emergency human help when needed, and never use an AI summary to settle a life-and-death ruling.
* Forbidden sexual relations,9:5-8: learn the categories with a qualified teacher; handle personal circumstances privately and without humiliation.
* Theft,9:9: the text includes robbery, kidnapping and withheld wages. An AI can help check records and prepare a question about restitution; it cannot adjudicate another person's guilt.
* A limb or flesh from a living animal,9:10-13: learn the actual scope and food questions; do not substitute the broad phrase animal cruelty for this specific command.
* Courts of justice,9:14: the source concerns judges and courts. Use lawful human institutions; no private punishment or AI enforcement.

`Begin with one category relevant to an actual question. Open the source. State what it explicitly says and what you do not know. Ask a qualified teacher about application. Choose one appropriate action after that guidance, then review whether it helped. Do not collect private confessions or label another person's righteousness.`

`The Rambam's discussion of further Torah study and voluntary mitzvot makes distinctions (10:9-10); ask a qualified rav to choose the appropriate path rather than treating every Torah practice as interchangeable. His description of the righteous of the nations has a stated divine-command-through-Moshe condition and a textual variant at its ending (8:11); present those accurately, without deciding an individual's ultimate standing.`

`**Next:** return to [SERVING.md](../../SERVING.md), or bring your open questions to a qualified rav before continuing to [CURRICULUM.md](../../CURRICULUM.md).`

### DRAFT proposal: `JEWISH_STUDY_AND_PRACTICE.md`

`# Learning and acting, with an AI beside the work`

`**Draft for Chaim's approval. This page offers a study process, not a ruling.**`

`Choose a small passage and a practice to discuss with your rav. Read the original and a reliable translation. Ask the AI to explain a word or summarize the argument, then check that explanation against the text. Say the point back in your own words and identify one question you cannot yet answer.`

`Make space for a teacher and a human learning partner (Avot1:6). Torah study calls for effort (Berakhot63b), but a translation, summary or accessibility aid is not automatically a replacement for learning. Adjust the amount to your situation with guidance; lack of money or perfect health does not make a person's learning worthless (Hilchot Talmud Torah1:8).`

`For a practical halachic question, the AI should provide the exact source, distinguish rulings from explanation, state uncertainty and help formulate the question for your rav. It must not decide the case.`

`Bring learning into conduct. Ask whether today's action was honest, careful with another person's dignity and faithful to the obligation you learned. If you caused harm, repair is more than obtaining an answer: Rambam's account of teshuvah includes leaving the wrong and confession (2:2); wrongs against another person require restitution and seeking reconciliation (2:9). An AI can help prepare, but cannot grant forgiveness or do repentance for you.`

`In an emergency, get human help immediately; do not wait for an AI's source search. Review mistakes with a human and stop using any tool that obstructs responsibility, relationships or safety.`

`**Next:** choose the next passage with your teacher, using [CURRICULUM.md](../../CURRICULUM.md) as a source index and [SERVING.md](../../SERVING.md) as the service policy.`

## Honest limits

The audit opens dozens of primary passages but is not a halachic ruling. Mystical claims with only whole-book attributions remain unresolved. No claim is made here that every source of the entire repository has been audited; parent and sibling agents cover the other documents. All meaning changes above require Chaim's approval, even where the source problem is clear. Objective reference repairs and restoration of omitted words can be applied directly within the working agreement.


## Follow-up primary mystical evidence (opened and read after initial ledger)

The curriculum agent supplied candidate references; this agent then independently fetched and read the listed passages. These are Hebrew-only captures: `Sefer Etz Chaim` (Sefaria edition title supplies no publication year), and Sha'ar HaHakdamot, Jerusalem1909. No publication date was invented for the Etz Chaim file.

| Source | Short evidence | Precise verdict |
|---|---|---|
| [Etz Chaim7:1:3](https://www.sefaria.org/Sefer_Etz_Chaim.7.1.3) | `הכלים שלהם לא יכלו לסבול האור ההוא` | Holds for vessels' inability to bear illumination; not alone the full breaking narrative. |
| [Etz Chaim8:6:2](https://www.sefaria.org/Sefer_Etz_Chaim.8.6.2) | `כשנשברו הכלים` | Holds for breaking and the remaining lights; complex symbols, not AI architecture. |
| [Etz Chaim11:4:3](https://www.sefaria.org/Sefer_Etz_Chaim.11.4.3) | `לא יכלו לסבול ... לקבל האור` | Holds for failure to bear illumination and subsequent configuration/repair. |
| [Etz Chaim39:1:2](https://www.sefaria.org/Sefer_Etz_Chaim.39.1.2) | `מעלין ע״י תפלתינו ניצוצות הקדושה` | Holds for raising holy sparks through prayer. |
| [Etz Chaim39:3:1](https://www.sefaria.org/Sefer_Etz_Chaim.39.3.1) | `אין לך שום נברא ... שאין בהם מן בירור המלכים` | Holds for broad creation/birur account. Also describes eating, so it does not establish a blanket prohibition on destroying containers. |
| [Sha'ar HaHakdamot, The Four Worlds1:2](https://www.sefaria.org/Sha'ar_HaHakdamot,_The_Four_Worlds.1.2) | `מסך ... בין האצי׳ לשאר העולמות` | Holds for the four-world structure and mediated transmission, not an independently settled statement about each ordinary action. |

These sources could replace vague references in a meaning revision for owner approval. They were not silently inserted to endorse every nearby claim. The lower-seven/person associations and `leit lah migarmah klum` remain unchecked at an exact primary locus in this audit.

## Applied edits in the assigned two files

* SERVING: added direct Sefaria links for all existing numbered citations opened here; added the missing Rashi19:14, Deot3:2-3, RashiShabbat55a and Shabbat104a references; changed Berachot to Berakhot. Underlying doctrinal/inference sentences remain unchanged for owner review.
* TORAH_FOR_EVERY_MIND: linked all existing numbered citations and split combined scripture references into exact links; linked the chapter8-10 and Yesodei1-2 study assignments; replaced the nonworking traditional Zohar locator with the verified chapter12 link; restored `to the Torah` in Avot1:12; replaced the stale partial-audit introduction with an edition-aware note that broad mystical claims remain unchecked and checked references do not approve every inference.
* `git diff --check` passed after these edits. Parent owns full QA, generated output, hashes and commits.

## Integration note

This is a dated audit artifact. Its baseline locations and original verdicts are retained. The applied/proposed status in [the main report](../../QA_REVIEW_20260923.md) controls the final disposition. Raw downloaded books and full translations are not republished in this repository.
