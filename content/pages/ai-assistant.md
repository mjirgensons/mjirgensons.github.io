---
title: The Jirgenson Model canon and prompt for AI assistants
description: Free canon and operating prompt that make an AI assistant (ChatGPT, Claude, Gemini) analyse a business situation by the Jirgenson Model: priorities in refusal order, numbers not feelings, red lines, levers, two forecasts. Blind-tested: 88.9 vs 55.9, invented facts 75% to 11%.
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

The same model answered ten realistic business cases with the canon and prompt and without them. A stronger model judged every pair blind against a pre-registered answer key.

| | With the method | Without |
|---|---|---|
| Score, 0–100 | **88.9** | 55.9 |
| Pairs preferred by the judge | **30 of 30** | 0 |
| Answers containing an invented fact | **11%** | 75% |

Limits, stated in the book and in the repository: one judge model, one model family, ten development cases (ten further sealed cases are held out and hashed). The full method, raw answers, all 120 judge records, a second-judge spot check and the scripts are [public](https://github.com/mjirgensons/jirgenson-model/tree/main/experiments/E5-blind-test-2026-10). Don't believe it; run it.

## What you get back

A short brief in your own words: where you are (three to six numbers, computed), the greatest danger with a date and an amount, what to do today, this week and this month on levers you actually control, what you protect first, what not to do now, what to measure and when to check, and two forecasts, "if nothing changes" and "if the plan works", each with a range. The model's vocabulary stays inside the assistant's reasoning; you see results.

## FAQ

### Which AI assistants does it work with?

Any capable language model that accepts a long text attachment or paste: ChatGPT, Claude, Gemini and others. The published test used one model family; results elsewhere may differ.

### Will the assistant choose my priorities for me?

No. The canon forbids it (§15.2): the assistant proposes a refusal order from your words, marks it as its own proposal, and proceeds; you confirm or change it.

### Does it invent numbers?

The prompt allows only three kinds of sentence about your situation: your facts, arithmetic shown from them, and assumptions labelled as such. In the blind test, answers with an invented fact fell from 75% to 11%; not to zero.
