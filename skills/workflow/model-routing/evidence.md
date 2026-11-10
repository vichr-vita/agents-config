# Model routing evidence

The data behind the rules in `SKILL.md`, gathered on 10 November 2026, one day after Fable 5.2 shipped. Update a rule here first when newer measurements contradict it.

Labels: **M** is an independent measurement, **V** is an Anthropic claim, **P** is a practitioner's opinion or single run.

## Prices

| Model | Input / output per 1M tokens (V) |
| --- | --- |
| Fable 5.2 | $8 / $40 |
| Opus 5.5 | $4 / $20 |
| Sonnet 5.5 | $2 / $10 |
| Haiku 5.5 | $0.10 / $0.50; $0.50 / $2.50 when the prompt exceeds 100K tokens |

Claude Code defaults every model to `medium` effort and the main session to Opus 5.5 (V, code.claude.com/docs/en/model-config). Anthropic publishes no per-model subscription burn rate. Fable is capped at 50% of the weekly limit and "uses them faster than other Claude models" (V, support.claude.com/en/articles/15424964).

## Cost and score by effort

Artificial Analysis Intelligence Index, score and API cost per task (M, artificialanalysis.ai/models/claude-{model}[-effort]):

| Model | low | medium | high | xhigh | max |
| --- | --- | --- | --- | --- | --- |
| Fable 5.2 | 54, $3.10 | 56, $3.80 | 62, $9.08 | 62, $14.83 | 65, $26.54 |
| Opus 5.5 | 35, $0.98 | 48, $2.45 | 52, $3.46 | 57, $6.05 | 59, $10.04 |
| Sonnet 5.5 | 26, $0.51 | 31, $0.78 | 42, $1.64 | 50, $4.09 | 55, $10.02 |
| Haiku 5.5 | 19, $0.04 | 25, $0.09 | 30, $0.16 | 35, $0.25 | 36, $0.41 |

CursorBench 4.0, coding score and cost per task (M, cursor.com/evals):

| Model | low | medium | high | xhigh | max |
| --- | --- | --- | --- | --- | --- |
| Fable 5.2 | 53.2, $3.94 | 54.8, $4.66 | 56.9, $9.70 | 56.3, $15.48 | 60.0, $32.79 |
| Opus 5.5 | 43.7, $1.17 | 52.5, $2.91 | 56.0, $3.97 | 56.0, $6.98 | 57.8, $13.43 |
| Sonnet 5.5 | 35.8, $0.37 | 39.2, $0.52 | 47.8, $1.20 | 53.1, $2.81 | 55.5, $7.05 |
| Haiku 5.5 | 30.9, $0.08 | 36.9, $0.17 | 42.3, $0.32 | 44.3, $0.56 | 48.4, $1.12 |

What the tables show:

- Going from `high` to `max` gains 1.8 CursorBench points on Opus and 3.1 on Fable, for 3.4 times the cost. Fable `xhigh` scores no better than Fable `high` on either index.
- Sonnet at `xhigh` or `max` is dominated by Opus one level lower on Artificial Analysis. Sonnet at `max` is dominated on both.
- Haiku at `high` or `xhigh` beats Sonnet at `low` or `medium` on both indexes for less money. It is slower, uses more tokens, and loses on judgment-heavy work (see Haiku below), so the rules give Haiku the mechanical work and Sonnet the rest.

## Haiku 5.5

- Codebase search: 36 read-only runs found every target with no invented paths. At `medium` a run cost $0.016 against $0.62 for Opus `medium`. `high` and `xhigh` added tokens without improving accuracy (M, aiviolabs.com/en/blog/haiku-5-5-as-a-subagent).
- Web extraction: in a blind test of 31 same-page extractions, Haiku at `high` lost 5 to 20 against Sonnet at `medium`, with 9 unsupported claims against 2 (M, GitHub PR dubbl-a/house-rules#340).
- Workers under an Opus orchestrator on defect search: Haiku workers scored F1 0.677, Sonnet workers 0.831 (V, anthropic.com/claude-haiku-5-5).
- Refusals: on Zapier AutomationBench, refusals rose from 13.2% at `low` to 37.0% at `max`, all labelled biology on ordinary business tasks (M, zapier.com/benchmarks/claude-haiku5_5-report). Refusals have no server-side fallback, and retrying "usually returns another refusal" (V, Haiku 5.5 prompting guide).
- At `low` it stops early and reports changes as done without checking (V, Haiku 5.5 prompting guide).

## Sonnet 5.5

- Anthropic's internal agentic coding set: Sonnet `medium` 62.7% at $0.16, Sonnet `high` 77.8% at $0.33, Opus `low` 74.8% at $0.35, Opus `medium` 86.6% at $0.84 (V, platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence).
- Vals Code Migration: 86.9%, first of 30. Opus 5.5 scored 81.0%, third (M, vals.ai).
- Long context: ProgramBench 79.7% against 91.2% for Opus (V). Factual recall: SimpleQA Verified 47% against 72% for Opus (M, Epoch).
- Code review: 6 of 13 hard cases at 41% precision, against 8 of 13 at 67% for Opus (M, coderabbit.ai/blog/sonnet-5-5-model-review).
- At `low` it reports changes as done without running a check. At every level it adds unrequested tests and docs (V, Sonnet 5.5 prompting guide).
- `cyber` and `frontier_llm` blocks fall back to Sonnet 5 when fallback is on. In the system card's prompt-injection test, 12% of rerouted requests were compromised, against 0.07% when Sonnet 5.5 answered (V, Sonnet 5.5 system card).

## Opus 5.5

- `low` scored 34 points below `medium` on Anthropic's defect-search benchmark, and 13.3 points below on DRACO research (V, optimizing-for-cost guide).
- Code review: `max` effort caught 62.5% against 63.8% at standard effort. "Turning up effort did not consistently produce a better review" (M, coderabbit.ai/blog/opus-5-5-model-review).
- SlopCodeBench: `medium` passed 28 tasks for $193, `xhigh` passed 25 for $817 (M, humanlayer benchmark write-up).
- `max` twice exhausted the 128K output limit while still reasoning and returned nothing (M, simonwillison.net/2026/Sep/22/opus-and-sol-and-luna).
- Arena WebDev: Opus 5.5 `max` 1813, second only to Fable 5.2 (M, arena.ai/leaderboard/webdev). Every calls design its clearest win (P).

## Fable 5.2

- Small-sample head-to-head: Fable caught a design hole in a passing fix in 4 of 4 runs, Opus in 1 of 4, at $41 against $17. On symptom-only bug reports at `medium`, Opus fixed 27 of 28 and Fable 23 of 28 (M, paddo.dev/blog/fable-5-2-vs-opus-5-5).
- Practitioners and Anthropic engineers agree it is strongest on long autonomous builds and gives little over Opus on ordinary coding. Theo's request logs put a $200 Ultra plan at about $15,000 of Opus usage against $3,000 of Fable (P, Latent Space AINews, 10 November 2026).
- Safeguards block most cybersecurity and research-biology tasks (V, anthropic.com/claude-fable-and-mythos-5-2).

## Delegation

Delegating to cheaper workers pays only for bulk or parallel work. On a single chain of dependent steps, the coordinator's model alone at a lower effort did better (V, claude-api skill, cost-optimization.md section 2.6). Eight Haiku searchers cost 51% more in total than one Sonnet searcher and were no faster, because the integrating agent's input grew (M, aiviolabs).
