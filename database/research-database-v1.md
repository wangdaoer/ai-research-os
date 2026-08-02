# Research Database v1

## Purpose
统一管理公司、行业、研究、决策、复盘和规则资产。

## Entity Model

Company
- ticker
- name
- sector
- research_ids
- insights

Research
- research_id
- question
- date
- agents
- conclusion
- confidence

Decision
- action
- position
- risk
- invalidation
- review_date

Review
- result
- logic_result
- lessons
- new_rules

## Design Principles

1. 原始研究不可覆盖，只能追加版本。
2. 每个结论必须关联 research_id。
3. 每个决策必须有失效条件。
4. 每次复盘必须产生知识沉淀。
