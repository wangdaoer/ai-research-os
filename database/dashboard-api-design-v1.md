# Research Dashboard API Design v1

## Goal
为网站、Dashboard 和 Agent 提供统一数据接口。

## Core APIs

GET /companies
获取公司列表。

GET /research/{id}
获取完整研究记录。

GET /decisions
获取投资决策记录。

GET /reviews
获取复盘结果。

GET /insights
获取知识洞察。

## Dashboard Modules

1. 自选股监控
2. 研究状态
3. Agent评分
4. 风险提醒
5. 复盘统计
6. 知识图谱

## Future Integration

支持 JSON/CSV 导入，与 A 股复盘看板连接。
