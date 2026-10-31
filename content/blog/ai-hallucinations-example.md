---
title: "AI Hallucinations Example: How to Spot an Invented Fact"
description: "An AI hallucinations example from business advice, the five shapes an invented fact takes, and a 15-minute audit that sorts every sentence before you act on it."
date: 2026-10-31
updated: 2026-10-31
chapter: Chapter 16, The electricity we have already switched on; Appendices H, I and J
slug: ai-hallucinations-example
keywords: [ai hallucinations example, how to prevent ai hallucinations, ai hallucinations, what is ai hallucinations, stop chatgpt making things up, chatgpt for small business, ai hallucination examples in business, how to spot ai hallucinations, chatgpt invented numbers, check ai answers, ai reproducibility check]
answer: "An AI hallucinations example from business advice: you ask about falling cash, and the answer quotes a 'usual' payment term you never mentioned. An invented fact is any number, rule, cause or priority about your situation that you did not supply, stated as fact. Sort every sentence of the answer: your fact, arithmetic shown from it, a labelled assumption, or a check you still have to make."
---

The most dangerous sentence in an AI answer is the one that sounds like your own accountant.

It is late, and you type your situation into an assistant: the print shop shows a profit, yet the cash keeps falling. The reply comes back calm, structured and sure of itself. Halfway down it says that print shops are usually paid within 60 days. You never mentioned payment terms. (This is an illustration, not a quote from any test.)

The answer is laid out better than your bank statement. It rests on a number nobody gave it.

## What AI hallucinations look like in a business answer

In a business conversation, the invented fact is quiet. It is any figure, rule, deadline, cause or priority about your situation that you did not supply, presented as fact instead of as an assumption.

The mechanism is plain. An assistant with nothing to anchor it has to say something, so it does. Where your data have a gap, it fills it with something plausible and does not tell you. Where you have not said what matters most, it picks for you.

<div class="def"><strong>In the Jirgenson Model,</strong> an assistant may state three kinds of thing about your situation. Your own facts, arithmetic shown from them, and labelled assumptions. Anything else appears as a check for you to make. The canon puts it in one line: the model never chooses the owner's priorities, and never invents data.</div>

## An AI hallucinations example in five shapes

The situations below come from a blind test of ten small-business crises. The sentences in quotes are illustrations of each shape, written for this post.

**1. The typical value.** The print shop with a profit and falling cash. "Print shops are usually paid within 60 days." A statement about what is usually true has replaced your own debtor list.

**2. The borrowed rule.** The food truck with 72 hours left before its permit is suspended. "Cities normally allow a short grace period." If that rule does not apply, the owner learns it on day three.

**3. The invented cause.** The translation agency losing clients to automatic translation. "Your clients left because your prices are too high." A cause is a hypothesis. Stated as fact, it sends the owner after the wrong lever.

**4. The chosen priority.** The freelancer whose client has stopped paying, with rent due in six days. The answer decides that keeping the client matters more than the rent, without asking. A machine that sets your order of goals has invented the most important fact of all.

**5. The promise.** The second nail salon whose owner asks for a guaranteed payback. "With this plan, you will break even in eight months." No honest answer guarantees a result.

Each one swaps your situation for an average one.

## What a blind test found

Left to itself, the assistant slipped something unsupported into seven answers out of ten. With the Jirgenson Model's canon and operating prompt, one answer in 120.

The test ran the same AI (Claude Sonnet 5.5) on ten realistic crises, with and without the model. A stronger model (Claude Opus 5.5) judged the pairs blind.

| | Without the model | With the model |
|---|---|---|
| Answers with an invented fact | 7 in 10 | 1 in 120 |
| Rule violations per answer | 1.05 | 0, in 120 blind reviews |
| Score out of 100 | 56.2 | 88.8 |
| Control quality, 1 to 10 | 4.2 | 8.3 |
| Mandatory elements covered | 55% | 97% |
| Average length, words | 501 | 454 |

The same AI scored 58% higher with the model. It scored 31% higher than a good generic consultant prompt. The blind judge preferred it 30 times out of 30. The biggest gains came in the crises: the translation agency rose 51 points, the food truck 42.

And the one invented fact left in 120 reviews? It was copied from an example sentence inside the prompt itself.

Ten scenarios, one model family, an AI judge; the method and the earlier round's full data are public on GitHub.

## How to spot AI hallucinations: a 15-minute audit

You can audit any answer, from any assistant, before you act on it. Five steps, each with a filled-in entry from the coffee shop that runs through the book.

**1. Feed it a sum you already know.** Give the assistant your goal rows and your current state, then ask for the gap on each row.
Andrew gives five goals and five readings. Reserve: 2.0 months wanted, 0.5 now. Margin: 15% against 9%. Regular customers: 40% against 25%. Complaints: 2 against 5. Hours: 40 against 65. It must return −1.5, −6, −15, +3 and +25. Any other number means it did not calculate from your data.

**2. Mark every sentence about your situation.** Use four marks (the sentences are illustrations):

| Mark | Meaning | Example sentence |
|---|---|---|
| F | Your own fact | "The reserve is 0.5 months of expenses." |
| A | Arithmetic shown from your facts | "0.5 × €27,300 = €13,650." |
| L | A labelled assumption, with what changes if it is wrong | "I am assuming revenue stays at €30,000; if it falls, the gap grows." |
| ? | Everything else | "Coffee shops usually run on 10% margins." |

**3. Turn every ? into a check.** Name who checks it, where and by when. "Coffee shops usually run on 10%" becomes: pull your own margin from the accounts, this week.

**4. Decide which checks to do by hand.** Multiply the chance of a wrong answer by the cost of the decision. If the result beats the cost of the check, check by hand.
Say the assistant is wrong in one case out of ten. A €2,000 equipment decision carries €200 of expected damage. A fifteen-minute check at €40 an hour costs €10. Check it. A €20 pastry order carries €2. Check a sample of one in ten instead.

**5. Restart when the numbers drift.** If the answers turn vague or stop matching your figures, treat it as an error. Find the cause, then open a clean conversation and give the goals and the state again.

That is the whole audit. It works on ChatGPT, Claude or any other assistant, because it checks the answer against your data, not against the brand.

## What six months of unchecked answers cost

Ask an unanchored assistant one question a week for six months. That is 26 answers. In the test, seven answers in ten carried an invented fact, and nothing marked which ones.

Each of those sits inside a decision. On one €2,000 decision, even a one-in-ten error rate is €200 of expected damage, against a €10 check.

The human cost: the owner acts at midnight on a grace period that does not exist.

The villain is not the assistant. It is the habit of asking with nothing on the table: no order of goals, no measured numbers, no rules. A fluent answer is not a measured one.

## What the audit does not fix

The audit catches invented facts after the assistant writes them. That treats the symptom.

The cause stays in place. The assistant still has no anchor. No ranked goals, no measured state, no rulebook for its answer. You will keep auditing the same kinds of mistake every week.

Two steps remove the cause.

- **Your goal order and your measured state, on paper before you ask.** Then it has no priorities to invent and no gaps to fill. The refusal test and the state table are the first two steps of the model.
- **The canon and the operating prompt.** A fixed order of analysis, rules for questions and a restart rule. Appendices H and I.

Without them, you are proofreading a confident stranger.

The assistant does not sit above the loop. Goal, state, error, levers, plan and forecast stay yours; the tool only speeds them up. The rules behind the falling error rate are in [how to prevent AI hallucinations](/blog/how-to-prevent-ai-hallucinations/).

<div class="takeaways" markdown="1">
### Key takeaways

- An invented fact is any number, rule, cause or priority about your situation that you did not supply, stated as fact.
- Watch for five shapes: the typical value, the borrowed rule, the invented cause, the chosen priority, the promise.
- Feed the assistant a sum you already know. A wrong gap means it did not use your data.
- Mark each sentence F, A, L or ?, and turn every ? into a check with a name and a date.
- In a blind test, invented facts fell from seven answers in ten to one in 120 with the model.
</div>

## Two choices for your next question

You have two choices. Keep asking with nothing on the table, and proofread every confident answer at midnight. Or put your goals and your numbers on paper first, so the assistant has nothing left to invent.

The audit catches the invented fact. The goal order, the measured state and the canon stop it from being written.

Test the logic for free: [Chapter 1, with the refusal test](/blog/free-sample/). Or get the full control system on Kindle for $9.99, [on Amazon](https://www.amazon.com/dp/B0HPBR6BNX). It comes as a Kindle book, with the canon and the operating prompt as appendices.

## FAQ

### What is an example of an AI hallucination in business?

An answer about your falling cash that says clients in your trade usually pay within 60 days, when you never mentioned payment terms. Any figure, rule or cause you did not supply, stated as fact, is an invented fact.

### How do I stop ChatGPT making things up?

Give it your ranked goals and measured numbers, and require that every statement is your fact, shown arithmetic or a labelled assumption. Then audit the answer: feed it a sum you already know and mark every sentence.

### Is ChatGPT safe to use for small business decisions?

As a fast helper, with checks. Let it calculate from your data and keep the order of goals yourself. Check by hand any decision where a wrong answer costs more than the check.
