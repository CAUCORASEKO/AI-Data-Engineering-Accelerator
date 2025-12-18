
-- =========================================================
-- Azure Databricks SQL Analytics
-- Gold Layer Consumption
--
-- Source: ai_data_engineering.gold_people_metrics
-- Executed in Azure Databricks
-- =========================================================

-- Inspect full Gold table
SELECT *
FROM ai_data_engineering.gold_people_metrics;

-- Aggregated business view
SELECT
  gender,
  total_people,
  ROUND(avg_salary, 2) AS avg_salary
FROM ai_data_engineering.gold_people_metrics;