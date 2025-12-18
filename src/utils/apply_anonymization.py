# src/utils/apply_anonymization.py

import pandas as pd
from src.utils.anonymization import anonymize_record

SALT = "local-demo-salt"


def anonymize_csv(
    input_path: str,
    output_path: str
):
    """
    Apply anonymization logic to a CSV file (Silver layer).
    """
    df = pd.read_csv(input_path)

    anonymized_records = []
    for _, row in df.iterrows():
        anonymized_records.append(
            anonymize_record(row.to_dict(), SALT)
        )

    pd.DataFrame(anonymized_records).to_csv(
        output_path,
        index=False
    )


if __name__ == "__main__":
    anonymize_csv(
        "synthetic_transactions.csv",
        "synthetic_transactions_silver.csv"
    )