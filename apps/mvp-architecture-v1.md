# AI Research OS MVP Architecture v1

## Goal

Build a local-first AI investment research workspace.

## Stack

- Frontend: Next.js + React
- Backend: FastAPI
- Database: SQLite first, PostgreSQL later
- Data input: JSON / CSV
- AI layer: Agent workflow

## MVP Modules

### Dashboard
- Market overview
- Watchlist
- Research queue
- Alerts

### Stock Research
- Research Card
- Agent outputs
- Bull/Base/Bear scenarios
- Decision record

### Data Import
- CSV import
- JSON import
- Validation
- Normalization

### Review Engine
- Daily review
- Thesis tracking
- Rule updates

## Development Order

1. Database models
2. API endpoints
3. Frontend pages
4. Data importer
5. Agent integration
6. Dashboard visualization
