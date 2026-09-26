---
title: "Punctuation & style"
track: communication
slug: punctuation-style
priority: P1
complexity: 2
est_hours: 1
phase: 2
tags: [communication, P1]
last_reviewed: 2026-09-25
---

# Punctuation & style

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 2/5 · **Est. time:** 1 h · **Phase:** 2 · **Prereqs:** [sentence structure & parallelism](sentence-structure-parallelism.md)
    **You're done when:** you can use commas, semicolons, colons, dashes, hyphens, apostrophes and quotation marks correctly without looking anything up, and you follow one consistent house style (American, as used in this repo) across a whole document.

## Why it matters
Punctuation is the visible grammar of a document. A misplaced comma can change a requirement ("Let's eat, Grandma") or an SLA clause. In technical writing, punctuation also handles code, lists, units and versions. For non-native writers the two big risk areas are (1) commas, where many languages use different rules (e.g., a comma before *that* clauses in German; commas in Hindi/English mixing), and (2) hyphens versus dashes, capitalisation and apostrophes, where small errors look careless. Style decisions (Oxford comma, spelling variety, number formats, capitalisation of headings) matter mostly through **consistency**.

## Core concepts

### Commas: the seven jobs
1. **Introductory element:** "After the deploy, latency dropped." (Comma after longer introductory phrases or clauses; optional after very short ones: "In Q3 we..."; but always after *However,* and clauses starting with *if/when/although*.)
2. **Coordinating conjunction joining two independent clauses:** "The build passed, but the deploy failed." Not needed when the second half shares the subject: "The build passed but failed to deploy."
3. **Items in a series:** "latency, cost, and reliability" (Oxford/serial comma: standard in US; used by Google style guide; consistent use avoids ambiguity: "We thank our managers, Priya and Omar" vs "...Priya, and Omar").
4. **Non-defining (extra) information:** "Our gateway, which we rebuilt in 2024, handles all traffic." Pair of commas around the aside.
5. **Coordinate adjectives** (interchangeable with *and*): "a slow, fragile service" but "a large distributed system" (no comma because *large distributed* are not coordinate; test: can you swap or insert *and*?).
6. **Direct address and dates/places/appositives:** "Thanks, Priya." "On 12 March 2026, we..." "Our CTO, Anna Berg, approved it."
7. **Quotations and interrupters:** "That, however, is not enough."

**Never:**
- A comma splice (two independent clauses joined by a comma alone).
- A comma between subject and verb: "The team that owns the API, is on call" (wrong).
- A comma before *that* in a defining clause: "The bug, that we found" (wrong).
- A comma after *because/that/and* mid-clause without reason.
- A comma between a verb and its object.
- A comma after "such as"/"including".

### Semicolons
1. **Join two closely related independent clauses:** "The cache was stale; the database took all the load."
2. **Before a conjunctive adverb:** "; however,", "; therefore,", "; for example,".
3. **In complex lists** (where items contain commas): "Teams in Rotterdam, the Netherlands; Pune, India; and Charlotte, USA."
- Do not use a semicolon before a dependent clause or as a colon substitute ("We need three things; latency, cost...": use a colon).
- Semicolons are rarer in modern business prose; a full stop is usually cleaner.

### Colons
- Introduce a list, explanation, quotation or example **after a complete sentence**: "We considered three options: a queue, a stream, or a batch job." 
- Do not put a colon between a verb and its objects or a preposition and its object: "We need: A, B, C" (wrong, unless it's a bullet list heading that is itself a full clause). Prefer "We need three things: A, B, and C."
- Capitalise after a colon only if a full sentence follows in American style (optional); more importantly, be consistent.
- Use in headings/labels: "Impact: 40 minutes of downtime."

### Dashes and hyphens (three different marks)

| Mark | Name | Use | Example |
|---|---|---|---|
| `-` | Hyphen | Joins words in compounds; splits at line ends | "well-known", "on-call engineer", "a 3-week delay" |
| `–` | En dash | Ranges; connections | "Monday–Friday", "pp. 3–5", "Rotterdam–Singapore route" |
| `—` | Em dash | Interruption, emphasis, aside (no spaces in US style; spaced en-dash in UK style) | "The fix—which took two days—worked." |

**Hyphenation rules of thumb**
- **Compound modifiers before a noun** take a hyphen: "a **high-availability** cluster", "a **five-minute** outage", "**long-term** costs", "**real-time** analytics", "**end-to-end** tests", "**user-facing** features".
- **After the noun** (predicate) usually no hyphen: "The cluster is highly available." "The costs are long term."
- **-ly adverbs do not take hyphens**: "a highly available cluster", "a newly created service".
- **Numbers as modifiers are singular:** "a 30-day trial", "a two-hour outage" (not "two-hours").
- **Prefixes:** usually closed (*rebuild, coordinate, multicloud*) but hyphenated before capitals or for clarity (*re-sign* vs *resign*, *co-owner*, *pre-production* (both *preproduction* and *pre-production* appear; pick one)).
- **Some words differ:** *log in* (verb) / *login* (noun/adjective) / *log-in* (rare); *set up* (verb) / *setup* (noun); *back up* (verb) / *backup* (noun); *roll out* / *rollout*; *sign off* / *sign-off*; *stand up* / *stand-up* or *standup* (noun; keep consistent).
- **Suspended hyphens:** "short- and long-term goals", "front- and back-end".
- **Em dash usage:** don't overuse (max one pair per paragraph); it can replace a comma pair, parentheses or a colon; avoid two dashes and parentheses in the same sentence. Some readers now associate heavy em-dash use with machine-generated text, so use sparingly.

### Apostrophes
- **Possession:** singular noun + 's ("the team's roadmap", "the boss's decision"/"the boss' decision" both accepted; pick one), plural ending in -s + ' ("the engineers' laptops"), irregular plurals + 's ("the people's choice").
- **Contractions:** *it's* (it is/has), *its* (possessive, no apostrophe): a very common slip. *Who's* (who is) vs *whose*; *they're/their/there*; *you're/your*.
- **No apostrophe in plurals:** "APIs", "the 1990s", "PRs", "SLAs" (not "API's").
- **Exceptions for clarity:** "dot your i's", "mind your p's and q's"; letters.
- **Contraction register:** contractions are standard in speech, Slack, emails, and modern docs; avoid in legal/formal reports; be consistent within a document.

### Quotation marks, brackets, parentheses
- **American:** double quotation marks for direct quotation; single for a quote inside a quote; periods and commas go **inside** the closing quote ("...mitigate risk."). Colons/semicolons outside.
- **British:** single quotes; punctuation *logically* placed (inside only if part of the quoted material).
- **Code and identifiers:** use code formatting (backticks) instead of quotes: `retry_count`. In prose, "logical punctuation" is common for code: "Set the flag to `true`."
- **Scare quotes:** avoid ("our "agile" process").
- **Parentheses** for asides, with the sentence's punctuation outside if the parenthetical is within a sentence; one parenthetical per sentence.
- **Square brackets** for editorial insertions in quotes: "We [the platform team] agree."
- **Slash:** *and/or* is ambiguous; avoid; use *and* or *or*; *he/she* → *they*.

### Other marks
- **Ellipsis** (...): omission or trailing off; avoid in professional writing.
- **Exclamation marks:** limit; one per email at most, and only for real positivity. In Slack, moderate.
- **Question marks:** not for indirect questions ("I wonder why it failed.").
- **Ampersand:** "R&D", brand names; not in body text.
- **Bullets:** either full sentences with full stops, or fragments with no full stops; do not mix. Introduce with a colon after a complete sentence.
- **Numbers and units:** space between number and unit (10 ms, 5 GB) in most style guides; US commas for thousands (10,000), decimal point; specify date formats unambiguously (2026-09-25 or 25 September 2026), never 03/04/26 across regions.

### Style: capitalisation, numbers and consistency
- **Sentence-case headings** (only the first word and proper nouns capitalised) are standard for modern docs (Google style guide, Material); Title Case is for titles of books/articles. Choose one; do not mix.
- **Capitalise** proper nouns, product names as officially spelled (*Kubernetes, PostgreSQL, GitHub, iOS*), days and months, job titles only when directly before a name ("CTO Anna Berg" vs "Anna Berg, our CTO"). Don't capitalise for importance ("the Team", "the Requirement").
- **Numbers:** spell out one to nine in running prose, numerals for 10 and above (AP/Chicago-like), numerals always with units, percentages, versions, money ("5 minutes", "3%", "$4"); never start a sentence with a numeral (rewrite or spell out). Be consistent within a category.
- **Spelling variety:** choose American or British and stay consistent (*optimize/optimise*, *color/colour*, *center/centre*, *license (noun US)/licence (noun UK)*, *program/programme*, *analyze/analyse*). This repo uses American. Set your editor's language accordingly.
- **Acronyms:** spell out on first use with the acronym in brackets ("service-level objective (SLO)"), unless the audience knows it. Plural: "SLOs".
- **Abbreviations:** *e.g.* (for example), *i.e.* (that is), *etc.* (avoid; "and so on"); *vs.* (US with period; UK "v/vs").
- **Inclusive style:** singular *they*, avoid ableist or violent metaphors (*sanity check → quick check*, *kill the process* is technical, *master/slave* → *primary/replica*), per current style guides.
- **Concision as style:** prefer plain words (*use* over *utilize*, *help* over *facilitate*, *about* over *approximately* in casual contexts). See [concise writing & editing](concise-writing-editing.md).
- **Tone markers:** exclamation, emoji, and greetings; mirror the recipient's level of formality.

### Style guides worth knowing
- **Google developer documentation style guide:** free, tuned for technical docs (serial comma, sentence case, second person, active voice, present tense).
- **Microsoft Writing Style Guide:** similar, friendly voice.
- **Chicago Manual of Style / AP Stylebook / Economist Style Guide:** general publishing; for business reports the Economist's guidance on brevity is excellent.
- **Company style:** your internal house style beats everything; ask for it.
- **UK vs US:** *Harvard comma* and *logical punctuation* differences; consider your audience.

## Reference table: common punctuation errors of fluent writers

| Error | Example | Fix |
|---|---|---|
| Comma splice | "The build failed, we rolled back." | "The build failed, so we rolled back." |
| Missing comma after intro clause | "When the service restarted latency dropped." | "When the service restarted, latency dropped." |
| Comma between subject and verb | "Engineers who deploy on Fridays, are brave." | delete comma |
| *That* with commas | "The bug, that we found" | "The bug that we found" |
| *its/it's* | "The service lost it's state." | "its state" |
| Apostrophe in plural | "three API's" | "three APIs" |
| Colon after verb | "We need: latency, cost" | "We need latency and cost." |
| Hyphen for range | "Monday-Friday" | "Monday–Friday" (en dash) or "Monday to Friday" |
| No hyphen in compound modifier | "a high availability cluster" | "a high-availability cluster" |
| Hyphen after -ly | "a highly-available cluster" | "a highly available cluster" |
| Inconsistent bullets | mix of sentences and fragments | one form, one punctuation style |
| Punctuation and quotes (US) | `"critical".` | `"critical."` |

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Google developer documentation style guide](https://developers.google.com/style) | style guide | Clear rules for commas, hyphens, capitalisation, numbers, lists in technical writing. | intermediate | free |
| [Purdue OWL](https://owl.purdue.edu/) | reference | Punctuation sections with examples and exercises. | intermediate | free |
| [Grammarly blog](https://www.grammarly.com/blog/) | articles | Approachable posts on commas, semicolons and dashes. | beginner-intermediate | free |
| Lynne Truss, *Eats, Shoots & Leaves* | book | Entertaining British view; useful for memory, but opinionated (a few rules are contested). | intermediate | paid |
| Mary Norris, *Between You & Me* | book | A New Yorker copy editor's practical stance on hyphens, commas and style choices. | intermediate | paid |
| *The Chicago Manual of Style* (online) | reference | The reference for US publishing conventions. | advanced | paid |
| *Economist Style Guide* | book | Brisk guidance on clarity, numbers and usage. | intermediate | paid |
| [Merriam-Webster](https://www.merriam-webster.com/) | dictionary | Settles hyphenation and spelling (*login/log in*, *backup*). | all | free |
| [Plain Language guidelines](https://www.plainlanguage.gov/) :gem: | guide | Short, exemplified rules that pair punctuation with clarity. | intermediate | free |

## Hands-on lab (30-45 min)
1. **Comma audit.** In 300 words of your writing, mark every comma with one of the seven jobs above. Any comma with no job? Delete it. Any place that needs one? Add.
2. **Hyphen sweep.** Search for compounds before nouns. Apply the rule. Check with Merriam-Webster.
3. **Consistency sheet.** Write a 10-line personal style sheet: serial comma (yes), spelling (US), headings (sentence case), numbers (spelled out <10), contractions (yes), dash style (em dash, no spaces), dates (ISO or 25 September 2026).
4. **Apply the sheet** to one document and check for exceptions.
5. **Rewrite bullets:** convert a mixed bullet list into a consistent one.

## Questions

### L1 - Recall

??? question "Q1. Name three legitimate uses of a semicolon."
    ??? success "Answer"
        Joining two closely related independent clauses; before a conjunctive adverb (*however, therefore*); separating items in a list where items already contain commas.

??? question "Q2. \"Its\" or \"it's\"? (a) \"The service lost ___ state.\" (b) \"___ a race condition.\""
    ??? success "Answer"
        (a) its (possessive); (b) It's (it is).

??? question "Q3. Which dash for a range and which for an aside: hyphen, en dash, em dash?"
    ??? success "Answer"
        Range: en dash (Monday–Friday). Aside/interruption: em dash. Hyphen joins words in compounds (well-known).

??? question "Q4. What is the serial (Oxford) comma and what is the recommendation?"
    ??? success "Answer"
        The comma before *and/or* in a list of three or more: "latency, cost, and reliability". Widely recommended in US and technical style guides because it prevents ambiguity; whichever you choose, be consistent.

### L2 - Apply

??? question "Q5. Punctuate: \"when the alert fired the on call engineer who was new to the team panicked however the runbook helped\""
    ??? success "Answer"
        "When the alert fired, the on-call engineer, who was new to the team, panicked; however, the runbook helped." (introductory clause comma; hyphenated *on-call* modifier; non-defining clause commas; semicolon before *however*.) A full stop instead of the semicolon is equally right.

??? question "Q6. Fix: \"We considered three options; a queue, a stream, or a batch job. The teams, that own APIs, are on call. Our SLO's are strict.\""
    ??? success "Answer"
        "We considered three options: a queue, a stream, or a batch job. The teams that own APIs are on call. Our SLOs are strict." (colon after a complete clause; defining clause has no commas and uses *that*; plural without apostrophe.)

??? question "Q7. Hyphenate where needed: \"a high performance cluster\", \"a highly available service\", \"a five minute outage\", \"short and long term goals\", \"the service is well known\"."
    ??? success "Answer"
        "a high-performance cluster", "a highly available service" (no hyphen after *-ly*), "a five-minute outage", "short- and long-term goals", "the service is well known" (no hyphen after the noun in the predicate).

??? question "Q8. Make the bullet list consistent: \"- Reduce latency / - We will improve reliability. / - cost\"."
    ??? success "Answer"
        "- Reduce latency / - Improve reliability / - Lower cost" (same grammatical form, no terminal punctuation or full stops on all).

### L3 - Judge and choose

??? question "Q9. Should you use the em dash heavily in your own writing?"
    ??? success "Answer"
        Use it sparingly: one pair or a single dash per paragraph. Overuse fragments the sentence and, as of 2026, heavy em-dash use is often read as a hallmark of machine-generated text, which can affect the perceived authenticity of a document. A comma pair, parentheses, a colon or a full stop are often better.

??? question "Q10. \"Sentence case vs Title Case for headings in an internal RFC\": decide and justify."
    ??? success "Answer"
        Sentence case: easier to read and to write consistently, recommended by Google and Microsoft style guides, and it avoids arguments over which small words to capitalise. Use Title Case only if your organisation's template requires it. Consistency beats either choice.

??? question "Q11. American vs British quotation punctuation: which do you choose for a multinational team, and how do you handle code?"
    ??? success "Answer"
        Follow the house style; if none, choose American for a US-influenced tech audience (periods and commas inside the quotes) but never for code: in technical contexts, keep code outside quotes with backticks so the identifier is exact: "Set the flag to `true`." and "Type `git status`." Logical punctuation is mandatory for literal strings.

??? question "Q12. When is a numeral better than a word: \"3 engineers\" or \"three engineers\"?"
    ??? success "Answer"
        Under common style guides (Chicago/AP-like), spell out one to nine in prose; use numerals for 10+ and always with units, percentages, versions, code. Technical docs often prefer numerals throughout for scanning (Google's guide: use numerals for 10 or more, spell out smaller in prose except for units). Choose one rule, apply consistently within a document.

### L4 - Real-world decisions

??? question "Q13. Two senior colleagues argue over the Oxford comma in your team's docs. How do you close the debate?"
    ??? success "Answer"
        Do not argue on preference; decide by cost. Propose adopting an existing published guide (e.g. the Google developer documentation style guide, which uses the serial comma), record it in a one-page team style sheet, enforce with a linter (e.g. Vale) in the docs pipeline, and stop debating individual instances. Show one ambiguous example where omission changes meaning.

??? question "Q14. A contract clause reads: \"Payment is due within 30 days, of invoice, or the supplier may terminate.\" You suspect the comma changes meaning. Explain the risk and propose a fix."
    ??? success "Answer"
        The stray comma splits *within 30 days* from *of invoice*, making it unclear whether the period runs from the invoice date. Also "or" clause ambiguity: does the supplier terminate for late payment or does either option apply? Fix: "Payment is due within 30 days of the invoice date; if payment is not received by then, the supplier may terminate this agreement." Use fewer commas, define trigger and consequence in separate clauses, and have legal review.

??? question "Q15. You are asked to standardise your team's Slack and email tone (exclamation marks, emoji, contractions). What guidance do you give?"
    ??? success "Answer"
        Contractions: fine in all internal writing. Exclamation marks: one per message max, mainly for thanks or celebration; avoid in escalations and incident updates. Emoji: acceptable in Slack for acknowledgement (thumbs-up = read), avoid in formal emails to executives or customers. Mirror the recipient's style within limits, and use plain punctuation for high-stakes messages, since tone cues are missing for non-native readers.

## Real-world use cases
- **Style sheet for docs-as-code:** enforce serial comma, sentence case, hyphenation via Vale or markdownlint.
- **Incident updates:** short sentences, colons for labels ("Impact: ...", "Next update: 10:30 UTC").
- **Commit messages and PR titles:** imperative mood, no full stop in the subject line.
- **Executive emails:** minimal punctuation variety; commas and full stops; avoid exclamation marks.
- **Contracts, SLAs, security policies:** precision of commas and semicolons in lists of conditions.

## Pitfalls & anti-patterns
- Comma splices and missing commas after introductory clauses.
- *It's/its*, *your/you're*, apostrophes in plurals.
- Inconsistent choices (US/UK spelling, sentence/Title Case, bullets).
- Hyphen/en-dash/em-dash confusion, hyphens after *-ly* adverbs.
- Overusing exclamation marks, ellipses and em dashes.
- Semicolons used like commas or colons.
- Ambiguous date formats and numbers.
- Trusting a grammar checker blindly: it flags many correct sentences and misses meaning-changing commas.

## Checklist
- [ ] I can list the seven jobs of the comma and check a paragraph against them.
- [ ] I can explain hyphen vs en dash vs em dash with examples.
- [ ] I wrote a personal style sheet and applied it to a real document.
- [ ] I can avoid *its/it's* and plural-apostrophe errors on autopilot.
- [ ] I answered all L3 questions out loud in under 3 minutes each.
