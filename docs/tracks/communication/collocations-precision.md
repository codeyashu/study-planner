---
title: "Collocations & precision with numbers and data"
track: communication
slug: collocations-precision
priority: P1
complexity: 3
est_hours: 2
phase: 2
tags: [communication, P1]
last_reviewed: 2026-09-25
---

# Collocations & precision with numbers and data

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 3/5 · **Est. time:** 2 h · **Phase:** 2 · **Prereqs:** [prepositions & collocations](prepositions-collocations.md), [business & tech-leadership vocabulary](business-tech-vocabulary.md)
    **You're done when:** you can describe a trend, a magnitude of change, and a degree of certainty about a number precisely, choosing the right verb + noun collocation and the right approximator, without defaulting to vague words like "a lot" or "very".

## Why it matters
Staff engineers constantly report and reason about numbers: latency, error rate, cost, headcount, timelines, confidence intervals. Precision here is not pedantry - "roughly 20%" and "exactly 20%" and "up to 20%" commit you to different things, and a VP will act differently on "significant" versus "12%, with a margin of error of ±3 points". The vocabulary of quantity, trend and approximation is a small, learnable set. Native speakers also use fixed collocations (*make progress*, not *do progress*; *a sharp rise*, not *a sharp increase* - actually both, but *steep rise* not *steep increase*) - learning the pairs, not just the words, prevents subtly foreign-sounding sentences.

## Core concepts

### 1. Describing magnitude of change (verb + adverb/noun)

| Small/gradual | Moderate | Large/sudden |
|---|---|---|
| edge up / down | rise, fall, increase, decrease | surge, spike, soar, plummet, plunge |
| tick up / down (informal) | climb, drop | skyrocket, collapse |
| inch up / down | grow, shrink | jump, crash |
| creep up | improve, decline | rocket (UK informal) |

**Collocating adverbs (verb + adverb):** *rise sharply / steadily / gradually / slightly / significantly / dramatically / marginally*; *fall sharply / steeply / slightly*; *increase substantially / modestly*.

**Collocating adjectives (noun form: a ___ rise/fall/increase/decrease):** *a sharp rise, a steep decline, a modest increase, a marginal change, a dramatic drop, a steady improvement, a slight dip, a significant reduction, a substantial gain, a negligible effect*.

**Trap:** *a big increase* is grammatical but informal/imprecise; prefer *a substantial/significant increase* in writing, and always attach a number when you have one: "a substantial (23%) increase" beats "a substantial increase" alone.

### 2. Describing trend shape and duration

| Word | Meaning |
|---|---|
| plateau | level off after growth/decline, verb or noun | "Latency plateaued around 80 ms." |
| level off / level out | stop rising or falling | |
| stabilise (US: stabilize) | become steady | "Error rates have stabilised." |
| fluctuate | vary up and down irregularly | "CPU usage fluctuates throughout the day." |
| taper off | gradually decrease toward the end | "Traffic tapers off after 6 p.m." |
| bottom out | reach the lowest point before recovering | "Sign-ups bottomed out in January." |
| peak (at) | reach the highest point | "Load peaked at 40k RPS." |
| trend upward/downward | show a general direction over time | "Costs are trending upward." |
| a downward/upward trajectory | | |
| rebound / recover / bounce back | return toward a previous level after a drop | "Conversion rebounded after the fix." |
| a step change | a sudden, discrete shift to a new level (not gradual) | "The new cache produced a step change in latency." |
| a knock-on effect | a secondary consequence | "The outage had a knock-on effect on billing." |

### 3. Approximating a number precisely

| Function | Words | Example |
|---|---|---|
| Roughly, close to exact | approximately, roughly, about, around, or so, in the region of, in the ballpark of (informal) | "Approximately 4,000 requests per second." |
| Slightly under/over | just under, just over, nearly, almost, barely | "Just under 5%." "Barely 2 seconds." |
| A range | between X and Y, X to Y, in the range of, anywhere from X to Y | "Between 200 and 300 ms." |
| An upper/lower bound | up to, at most, no more than / at least, a minimum of | "Up to 10,000 concurrent users." "At least 99.9% availability." |
| Order of magnitude | on the order of, roughly X times | "On the order of 10x more traffic." |
| A precise figure with confidence | exactly, precisely; give the margin: ± | "Exactly 47 minutes." "12% ± 2 points." |
| Vague quantity (avoid in data reporting) | a lot of, a bunch of, tons of, loads of | Fine in speech; replace with a number or a defined range in writing. |

### 4. Frequency and proportion

| Word | Meaning | Example |
|---|---|---|
| the majority / a majority of | more than half | "The majority of incidents are config-related." |
| a minority of | less than half, a smaller part | |
| a handful of | a small number (informal-ish, common) | "A handful of customers were affected." |
| the vast majority / an overwhelming majority | almost all | |
| a fraction of | a small part | "Only a fraction of traffic hits the fallback path." |
| roughly X in Y / one in three | ratio expressed naturally | "Roughly one in five deployments needs a rollback." |
| on average / on the whole / typically / generally | | |
| more often than not | more than 50% of the time (informal) | |
| rarely, seldom, occasionally, frequently, consistently | frequency adverbs, see [articles/word order] | |

### 5. Cause, correlation, and confidence language for data claims
- **Correlation vs causation:** *is associated with, is correlated with, tends to co-occur with* (correlation) vs *causes, leads to, results in, is responsible for* (causation). Do not claim causation from correlation alone: "Latency correlates with cart abandonment" ≠ "Latency causes cart abandonment" unless tested.
- **Confidence framing:** pair with the [hedging ladder](conditionals-modals-hedging.md): "the data suggest / indicate / show / confirm" (increasing strength); "this is consistent with / this points to" (softer).
- **Statistical vs practical significance:** "statistically significant" has a technical meaning (p-value); don't use it loosely to mean "big". Use *substantial, material, meaningful* for practical size.
- **Sample and scope caveats:** "based on a sample of 200 sessions", "in the regions we measured", "so far this quarter" - precision requires scoping the claim.

### 6. Verb + noun collocations for reporting numbers
| Collocation | Example |
|---|---|
| hit a target / miss a target | "We hit our latency target for the quarter." |
| meet / exceed / fall short of expectations | "Adoption exceeded expectations." |
| beat / miss a forecast | "Revenue beat the forecast by 5%." |
| post a gain / a loss | "The team posted a 15% efficiency gain." |
| set a record | "Traffic set a new record on Black Friday." |
| break down by (category) | "Costs break down by team as follows." |
| account for (a share) | "Compute accounts for 60% of the bill." |
| make up (a proportion) | "Retries make up a small share of total calls." |
| come in at / land at | "The final number came in at 8.2%." |
| track against (a target) | "We're tracking against the Q3 goal." |

### 7. Units, precision and formatting in prose
- Always pair a number with a unit and, where relevant, a time window: "40 ms p99 latency over the last 7 days", not "latency is low".
- **Precision matches confidence:** don't write "47.3%" if your measurement error is ±5 points; round to match true precision ("about 47%").
- **Percent vs percentage points:** "error rate rose from 2% to 4%" is a rise of "2 percentage points" or "a 100% relative increase" - these are very different claims; state which you mean.
- **Doubling/halving language:** "twice as many", "half as much", "an X-fold increase", "an order of magnitude" (≈10x).
- **Time-window precision:** "week-over-week", "quarter-over-quarter", "year-over-year (YoY)", "month-over-month (MoM)".

## Reference table: vague to precise

| Vague | Precise |
|---|---|
| "Latency is a lot better." | "P99 latency dropped from 800 ms to 120 ms, an 85% reduction." |
| "We had a lot of incidents." | "We had 14 incidents this quarter, up from 9 last quarter." |
| "Costs went up a bit." | "Compute costs rose 6% quarter-over-quarter." |
| "Most teams are on the new platform." | "32 of 40 teams (80%) have migrated." |
| "The fix helped a ton." | "The fix cut error rate from 3.2% to 0.4%." |
| "It's much faster now." | "It's roughly 3x faster (from 900 ms to 300 ms)." |
| "Adoption is growing fast." | "Weekly active users grew 18% month-over-month for three consecutive months." |

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Ozdic collocation dictionary](https://ozdic.com/) :gem: | dictionary | Look up "increase" or "rise" to see exactly which adjectives/adverbs collocate. | intermediate-advanced | free |
| [Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/) | dictionary | Clear entries for approximators (*roughly, nearly, barely*) with examples. | all | free |
| [Cambridge Dictionary](https://dictionary.cambridge.org/) | dictionary | Good coverage of frequency and proportion words with usage notes. | intermediate | free |
| [English-Corpora.org (COCA)](https://www.english-corpora.org/coca/) :gem: | tool | Check real collocates for "increase/rise/surge" plus adverb pairings by frequency. | advanced | freemium |
| Cambridge *English Collocations in Use (Advanced)* | book | Includes a unit on describing trends and data, with exercises. | intermediate-advanced | paid |
| [Google developer documentation style guide](https://developers.google.com/style) | style guide | Numbers section: formatting, units, precision guidance for technical writing. | intermediate | free |
| [Plain Language guidelines](https://www.plainlanguage.gov/) | guide | Advocates precise, concrete numbers over vague qualifiers. | intermediate | free |
| Nate Silver, *The Signal and the Noise* | book | Not a language book, but sharpens the habit of precise, honest uncertainty language around data. | advanced | paid |

## Hands-on lab (45-60 min)
1. **Vague hunt.** Find five instances of "a lot", "very", "significantly" (without a number) or "much better" in your own recent writing. Replace each with a number, a range, or a precise collocation from the tables.
2. **Trend description.** Take a real metric from your work (latency, cost, error rate, adoption) over the last quarter and describe its trend using at least four different trend/magnitude words (rose, plateaued, spiked, stabilised).
3. **Approximator drill.** Write the same number five ways: exact, "roughly", "just under", "in the range of", "on the order of" - and decide which fits a headline vs a detailed appendix.
4. **Correlation check.** Rewrite a claim you've made recently that implied causation from correlation, adding appropriate hedging language.
5. **Speak it.** Give a 60-second spoken summary of a metric's trend using precise collocations, no "a lot"/"very".

## Questions

### L1 - Recall

??? question "Q1. Give three verbs for a large, sudden increase and three for a small, gradual one."
    ??? success "Answer"
        Large/sudden: surge, spike, soar (also skyrocket, jump). Small/gradual: edge up, tick up, inch up, creep up.

??? question "Q2. What is the difference between \"just under 5%\" and \"about 5%\"?"
    ??? success "Answer"
        "Just under 5%" means slightly less than 5% (e.g., 4.7%), a precise directional claim. "About 5%" is a looser approximation that could be slightly above or below 5%.

??? question "Q3. Distinguish \"percentage points\" from \"percent\" when describing a change from 2% to 4%."
    ??? success "Answer"
        The change is 2 percentage points (4% − 2%), but a 100% relative increase (it doubled). Saying "a 2% increase" would be wrong and misleadingly small.

??? question "Q4. Name the collocation error: \"do a progress\" and \"make an increase\"."
    ??? success "Answer"
        Correct: "make progress" (not "do progress") and "see/show an increase" or simply "increase" as a verb (not "make an increase"). Learn the fixed verb-noun pairing, not each word separately.

### L2 - Apply

??? question "Q5. Rewrite precisely: \"Latency got a lot worse after the release, but it's kind of stabilising now.\""
    ??? success "Answer"
        "P99 latency rose sharply after the release, from 150 ms to 600 ms, and has since plateaued around 400 ms." (Names the metric, gives before/after numbers, uses precise trend verbs.)

??? question "Q6. Choose the right word: \"Adoption ___ (plateaued / surged) after we removed the sign-up friction, then ___ (tapered off / bottomed out) once we'd captured the early-adopter segment.\""
    ??? success "Answer"
        surged (sharp rise after the fix); tapered off (gradual decrease as the easy gains were captured).

??? question "Q7. Fix the collocation: \"We did a big improvement on cost and made a decrease in errors.\""
    ??? success "Answer"
        "We made a substantial improvement in cost and achieved a decrease in errors." (or "we substantially reduced cost and errors"). *Make an improvement*, not *do an improvement*; pair *decrease* with *achieve/see/there was*, not *make*.

??? question "Q8. Express the same fact three ways with different confidence: \"Roughly 60% of teams have migrated (estimate from an incomplete count).\""
    ??? success "Answer"
        "The data indicate that roughly 60% of teams have migrated." (moderate confidence, hedged); "Based on our current (incomplete) count, about 60% of teams have migrated." (explicit scope caveat); "We estimate 60%, ±5 points, pending final confirmation from three teams." (explicit uncertainty range).

### L3 - Judge and choose

??? question "Q9. \"Errors increased significantly\" vs \"errors increased by 40%\": which do you write in an incident report, and when is \"significantly\" still useful?"
    ??? success "Answer"
        Prefer the number: "errors increased by 40%" is falsifiable and actionable. "Significantly" is useful only as a lead-in before the number ("Errors increased significantly - by 40%, from 2% to 2.8%") or when you genuinely lack a number and want to flag direction and importance without overclaiming precision you don't have.

??? question "Q10. A dashboard shows latency \"correlates with\" cart abandonment. A PM wants to write \"latency causes cart abandonment\" in a slide. How do you respond?"
    ??? success "Answer"
        Point out the correlation-causation gap: other factors (time of day, user segment, promo periods) could explain both. Suggest either running a controlled test (e.g., an A/B latency injection) before claiming causation, or softening the slide language to "latency is strongly associated with cart abandonment; we plan to test this causally." Precision protects the team from an overclaim that gets challenged later.

??? question "Q11. When is \"a handful of customers\" appropriate, and when should you give an exact number instead?"
    ??? success "Answer"
        "A handful of" is fine in a quick verbal update where the exact count doesn't change the decision (roughly 3-6). In a written incident report, customer-facing communication, or anything that will be audited, give the exact number ("14 customers were affected") - vague quantifiers in formal incident documentation can look evasive.

??? question "Q12. \"Costs are trending upward\" - is this claim complete? What's missing for a Staff-level update?"
    ??? success "Answer"
        Missing: the time window, the magnitude, and the driver. A complete version: "Compute costs have trended upward for three consecutive months, up 22% cumulatively, driven mainly by the new ML inference workload." Trend words alone describe shape, not size or cause - both are usually needed for a decision-maker.

### L4 - Real-world decisions

??? question "Q13. You must present a quarter's reliability numbers to the board in 90 seconds. Draft the key sentence, choosing precision level deliberately."
    ??? success "Answer"
        "Availability held at 99.95% for the quarter, in line with our SLO; the one exception was a 47-minute outage in March, which we've since addressed with an automated failover - so we don't expect a repeat of that specific cause." One precise headline number, one scoped exception with a number, one forward-looking mitigation - no vague qualifiers, appropriate for board-level brevity.

??? question "Q14. A colleague's design doc claims \"this will make things much faster\" with no numbers, for a change you suspect has real but modest impact. How do you push for precision without derailing the review?"
    ??? success "Answer"
        Ask a specific, low-friction question: "Do we have a rough estimate - even order-of-magnitude - of the expected latency improvement, so reviewers can judge if it's worth the added complexity?" This invites a number without demanding a full benchmark, and frames precision as helping the proposal, not attacking it.

??? question "Q15. Your team's postmortem draft says \"the impact was significant.\" The audience includes both engineers and a non-technical executive sponsor. Rewrite for both audiences in one paragraph."
    ??? success "Answer"
        "The outage affected approximately 12,000 customers (about 8% of daily active users) for 47 minutes, resulting in an estimated $40,000 in lost transactions. For engineers: p99 latency spiked to 4.2 seconds before the circuit breaker tripped at 09:38 UTC." Leads with the business-relevant number and scope, then adds the technical detail as a clearly separated addendum - serves both audiences without forcing either to translate vague language.

## Real-world use cases
- **Postmortems and incident reports:** exact scope, duration, and customer impact numbers.
- **Capacity planning docs:** order-of-magnitude estimates with explicit uncertainty.
- **Exec/board updates:** one precise headline metric plus a scoped exception, no unqualified "significantly".
- **A/B test and experiment write-ups:** correlation vs causation language, confidence intervals.
- **Vendor/cost negotiations:** precise percentage vs percentage-point distinctions matter for money.

## Pitfalls & anti-patterns
- Using "a lot", "very", "significantly" without ever attaching a number.
- Confusing percentage change with percentage-point change.
- Claiming causation from correlation.
- Using "statistically significant" loosely to mean "big" or "important".
- Reporting more decimal precision than your measurement actually supports.
- Mixing time windows without labeling them (week-over-week vs quarter-over-quarter).
- Wrong verb-noun collocations ("do a progress", "make an increase").

## Checklist
- [ ] I can describe a trend's shape, size, and duration using at least six different precise words.
- [ ] I can express the same number with five different levels of approximation.
- [ ] I distinguish percentage-point change from percent change reliably.
- [ ] I avoid claiming causation from correlation in my own writing.
- [ ] I answered all L3 questions out loud in under 3 minutes each.
