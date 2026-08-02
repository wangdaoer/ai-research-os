# A股数据接入层 v1

目标：将自选股、复盘数据、行情数据统一接入 AI Research OS。

流程：

CSV/JSON 导入
→ 数据校验
→ 字段标准化
→ Research Database
→ Agent 分析
→ Dashboard

核心要求：

- 保留原始数据
- 记录来源和时间
- 不覆盖历史版本
- 数据变化触发研究任务
