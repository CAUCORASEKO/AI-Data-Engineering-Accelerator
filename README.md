
## Overview

This project demonstrates a production-style Data Engineering pipeline implemented in Azure Databricks using Apache Spark (PySpark) and Delta Lake.

The pipeline follows the Bronze / Silver / Gold architecture and was executed and validated in a real Azure Databricks environment.

---

## Data Engineering Capabilities

- Apache Spark (PySpark)
- Delta Lake (ACID-compliant tables)
- Bronze / Silver / Gold modeling
- Data cleansing and standardization
- PII removal and governance
- Business aggregations
- SQL analytics over Delta tables

---

## Pipeline Architecture

Raw Parquet Dataset  
→ Bronze (Delta)  
→ Silver (Cleaned & Anonymized)  
→ Gold (Business Metrics)  
→ SQL Analytics

---

## Bronze Layer

- Raw ingestion from Parquet  
- Stored as Delta Lake  
- Full schema preserved including PII  

---

## Silver Layer

- Data cleansing  
- Lowercasing and trimming  
- PII removal (SSN)  
- Data quality enforcement  

---

## Gold Layer

- Aggregated business metrics  
- Optimized for analytics  
- Queryable via SQL  

---

## Gold Metrics

- Total people by gender  
- Average salary  
- Minimum salary  
- Maximum salary  

---

## Example SQL

SELECT
  gender,
  total_people,
  ROUND(avg_salary, 2) AS avg_salary
FROM ai_data_engineering.gold_people_metrics;

---

## Execution Evidence

- Pipeline executed in Azure Databricks  
- Delta tables created and registered  
- SQL queries executed successfully  

---

## Technologies

- Azure Databricks  
- Apache Spark  
- Delta Lake  
- SQL  
- Azure Cloud  

---

## Status

✔ Azure Databricks configured  
✔ Bronze / Silver / Gold implemented  
✔ Delta tables registered  
✔ SQL validated  

---

## License

MIT License




