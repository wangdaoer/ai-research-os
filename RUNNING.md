# AI Research OS — Runnable MVP

## Start with Docker

```bash
git clone https://github.com/wangdaoer/ai-research-os.git
cd ai-research-os
git checkout agent/build-runnable-mvp
docker compose up --build
```

Open:

- Dashboard: http://localhost:3000
- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

The API creates the PostgreSQL schema on startup and seeds two research cases:

- `300458` 全志科技
- `300750` 宁德时代

## API examples

```bash
curl http://localhost:8000/research
curl http://localhost:8000/research/300458
```

Create a new research record:

```bash
curl -X POST http://localhost:8000/research \
  -H 'Content-Type: application/json' \
  -d '{"ticker":"000001","company":"平安银行","thesis":"盈利质量与估值是否匹配"}'
```

## Current scope

This Alpha validates the vertical slice:

`Next.js dashboard → FastAPI → PostgreSQL → research records`

Agent outputs are seeded research records in this release. Live market data and model execution remain intentionally out of scope until the product flow is validated.
