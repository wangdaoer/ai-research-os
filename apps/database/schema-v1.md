# Research Database Schema v1

## Core Tables

## companies

- company_id
- ticker
- name
- sector
- tags

## research_records

- research_id
- company_id
- created_at
- horizon
- thesis
- confidence
- status

## agent_outputs

- output_id
- research_id
- agent_name
- conclusion
- evidence
- confidence

## decisions

- decision_id
- research_id
- action
- position
- risk
- invalidation

## reviews

- review_id
- research_id
- review_date
- result
- lessons

## rules

- rule_id
- source_research
- content
- validation_status
