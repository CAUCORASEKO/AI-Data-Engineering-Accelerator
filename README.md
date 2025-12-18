# AI Data Engineering Accelerator
## Financial Transactions Anomaly Detection (Azure + Databricks)

## Overview

This repository demonstrates how a **Data Engineer** can design, scale, and govern
**AI-powered financial data pipelines** using **Azure and Databricks**, with a strong
focus on:

- Scalability
- Security & compliance
- Traceability & auditability
- Productivity for analytics and AI consumers

The project uses **synthetic financial transactions** to showcase an **end-to-end
architecture** from ingestion to **anomaly detection model serving**.

> ⚠️ This project uses **synthetic data only**. No real customer or financial data is included.

---

## Architecture (High-Level)

```
Synthetic Data
     |
     v
ADLS Gen2 (Bronze)
     |
     v
Databricks (PySpark)
     |
     v
ADLS Gen2 (Silver - Anonymized)
     |
     v
ADLS Gen2 (Gold - Features)
     |
     v
MLflow (Model Registry)
     |
     v
Azure AI Endpoint (Secure Serving)
     |
     v
Consumers (Databricks Notebooks / Agents)
```

---

## Core Capabilities

### Data Engineering
- High-volume synthetic transaction generation
- Bronze / Silver / Gold data layering
- PySpark-based transformations
- Feature engineering for anomaly detection

### Security & Compliance
- Deterministic hashing with salt
- Data masking for sensitive fields
- No PII exposure beyond Bronze
- RBAC-ready architecture
- Secrets managed via Azure Key Vault and Databricks Secrets

### Machine Learning
- Anomaly detection using Isolation Forest or Autoencoders
- MLflow tracking and model versioning
- Reproducible training pipelines
- Secure model serving via Azure AI

### Auditability & Governance
- Prediction-level audit logging
- Traceable transaction and request IDs
- Model version tracking per prediction
- GDPR-friendly design (minimization and anonymization)

---

## Repository Structure

```
AI-Data-Engineering-Accelerator/
│── notebooks/
│   ├── data_ingestion_databricks.ipynb
│   ├── transformations_anonymization.ipynb
│   ├── anomaly_detection_model.ipynb
│   ├── model_serving_and_consumption.ipynb
│
│── src/
│   └── utils/
│       ├── generate_synthetic_dataset.py
│       ├── anonymization.py
│       ├── apply_anonymization.py
│       └── audit_logger.py
│
│── azure_ai/
│   └── deployment_scripts/
│       └── deploy_endpoint.py
│
│── conf/
│   └── sample_config.yaml
│
│── tests/
│   ├── test_anonymization.py
│   └── test_inference_logging.py
│
│── docs/
│   ├── architecture_diagram.md
│   └── compliance_notes.md
│
│── README.md
```

---

## Dataset

Synthetic financial transactions with the following fields:

- transaction_id
- customer_id (hashed in Silver layer)
- merchant_id
- timestamp
- amount
- currency
- channel (web / app / pos)
- payment_method (card / sepa / crypto)
- country
- device_id (masked)
- ip_hash (hashed)
- merchant_category_code
- risk_flags (synthetic)
- anomaly_probable (semi-supervised label)

---

## Local Development

### Prerequisites
- Python 3.10+
- Git
- macOS / Linux (Windows WSL supported)

### Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Generate Synthetic Data

```
python src/utils/generate_synthetic_dataset.py
```

### Apply Anonymization (Silver Layer)

```
PYTHONPATH=. python src/utils/apply_anonymization.py
```

### Run Tests

```
PYTHONPATH=. pytest tests/
```

---

## Databricks & Azure Execution

This project is designed to run end-to-end in Azure:

- Storage: Azure Data Lake Storage Gen2
- Compute: Azure Databricks
- ML: MLflow Model Registry
- Serving: Azure AI Online Endpoints

Execution steps are documented in the Databricks notebooks and `docs/` folder.

---

## Compliance Notes

- No raw PII used beyond Bronze layer
- Deterministic anonymization for traceability
- No secrets committed to the repository
- Synthetic data only
- Audit logs persisted in Delta tables

See `docs/compliance_notes.md` for details.

---

## Future Enhancements

- Streaming ingestion (Event Hubs)
- Real-time inference
- Feature Store integration
- Online learning
- CI/CD for ML pipelines
- Unity Catalog fine-grained access control

---

## License

This project is licensed under the MIT License.