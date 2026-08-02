# Data Ingestion Architecture v1

## Goal

Connect A-share watchlists, review exports, market data and research records into AI Research OS.

## Data Sources

- Watchlist: user selected stocks
- Daily review: JSON/CSV export
- Market data: price, volume, valuation metrics
- Company data: financial reports and announcements
- Research data: Agent outputs and reviews

## Flow

```
Raw Data
  ↓
Validation
  ↓
Normalization
  ↓
Research Database
  ↓
Agents
  ↓
Dashboard
```

## Rules

- Keep raw files immutable.
- Store source date and origin.
- Never overwrite historical research.
- Every decision must reference a research_id.
