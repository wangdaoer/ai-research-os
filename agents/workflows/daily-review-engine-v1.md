# Daily Review Engine v1

## Goal

Convert daily A-share market changes into research events instead of simple price summaries.

## Pipeline

```text
Market Data Update
        ↓
Watchlist Scanner
        ↓
Event Detection
        ↓
Relevant Agent Trigger
        ↓
Daily Research Note
        ↓
Memory Update
        ↓
Review Queue
```

## Trigger Types

### Price Event
- Large price movement
- Volume abnormality
- Gap movement

### Fundamental Event
- Earnings release
- Guidance change
- Major operating update

### Industry Event
- Policy change
- Supply/demand shift
- Competitor action

### Thesis Event
- Previous assumption challenged
- Previous assumption confirmed

## Daily Output

Each review should contain:

- What changed today
- Why it changed
- Which research assumptions are affected
- Whether confidence changes
- Whether position needs review
- Next action

## Decision Rules

Price movement alone does not change investment thesis.

A thesis review is required when:

1. Fundamental assumptions change.
2. Competitive position changes.
3. Valuation changes materially.
4. Risk conditions are triggered.

