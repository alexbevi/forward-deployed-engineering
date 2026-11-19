# Cost per task for coding agents

[Read the article](https://aws.amazon.com/blogs/machine-learning/how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-amazon-bedrock/).

Airbnb evaluates seven private suites, recording scores and token cost per attempt, including low-scoring runs. Dated public rates price uncached input, cache reads, cache writes and output across all requests. Scores and costs set model defaults and reasoning ceilings.

Model A had more expensive requests and users sent more of them; cached context dominated request cost. For a cohort of heavy users, migration reportedly cut spend on its main model to roughly one seventh in the first full week, with similar request counts. These are list-price estimates, without accepted delivery outcomes.

Model identities, actual campaign repetitions, cohort size and grader calibration are undisclosed. Human review, task authoring, repair and maintenance are outside the token metric. No matched production task mix is reported, preventing productivity or total-cost conclusions.

## Connections and verification

[Agentic Development](../Agentic%20Development.md) distinguishes evaluation economics from production usage. The joint Airbnb/AWS account is shared commercial provenance, not independent corroboration. [FDE](../FDE.md) and [Staff Engineer](../Staff%20Engineer.md) remain unchanged; the source does not establish role-specific practices.

Full article text, byline, visible date, canonical URL and publication/modification metadata were reviewed on November 19, 2026. The example configuration specifies one attempt per task and effort; actual campaign repetition counts are not established. Full suites, graders, token logs and billing records were not inspected, and no runs were reproduced locally.

## Record metadata

| Property | Value |
| --- | --- |
| type | article |
| collection | agentic-development |
| title | How Airbnb uses cost per task to operate coding agents on Amazon Bedrock |
| author | Alan Yao; Rashim Gupta; Sang Kong; Jayadev Vadakkanmarveettil |
| author_affiliations | Airbnb and AWS, as stated in the author biographies |
| site | AWS Artificial Intelligence Blog |
| url | https://aws.amazon.com/blogs/machine-learning/how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-amazon-bedrock/ |
| canonical_url | https://aws.amazon.com/blogs/machine-learning/how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-amazon-bedrock/ |
| publication_date | 2026-11-18 |
| publication_date_basis | Visible article date and article:published_time |
| source_updated | 2026-11-18 |
| source_updated_basis | article:modified_time |
| accessed | 2026-11-19 |
| created | 2026-11-19 |
| updated | 2026-11-19 |
| status | reviewed |
| source_kind | vendor-case-study |
| evidence_family | aws-airbnb-bedrock-coding-agents-2026 |
| evidence_basis | reported-experience; reported-experiment |
| contribution | Distinguishes evaluation token costs from production usage and actual billing |
| tags | agentic-development; agentic-development/verification; agentic-development/economics |
| themes | [Agent harnesses and verification](../Themes/Agent%20harnesses%20and%20verification.md) |
| approaches |  |
| playbooks |  |
| resources |  |
| people |  |
| models |  |
| role_applications |  |
