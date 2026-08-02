# AI Research OS API Contract v1

## Research

GET /research/{id}

Returns:
- research summary
- agent outputs
- decision status
- review schedule

## Watchlist

GET /watchlist

Returns:
- ticker
- price
- research status
- risk alerts

## Daily Review

GET /daily-review/{date}

Returns:
- market events
- triggered agents
- generated insights

## Import

POST /import/market-data

Input:
- CSV
- JSON

Pipeline:
Raw Data -> Validation -> Normalization -> Database
