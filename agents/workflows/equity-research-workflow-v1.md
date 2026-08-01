# Equity Research Workflow v1

## Pipeline

```text
Research Request
  ↓
Research Manager: scope and input validation
  ↓
Parallel Research
  ├─ Fundamental Agent
  ├─ Industry Agent
  ├─ Valuation Agent
  └─ Market Agent
  ↓
Bear Agent: independent challenge
  ↓
Research Manager: conflict matrix and synthesis
  ↓
Portfolio Agent: action and position sizing
  ↓
QA Agent: evidence and calculation gate
  ↓
Human Approval
  ↓
Research Database + Tracking + Review
```

## Input Contract
- research_id
- ticker/company
- research_date
- decision_horizon
- decision_question
- available_sources
- current_price and price_date
- portfolio_constraints

## Quality Gates
### Gate 1 — Input
Reject when the company, date, research horizon or decision question is missing.

### Gate 2 — Evidence
Every material claim must be tagged as fact, estimate, opinion or hypothesis. Critical facts require source and date.

### Gate 3 — Scenario
Bull/base/bear probabilities must total 100%; all scenarios require explicit assumptions and target values.

### Gate 4 — Risk
No action recommendation without downside analysis, invalidation conditions and a Bear Agent review.

### Gate 5 — Portfolio
Position sizing must account for confidence, downside, liquidity, correlation and concentration.

### Gate 6 — QA
Hard-fail issues block publication and must route back to the responsible Agent.

## Conflict Handling
- Preserve conflicting conclusions in the record.
- Weight evidence quality and independence, not the number of agreeing Agents.
- Shared sources do not count as independent confirmation.
- Unresolved material conflict lowers confidence and position size.

## Versioning
- Raw Agent outputs are immutable.
- Synthesis and decisions use version numbers.
- Updates append new records and reference prior research_id/version.
- Post-review changes must never rewrite the original thesis.

## Minimum Final Record
The final approved output must comply with `schemas/research-record.schema.json` and include market consensus, key disagreement, scenarios, expected return, downside, position, invalidation conditions, review date and QA status.