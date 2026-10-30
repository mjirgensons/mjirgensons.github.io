---
title: The Jirgenson Model canon and prompt for AI assistants
description: Free canon and operating prompt that make an AI assistant (ChatGPT, Claude, Gemini) analyse a business situation by the Jirgenson Model. Blind-tested: invented facts fell from 7 answers in 10 to 1 in 120.
url: /ai-assistant/
kicker: AI assistant
lead: Two plain-text files turn a general-purpose AI assistant into a management analyst that works by the Jirgenson Model and refuses to start without it. They are free. The book explains why they work and how to read what comes back.
updated: 2026-10-29
---

## What the files are

- **The canon** (`jirgenson_canon_v1.0_en.txt`): the compact rulebook of the model, sections §0 to §16, canon-id JMC-1. It is Appendix H of the book.
- **The operating prompt** (`jirgenson_prompt_v1.1_en.txt`): tells the assistant how to work with the canon: gate on the canon, help first, apply the model silently, never invent data, propose a refusal order and let the owner confirm it, give two forecasts with ranges, name the most dangerous thing with a date. It is Appendix I of the book.

Both files are on [GitHub](https://github.com/mjirgensons/jirgenson-model) under an open licence. Without the canon the assistant will not start and will ask for it: this is by design.

## How to use them

1. Download both files (Download or Raw, then save).
2. Open a new conversation with a language model assistant.
3. Attach the canon file to the message, or paste its full text.
4. Send the prompt as your first message.
5. Describe your situation in plain words, with your numbers, as your second message. Sample messages are in Appendix I of the book.

Three modes are built in: **emergency** (one action for today), **quick** (where you are and what to do this week, in one reply), and **full** (analysis in rounds with up to five questions). You do not need to name the mode; the assistant picks it from your message.

## What the blind test measured

Ten realistic business crises, each answered three times by the same AI (Claude Sonnet 5.5) with the canon and prompt and without them. A stronger model (Claude Opus 5.5) judged every pair blind, in both orders, against an answer key fixed in advance. Final round, prompt version 1.5:

| | With the method | Without | Good generic prompt |
|---|---|---|---|
| Score out of 100 | **88.8** | 56.2 | 67.7 |
| Blind pairings won | **30 of 30** | 0 | |
| Answers with an invented fact | **1 in 120** | 7 in 10 | |
| Rule violations per answer | **0** | 1.05 | 0.97 |
| Control quality (1 to 10) | **8.3** | 4.2 | 6.0 |
| Critical points covered | **97%** | 55% | 66% |

The single invented fact in 120 reviews was copied from an example sentence inside the prompt itself. Limits: ten scenarios, one model family, an AI judge. The results above are for the latest tested version of the prompt (1.5); the files on GitHub are the book edition. The method and the earlier round's full data, with every answer, judge record and script, are [public](https://github.com/mjirgensons/jirgenson-model/tree/main/experiments/E5-blind-test-2026-10). Don't believe it; run it.

## What you get back

A short brief in your own words: where you are (three to six numbers, computed), the greatest danger with a date and an amount, what to do today, this week and this month on levers you actually control, what you protect first, what not to do now, what to measure and when to check, and two forecasts, "if nothing changes" and "if the plan works", each with a range. The model's vocabulary stays inside the assistant's reasoning; you see results.

## FAQ

### Which AI assistants does it work with?

Any capable language model that accepts a long text attachment or paste: ChatGPT, Claude, Gemini and others. The published test used one model family; results elsewhere may differ.

### Will the assistant choose my priorities for me?

No. The canon forbids it (§15.2): the assistant proposes a refusal order from your words, marks it as its own proposal, and proceeds; you confirm or change it.

### Does it invent numbers?

The prompt allows only three kinds of sentence about your situation: your facts, arithmetic shown from them, and assumptions labelled as such. In the final round of the blind test, answers with an invented fact fell from 7 in 10 to 1 in 120.
