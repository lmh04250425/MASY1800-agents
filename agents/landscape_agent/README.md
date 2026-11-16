# Emerging Technology Landscape Agent

Assignment 8 (Lab 8 - SubAgent 7 Landscape), the final specialist. Specialist version 1.1. Student: Minghan Liu.

Governing question: *where does this emerging technology and application sit in the current technology landscape, and what signals should this organization monitor next?*

The agent produces a **dated** landscape in three layers:
- broad (the same for the same technology);
- application (the same for the same application);
- organizational relevance.

It rates ten dimensions with a **flip test**: is a signal DECISION-RELEVANT, WATCH or BACKGROUND for this organization and horizon? It types every piece of evidence (vendor / industry / independent / standard-reg / organization / inference), grades it and gives it a refresh class. It gives no single score. It writes triggers with cadence and thresholds, and it names and refreshes one stale claim.

## Current answer (as of 2026-11-15)

| Case | Most decision-relevant development | Strongest alternative | Regulation tier |
|---|---|---|---|
| NYU SPS | Vendor convergence: agent features arriving in the platforms SPS already uses | Chatbot over approved content + staff + self-scheduling link | WATCH |
| Coding agents (application contrast) | Measured vs perceived productivity (saturated vendor benchmarks vs a randomized trial) | Existing IDE assistant + code review | BACKGROUND |
| EU university (organization contrast) | Vendor scope creep meeting the EU high-risk boundary | Same as SPS | DECISION-RELEVANT |
| Hype probe | Unchanged from SPS; five headlines typed; proof of concept kept | — | — |

**Stale claim:** E11's "30% of tasks" is now 42.9% on the same benchmark (D35), and the leaderboard itself lags.

## Run

From the repository root, using Python 3 with the standard library only (no API key):

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/landscape_agent --case agents/landscape_agent/cases/primary.json
# paste work/... into ChatGPT, ask for JSON only, save as a NEW file, then:
python3 tools/validate_response.py PATH_TO_NEW_RESPONSE.json
python3 agents/landscape_agent/tests/verify_package.py
```

## Package map

| Path | Contents |
|---|---|
| `specialist_instructions.md` | v1.1 procedure, dimensions, rules and the typed register |
| `cases/` | primary, contrast_1 (coding), contrast_2 (EU university), hype_probe |
| `responses/` | final v1.1 outputs |
| `tests/cycle_1/`, `tests/cycle_2/` | instructions, outputs, reviews and hash manifests (cycle 1 failures preserved) |
| `tests/prompts/` | the exact packets |
| `tests/verify_package.py`, `validation_log.txt` | 31 checks |
| `evidence/source_register.json` | 31 sources, each with an evidence class, refresh class and dates |
| `records/` | landscape framework, signal filter, stale claim, course alignment, team handoff (with the integration requirements), Agent Record (markdown) |
| `submission/` | the Word Agent Record and a checklist |

## Limits

- The prompt packets were run with Claude in place of ChatGPT, and generation and review occurred in the same session (not blinded).
- Two organizations are synthetic.
- Some sources are secondary summaries or mirrors.
- No adoption rate exists for agents in admissions.
- US and New York rules on AI in admissions are not assessed.
- Legal points are flagged for counsel.
