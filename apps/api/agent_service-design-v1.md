# Agent Service Design v1

## Purpose

Connect research workflows with API layer.

## Flow

Request
→ Research Manager
→ Parallel Agents
→ Synthesis
→ Decision Record
→ Review Task

## Inputs

- research_id
- ticker
- research_question
- horizon
- data_sources

## Outputs

- agent_outputs
- confidence
- evidence
- risks
- decision_candidate

## Rules

- Keep raw agent outputs immutable.
- Store every run with version id.
- Require evidence before publishing conclusions.
