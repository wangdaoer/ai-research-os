# AI Research OS API MVP

## Goal

Provide local API services for research records, watchlists, data import and daily review.

## Modules

- research: query and manage research records
- watchlist: manage tracked stocks
- import: ingest CSV/JSON market data
- review: daily review tasks
- agent_service: trigger research workflows

## MVP Endpoints

GET /research/{research_id}
GET /watchlist
GET /daily-review/{date}
POST /import/market-data

## Runtime

FastAPI service. Initial storage can use SQLite, later migrate to PostgreSQL.
