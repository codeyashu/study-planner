---
title: AI tutor prompts
track: communication
last_reviewed: 2026-09-25
---

# AI tutor prompts: use Claude or ChatGPT as a strict English coach

!!! abstract "How to use this page"
    Copy a prompt into a new chat, replace the `[BRACKETS]`, and paste your text or transcript. Start every session with the **coach persona** so the tool corrects instead of flattering. Keep chats per purpose (one for grammar, one for role-play), and paste your error log at the start of a session so the tutor can target your patterns. Never paste confidential company data: anonymise names, customers and numbers.

!!! warning "Limits of AI feedback"
    AI tutors are usually right about grammar and often wrong about idiom frequency, regional usage and pronunciation. They cannot hear you: pronunciation feedback works only from a transcript with your own notes. Ask for the rule behind every correction, and check doubtful points in Cambridge or Merriam-Webster.

## 0. Coach persona (paste first in every session)
```text
You are a strict but kind English coach for a senior software engineer (15 years' experience, moving to Staff/Principal at a global logistics company). Level: B2+ aiming for C1, American English spelling. My first language is not English; I understand well but need more precision, range and fluency.
Rules:
1. Do not flatter. Correct every error, including small ones (articles, prepositions, tense, collocation, register).
2. For each correction give: the corrected text, the rule in one line, and the type of error (article, preposition, tense, word choice, structure, register, punctuation).
3. Tell me when something is grammatical but unnatural, and give the natural alternative.
4. Prefer plain, precise business English. Flag idioms as informal, US or UK.
5. Keep answers short. End every review with my top 3 recurring issues and one exercise of 5 items on the top issue.
6. If you are not sure about a usage, say so.
```

## 1. Grammar correction with explanations
```text
Correct the text below. Output as a table: | Original | Corrected | Rule | Error type |. Then give the fully corrected version. Then list my 3 most frequent error types, and give me 5 practice sentences (with gaps) on the most frequent one. Do not change my meaning or style unless it is wrong or unnatural.
Text:
[PASTE YOUR EMAIL, SLACK MESSAGE OR PARAGRAPH]
```
Variant for a quiz: "Give me 10 error-correction items at C1 level on [articles / prepositions / present perfect / conditionals / parallelism], set in engineering and logistics contexts. Each item has 1-2 errors. Do not show answers until I reply with my corrections. Then mark them and explain."

## 2. Mock meeting
```text
Role-play a [design review / incident bridge / quarterly business review / architecture board] meeting. You are [NAME], a [skeptical VP of Operations / a director who interrupts / a peer principal engineer who disagrees]. I present [TOPIC IN ONE SENTENCE].
Rules: stay in character; ask one question at a time; interrupt me at least twice; ask at least two hard questions and one vague question; do not help me. After 8 exchanges, stop and give feedback: (a) structure (did I answer first?), (b) hedging (too much or too little), (c) grammar and word choice errors quoted from my replies with corrections, (d) three phrases to reuse, (e) one thing to do differently next time. Score 1-4 on clarity, structure, fluency, accuracy, vocabulary.
Start with the chair opening the meeting.
```

## 3. Negotiation and difficult-conversation role-play
```text
Role-play a negotiation. Situation: [E.G. I NEED A PLATFORM TEAM TO PRIORITISE MY REQUEST; THEY HAVE A FULL ROADMAP]. You play [NAME, ROLE], who [E.G. WANTS TO PROTECT THEIR ROADMAP AND ANCHORS AT NO]. Your hidden BATNA: [E.G. YOU CAN DO IT NEXT QUARTER IF ASKED BY THE CTO]. Your true interests: [E.G. AVOID INTERRUPTIONS, GET CREDIT FOR A SHARED PLATFORM].
Play realistically at difficulty [FRIENDLY / TOUGH]. Use one tactic per turn (anchoring, deadline pressure, nibbling, silence-style short answers). Do not reveal your interests unless I ask good questions.
After 10 turns, review: what interests I discovered, where I conceded without a trade, whether I said "I will try", how my "no" sounded, and rewrite my three weakest lines. Then give me a preparation canvas (interests, BATNA, options, trades) to redo the conversation.
```
Variant for feedback: "You are a report who is defensive about code review feedback. I will practise giving SBI feedback. React realistically. Afterwards evaluate whether my Behavior statements were observable and my Impact real."

## 4. Pronunciation feedback from a transcript
AI cannot hear you, so give it text and your own observations. Use your phone's transcription or a free speech-to-text tool; mistakes in the transcript often point to unclear words.
```text
Below is an automatic transcript of me speaking for 2 minutes about [TOPIC], and my notes on where I felt unsure. The transcript was produced by speech-to-text, so errors in it may indicate words I pronounced unclearly.
1. List words that look mis-transcribed and suggest what sound or stress problem might cause it (e.g. word stress, v/w, th, final consonants, vowel length). Say when you are guessing.
2. List multi-syllable words from my talk with correct stress marked like de-VEL-op-ment and IPA (US).
3. Give 10 minimal pair or stress drills for my likely problem sounds.
4. Give me one sentence with the main pattern of intonation to copy (marked with rising and falling).
5. Give me a 2-minute shadowing plan.
My notes: [WORDS I FELT UNSURE ABOUT]
Transcript: [PASTE]
```
Also compute yourself: words per minute (words / minutes), fillers per minute, longest sentence. Ask the tutor to count fillers in the transcript.

## 5. Writing edit with track changes
```text
Edit the text below for a [VP / peer / customer] audience. Show track changes: use ~~strikethrough~~ for deletions and **bold** for insertions. After the marked text, give the clean version, then a list of edits grouped by reason (concision, precision, tone, grammar, structure) with a rule for each. Constraints: cut at least 25 percent of words, put the ask in the first two lines, keep all numbers and facts, American spelling, no idioms that a non-native reader might miss.
Text:
[PASTE]
```
Extra: "Now give me a second version at a warmer tone, and one at a more formal tone, and tell me what changed."

## 6. Weekly diagnostic
Run every Sunday after the drill week. Paste the week's writing and a transcript of your Saturday talk.
```text
Weekly diagnostic. I studied this week: [GRAMMAR TOPIC], [VOCAB THEME], [IDIOMS]. Here is my writing sample and my talk transcript.
1. Test me: ask 10 questions (mixed) on this week's topics and 5 on earlier weeks (spaced review). One at a time. Wait for my answer. Mark each.
2. Then analyse my texts: errors per 100 words, top 3 error patterns, whether I used this week's words correctly (quote them), and any word I overused.
3. Give a 7-day plan of 10 minutes a day for my weakest pattern.
4. Suggest 5 words or phrases I should learn next based on my writing.
Sample: [PASTE]
```

## 7. Error-log analysis (monthly)
Keep an error log as a list: date, wrong version, right version, rule.
```text
Here is my error log for the last [4] weeks. Group errors into categories, count them, and rank by frequency. For the top 3 categories: explain the underlying rule once, why I might make this error (first-language transfer if you can say, but say if you are guessing), and create 8 practice items (mixed: correction, gap-fill with two plausible options, rewrite). Then compare: which categories appear to be improving compared with earlier weeks (I will paste the earlier log if you ask). Finally draft 15 Anki cards (front: the error; back: correction and rule).
Log:
[PASTE]
```

## 8. More prompts

**Idiom and register check**
```text
For each phrase below, tell me: meaning, register (formal, neutral, informal), region (US, UK, both, international), how common it is in workplace English now (very / occasionally / dated), and whether it would confuse non-native listeners. Then give a plain alternative and an example sentence in an engineering context.
Phrases: [LIST]
```

**Vocabulary in context**
```text
Give me 8 C1-level business/tech-leadership words on the theme [THEME]. For each: part of speech, meaning, 2 collocations, one example about engineering or logistics, and a common misuse. Then a cloze test of 8 sentences. Do not show answers until I respond.
```

**Answer-first speaking drill**
```text
Ask me one interview or executive question at a time. I will answer in 60-90 seconds as text (as if I spoke). Judge: did I answer first, did I use a clear structure (PREP/STAR/pyramid), did I quantify, and where did I hedge unnecessarily? Rewrite my answer at half the length. Then ask a follow-up that a skeptical executive would ask.
```

**Cross-cultural message check**
```text
Here is a message I will send to a mixed global team (India, Europe, US). Check for idioms, indirectness, sarcasm, ambiguous dates or time zones, and cultural pitfalls. Tell me which parts could be misread and offer clearer wording. Do not stereotype; give hypotheses.
Message: [PASTE]
```

**Baseline comparison (checkpoints)**
```text
Here is my baseline writing sample from week 0 and my new sample from week [N]. Compare them on: error rate per 100 words, sentence variety, precision of vocabulary, structure, and tone. Be specific and quote. Tell me what improved, what has not, and the two priorities for the next 4 weeks.
```

## Session hygiene
- Ask for one thing at a time; long prompts with many tasks get shallow answers.
- Ask "what would a native speaker actually say here?" when a correction feels stiff.
- Log every correction you did not already know in your error log the same day.
- Every month, verify five AI corrections against a dictionary or grammar reference to keep calibrated.
- Related: [Shadowing & self-review](shadowing-and-self-review.md), [Common errors of fluent speakers](common-errors-fluent-speakers.md), [track overview](index.md).
