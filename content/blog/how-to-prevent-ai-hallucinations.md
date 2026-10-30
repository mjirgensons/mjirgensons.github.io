---
title: "How to prevent AI hallucinations in business advice"
description: How to prevent AI hallucinations when you ask ChatGPT or Claude for business advice: a blind test where invented facts fell from 7 answers in 10 to 1 in 120.
date: 2026-10-30
updated: 2026-10-30
chapter: Chapter 16, The electricity we have already switched on; Appendices H, I and J
slug: how-to-prevent-ai-hallucinations
keywords: [how to prevent ai hallucinations, ai hallucinations, what is ai hallucinations, ai hallucinations example, stop chatgpt making things up, chatgpt for small business]
answer: "How to prevent AI hallucinations in business advice: give the assistant a fixed rulebook that allows only three kinds of statement about your situation (your facts, arithmetic shown from them, and labelled assumptions) and a fixed order of analysis. In a blind test of the Jirgenson Model, answers with an invented fact fell from seven in ten to one in a hundred and twenty."
---

A food truck has 72 hours before it loses its permit. The owner types the situation into an AI assistant and gets back a confident, beautifully formatted plan. It mentions an "industry average" repair time, a "typical" grace period from the city, and a cash figure the owner never gave it. All three are invented. None of them is flagged. And the owner, tired and frightened, has no way to tell which sentences came from his life and which came from the machine's imagination.

That is what AI hallucinations look like in real life: a plausible number in the one place where you can least afford a wrong one. If you have ever wondered how to prevent AI hallucinations when you ask for business advice, the most useful answer I have read is hidden in the appendices of a management book: *Steer, Don't Guess* by Martin Jirgenson.

## What AI hallucinations are, in a business conversation

Most people picture AI hallucinations as a chatbot insisting the moon is made of cheese: obvious, funny, harmless. In a business conversation the reality is narrower and far more dangerous. It is any figure, rule, deadline or cause that was not in what you told the assistant, presented as a fact rather than as an assumption. A "typical margin for cafes". A "standard 30-day notice". "Most clients pay within a week". Each sounds like help. Each quietly replaces your situation with an average one.

The reason is not malice. A language model is built to produce a fluent answer, and when your data has a gap, the most fluent thing to do is fill it. Chapter 16 of the book puts it plainly: an assistant with nothing to anchor it "has to say something, so it does". If data are missing, it fills the gaps with plausible assumptions. If you have not said what matters most to you, it chooses for you.

<div class="def"><strong>In the Jirgenson Model,</strong> an invented fact is any number, rule or cause about your situation that you did not supply and that the assistant presents as fact instead of labelling it as an assumption. The model's canon forbids it outright: data come from the owner, and unknown data are requested, not guessed.</div>

## The blind test: seven in ten, then one in a hundred and twenty

Most advice on how to prevent AI hallucinations stops at "write a better prompt". Jirgenson did something rarer: he measured it. The experiment, called E5, gave the same AI (Claude Sonnet 5.5) ten realistic small-business crises: the food truck racing its permit deadline, a translation agency that depends on one client while AI reshapes its whole market, a freelancer six days from rent with a client who has stopped paying. Each case was answered with no instructions, the way most people use AI, and again with the Jirgenson Model's canon and operating prompt. A stronger model (Claude Opus 5.5) judged every pair blind against an answer key fixed in advance.

The results read like a before and after photograph:

| | Without the method | With the method |
|---|---|---|
| Answers containing an invented fact | 7 in 10 | **1 in 120** |
| Rule violations per answer | 1.05 | **0** |
| Score out of 100 | 56.2 | **88.8** |
| Blind pairings won | 0 | **30 of 30** |
| Control quality (1 to 10) | 4.2 | **8.3** |

Left to itself, the assistant slipped something made up into seven answers out of ten. With the method, one answer in a hundred and twenty. It broke no rules in 120 blind reviews, scored 58% higher, and beat a good generic consultant prompt by 31%. The biggest gains came exactly where hallucinations hurt most: the translation agency case improved by 51 points, the food truck by 42.

And the single invented fact that survived? The judge traced it back to an example sentence inside the prompt itself. The assistant had not made anything up. It had copied, faithfully, the one number its own instructions contained. If there is a better illustration of how literally these systems follow what you give them, I have not seen it.

## How to prevent AI hallucinations: the five rules that did the work

What makes this part of the book brilliant is that the rules are simple enough to use tomorrow, even without the book's files.

**1. Allow only three kinds of sentence about the situation.** The operating prompt permits exactly three:

- the person's own facts;
- arithmetic shown from those facts;
- assumptions labelled "I am assuming", with what changes if they are wrong.

Everything else (causes, typical values, what others will do) must be phrased as a check to perform. This single rule is the heart of how to prevent AI hallucinations in practice: it gives the model a legal place to put its guesses, so they stop disguising themselves as facts.

**2. Ask only what would change the decision.** An assistant that must compute with what it has, and may ask only questions that change the answer, has no reason to invent the rest.

**3. Never let it choose your priorities.** The assistant proposes an order of goals in your own words, marks it as a proposal, and you confirm it. A machine that is not allowed to decide what matters to you has one less thing to hallucinate.

**4. Fix the shape of the answer.** The same order every time: where you are, the most dangerous point, what to do, what to protect, what not to do, what to measure, two forecasts. When the structure is fixed, a missing number has nowhere to hide.

**5. Treat a mismatch as a red alarm.** If the assistant's figures stop matching yours, the book says, that is an error to diagnose: check the data, the calculation, the version of the rules, then restart with the goals and the state supplied again. Hallucinations thrive in long, drifting conversations; a reset rule starves them.

## An AI hallucinations example, and the same question answered properly

The book's own example is worth quoting in spirit. You write: "I have a small workshop, orders come in unevenly, and the money runs out too soon."

An assistant without the canon replies with pages of sensible, generic advice: broaden your customer base, keep a budget, think about advertising. None of it is wrong. None of it is yours.

An assistant with the canon starts from your own sentence. If the money runs out too soon, the reserve is less than a month of expenses, and that is the most vulnerable point. The first safe action is to calculate the reserve in months from your bank statement. Then it asks the one question that would change the plan. No averages, no invented deadlines, no borrowed margins. Just your numbers, and the honest gaps between them.

## Where this does not reach

The test has clear limits, and the book states them calmly: ten scenarios, one model family, an AI judge. The method and the earlier round's full data are public on GitHub, and the author invites anyone to rerun it. A rulebook does not make a language model infallible, and it does not replace your judgement or your data. What it does is make deviations visible. When the assistant starts inventing, you notice at once, because you know what the right move looks like.

<div class="takeaways" markdown="1">
### Key takeaways

- AI hallucinations in business advice are invented numbers, rules and causes presented as facts about your situation.
- The most effective way to prevent AI hallucinations is to restrict what the assistant may say: your facts, shown arithmetic, labelled assumptions.
- In a blind test, the Jirgenson Model cut answers with an invented fact from seven in ten to one in a hundred and twenty, with zero rule violations.
- Fix the order of the answer, keep priorities yours, and treat any mismatch with your figures as a red alarm.
</div>

## The book behind the prompt

The canon and the operating prompt are free, and you can [download them here](/ai-assistant/). But they are the appendices of a book, not a replacement for it. *Steer, Don't Guess* explains why these rules work: why a goal list needs an order, why a number needs one source, why a red line must be drawn before the crisis. Read it and you will not only know how to prevent AI hallucinations; you will know what a good answer looks like before the assistant gives it to you. That is the real protection.

Start with [the free sample](/blog/free-sample/) (the Introduction and Chapter 1), see how the whole method fits together in [the Jirgenson Model explained](/blog/jirgenson-model-management-method/), or read how the same discipline works without any AI in [what to do first in a business crisis](/blog/business-crisis-what-to-do-first/). When you are ready, the book is on [Amazon](https://www.amazon.com/dp/B0HPBR6BNX).

## FAQ

### How do you prevent AI hallucinations in business advice?

Give the assistant a rulebook that allows only your facts, arithmetic shown from them and labelled assumptions, a fixed order of analysis, and a rule to ask only questions that change the decision. In a blind test, this cut answers with an invented fact from seven in ten to one in a hundred and twenty.

### What is an AI hallucination?

It is confident output not supported by what you provided or by reality. In business advice it usually appears as an invented figure, deadline, typical value or cause, presented as fact instead of as an assumption.

### Can ChatGPT be stopped from making things up completely?

No rulebook makes a language model infallible. A strict prompt and canon make invented facts rare and visible, so you can catch them; your own data and judgement remain the final check.
