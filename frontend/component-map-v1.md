# Dashboard Component Map v1

## Layout

```
App
├── OverviewPage
│   ├── MarketCard
│   ├── WatchlistAlertCard
│   ├── ReviewQueue
│   └── ResearchTimeline
│
├── StockPage
│   ├── ThesisPanel
│   ├── ScenarioChart
│   ├── AgentOpinionList
│   ├── RiskPanel
│   └── ReviewHistory
│
├── AgentPage
│   ├── AgentScoreCard
│   ├── AccuracyChart
│   └── ErrorAnalysis
│
└── KnowledgePage
    ├── InsightCard
    ├── RuleCard
    └── KnowledgeGraph
```

## Future Stack

Frontend can be implemented with React/Next.js and consume the Research API layer.

## Data Flow

API -> Components -> User Actions -> Research Updates
