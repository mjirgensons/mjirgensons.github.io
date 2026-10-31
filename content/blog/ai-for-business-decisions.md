---
title: "AI for Business Decisions: What to Let It Do, What to Check"
description: "AI for business decisions: the four jobs an assistant can do in your loop, the risk in each, and a one-line rule for which answers to check by hand."
date: 2026-10-31
updated: 2026-10-31
chapter: Chapter 16, The electricity we have already switched on; Appendices H and I
slug: ai-for-business-decisions
keywords: [ai for business decisions, chatgpt prompt for business, chatgpt for small business, ai business advice, best chatgpt prompt for business, claude prompt for business, should ai make business decisions, ai decision making for small business, check ai answers, ai assistant for small business, human in the loop]
answer: "Use AI for business decisions as a calculator and an analyst, not as the one who decides. It can notice a deviation, build scenarios and prepare options; each job needs its own safeguard. You set the order of goals. Check an answer by hand when the chance it is wrong times the cost of the decision is larger than the cost of checking."
---

A food truck is 72 hours from losing its permit. Picture the owner typing the problem into a chatbot after closing.

The answer arrives fast. It is calm, well formatted and sure of itself. It may also contain a number the owner never gave it.

That food truck was one of ten test situations in a blind experiment. Without rules, seven answers in ten contained an invented fact. With a rulebook attached, one in a hundred and twenty did.

The machine was the same in both cases. What changed was what it was allowed to do.

## Why a fluent answer is not a safe one

An assistant asked about your business has to say something. So it does.

If a number is missing, it fills the hole with something plausible. If you did not say what matters most, it chooses for you. Then it hands you the result in perfect sentences, and there is nothing to check it against.

That is the trouble with most AI business advice. The grammar is flawless. The source of each number is unknown.

The common enemy here is not the tool. It is the confident guess: a figure that sounds right, arrives fast and was never yours.

## AI for business decisions: four jobs, four risks

Any tool, from a spreadsheet to a chatbot, can sit in your control loop in one of four places. Each place has its own way to fail and its own safeguard. Here they are, with Andrew's coffee shop next to each. The last column is an illustration built on his numbers.

| Job in the loop | What the AI does | How it fails | Safeguard | Andrew's example |
|---|---|---|---|---|
| 1. Notice the deviation | Compares the actual figure with the goal and raises a signal | False alarms, or silence from poor data | One source per number; thresholds set in advance | Reserve 0.5 months against a goal of 2.0: signal raised |
| 2. Build scenarios | Calculates "if nothing changes" and "if the plan works" | A neat calculation on wrong assumptions | Assumptions written down; forecast checked against facts | Goal reached at month 16 unchanged, month 10 with the plan |
| 3. Prepare the decision | Gathers options, consequences, questions | The first option to hand gets quietly accepted | A person approves the order of goals | It proposes "reserve first"; Andrew confirms it |
| 4. Execute | Reminds, orders, sends | A mistake repeated at speed; actions you cannot undo | Limited rights, a log, a person confirms | It drafts the supplier email; Andrew presses send |

Read the table from top to bottom. The further down, the more a mistake costs. So the access you give the assistant should shrink as you go down.

<div class="def"><strong>In the Jirgenson Model,</strong> a tool is not a lever. With a lever you move the process. With a tool you see and calculate. An assistant is a tool: it can see, calculate and prepare, while the choice and the responsibility stay with you.</div>

## The check-it rule, filled in

You cannot check every answer. You also cannot trust every answer. One line settles it.

Check an answer by hand when p × L is larger than c.

- **p** is the share of the assistant's answers that turn out wrong on tasks like this one. Take it from your own log.
- **L** is the cost of the decision if the answer is wrong.
- **c** is the cost of checking.

Here is the rule at work, with p = 0.1 (one wrong answer in ten):

| Decision | p × L | Cost of a 15-minute check at €40 an hour | Verdict |
|---|---|---|---|
| Buy equipment for €2,000 | 0.1 × €2,000 = €200 | €10 | Check it |
| Order €20 of pastries | 0.1 × €20 = €2 | €10 | Do not check each one. Check one in ten and update p |

Then add one test that takes two minutes. Give the assistant your goal rows and your state rows, and ask for the gaps. Andrew's five rows must come back as −1.5, −6, −15, +3 and +25. Any other number means the assistant did not calculate from your data.

Treat that as a red light. Find the cause: the data, the calculation or the version of the rules. Then start a fresh conversation and enter your goals and your state again.

That is the whole tool: four jobs with their safeguards, one line for when to check, and one two-minute test.

## What changed when the same AI had rules

Back to the ten test situations. The biggest gains came where an owner is most likely to panic. The translation agency losing clients to automatic translation gained 51 points. The food truck 72 hours from losing its permit gained 42.

Across all ten, the same AI scored 58% higher with the rulebook than with nothing. Here is the comparison that matters to anyone who already writes good prompts:

| Same AI, same situations | Score out of 100 |
|---|---|
| No instructions | 56.2 |
| A good generic consultant prompt | 67.7 |
| The model's canon and operating prompt | 88.8 |

That is 31% above a good generic prompt. A blind judge preferred the answer with the rules 30 times out of 30. Rule violations fell to zero in 120 blind reviews. Control quality doubled, from 4.2 to 8.3 out of 10. And the answers got shorter, from 501 to 454 words.

One detail is almost funny. The only invented fact in 120 reviews was copied from the prompt's own example sentence. The assistant did not make it up. It borrowed it.

## What six months of trusting the guess cost

Andrew's own story shows the cost without any AI in it. He believed his margin was about twenty per cent. It was 9%. That week he had planned a second barista and an advertising campaign, both resting on a margin that did not exist.

Feed that twenty per cent to an assistant, and it will build a handsome plan on it. Fast, tidy and wrong. Within a few months the money runs out, and no one understands why.

With a plan built on the honest 9%, the café reaches two months of reserve at month 10. Left as it was, at month 16. Six months of difference, decided by what you typed in.

## "Can I trust a test run by AI?"

Ask that question. The answer is in the limits. Ten scenarios, one model family, an AI judge; the method and the earlier round's full data are public on GitHub. Results with other assistants may differ.

The rule above does not ask you to trust the test. It asks you to keep your own log and to check the expensive answers by hand.

## Where the check stops

Be clear about what the check-it rule does. It treats a symptom: bad answers no longer slip through on expensive decisions.

The cause is still in place. The assistant invents and chooses because you have not given it two things. It has no order of goals, so it picks your priorities. It has no thresholds, so it cannot tell a yellow number from a red one.

Two steps close that gap.

- **The goal list in refusal order.** What you would give up first and what you defend last. Chapter 1.
- **The zone thresholds and the red protocol.** Where each number turns yellow or red, and what goes first when several are red. Chapter 4.

The free rulebook files, and how to load them step by step, are in [the ChatGPT prompt for business](/blog/chatgpt-prompt-for-business/). Without your goals and thresholds, even the best ChatGPT prompt for business is guessing about the two things only you know.

<div class="takeaways" markdown="1">
### Key takeaways

- Let AI notice, calculate and prepare. Keep the order of goals and the final choice.
- The further a job sits from "notice" and closer to "execute", the tighter the access.
- Check by hand when p × L is larger than the cost of checking.
- Ask for your gaps back. A wrong number means it did not use your data.
- A fluent answer is not a checked one.
</div>

## Two ways to use ChatGPT for small business

You have two choices. Keep asking the chatbot open questions and act on whatever sounds most confident. Or give it your goals, your numbers and a rule for what to check.

The check-it rule keeps the expensive mistakes out. The refusal order and the thresholds stop the assistant from guessing in the first place.

Test the logic for free: [Chapter 1, with the refusal test](/blog/free-sample/). Or get the full control system on Kindle, [on Amazon](https://www.amazon.com/dp/B0HPBR6BNX). It comes as a book, with the canon and the prompt printed as appendices.

## FAQ

### Should AI make business decisions?

It should prepare them, not make them. The safe way to use AI for business decisions is to let it compare numbers with goals, build scenarios and list options. You confirm the order of goals and take the final decision. Give it rights to act only with a log and your confirmation.

### What is the best ChatGPT prompt for business?

One that gives rules instead of a role. It sets what the assistant may say, how it works and what it must not decide. In a blind test, a rulebook scored 88.8 against 67.7 for a good generic consultant prompt.

### How do I check AI business advice?

Give it your goal and state numbers and ask for the gaps. If any figure differs from your own sum, restart. For costly decisions, check by hand whenever the chance of error times the cost is larger than the cost of checking.
