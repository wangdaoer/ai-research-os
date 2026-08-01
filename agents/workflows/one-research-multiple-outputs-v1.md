# One Research, Multiple Outputs v1

## 目标

将一次经过 QA 的研究，转化为投资决策、知识沉淀和内容资产，而不重复研究。

## 唯一事实源

所有衍生内容必须引用同一个 `research_id`。投资版本为主记录，其他输出不得新增未经验证的事实。

## 输入
- approved research record
- QA report
- source list
- audience profiles
- disclosure and compliance constraints

## 输出流水线

```text
Approved Research Record
  ├─ Investment Report
  ├─ Decision Record
  ├─ Research Memory Update
  ├─ Insight Cards
  ├─ Candidate Research Rules
  ├─ X Long Thread
  ├─ WeChat Long-form Article
  ├─ Short Knowledge Cards
  ├─ Video Script
  └─ Review / Backtest Task
```

## 输出标准

### 1. 投资报告
保留完整证据、市场共识、预期差、情景概率、估值、风险和仓位。不得为了可读性删除重大反方证据。

### 2. 决策记录
使用 `schemas/decision-record.schema.json`。只有人工批准后，`human_approval` 才能设为 true。

### 3. 研究记忆
使用 `schemas/research-memory.schema.json` 追加事件。不得覆盖历史 thesis。

### 4. Insight Cards
每张卡只表达一个可复用洞察，必须关联证据与适用边界。

### 5. Research Rules
初次提出的规则状态必须为 `candidate`。除非得到多条独立证据或回测支持，不得升级为 `active`。

### 6. X 长帖
重点是清晰、可传播和有观点；必须区分事实、推断和个人框架，不得伪装成投资建议。

### 7. 公众号长文
保留完整论证链，增加背景、案例和反方观点，不得复制原始来源的大段文字。

### 8. 视频脚本
围绕一个核心问题展开，必须保留关键限定条件和风险提示。

### 9. 复盘任务
按研究期限自动生成复核日期，并关联原始 `research_id` 和 `decision_id`。

## 内容一致性检查

发布前检查：
1. 数字是否与主研究记录一致；
2. 是否遗漏重要风险；
3. 是否把概率判断改写成确定事实；
4. 是否改变原始时间周期；
5. 是否加入了未验证的新结论；
6. 是否保留来源和研究日期；
7. 投资内容与公众内容是否有清晰边界。

## 资产命名

```text
research/{year}/{research_id}/report.md
data/research-history/{research_id}.json
data/decisions/{decision_id}.json
knowledge/insights/{insight_id}.md
knowledge/rules/{rule_id}.md
content/x/{research_id}.md
content/wechat/{research_id}.md
content/video/{research_id}.md
reviews/{review_id}.json
```

## 原则

一次研究可以产生多种表达，但只能有一个经过审核的事实基础。传播效率不得以牺牲研究准确性为代价。
