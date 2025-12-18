# src/utils/generate_synthetic_dataset.py

import uuid
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Optional


def generate_transactions(
    n_transactions: int = 100_000,
    fraud_rate: float = 0.02,
    skew: float = 1.3,
    start_date: Optional[datetime] = None,
    seed: int = 42
) -> pd.DataFrame:
    """
    Generate a synthetic financial transactions dataset.

    Args:
        n_transactions: Number of transactions to generate
        fraud_rate: Probability of anomalous transaction
        skew: Lognormal skew for transaction amounts
        start_date: Optional start datetime
        seed: Random seed for reproducibility

    Returns:
        pandas.DataFrame
    """

    np.random.seed(seed)
    start_date = start_date or (datetime.utcnow() - timedelta(days=30))

    customers = [f"C{str(i).zfill(6)}" for i in range(50_000)]
    merchants = [f"M{str(i).zfill(5)}" for i in range(5_000)]
    channels = ["web", "app", "pos"]
    payment_methods = ["card", "sepa", "crypto"]
    countries = ["ES", "FR", "DE", "IT", "NL"]

    records = []

    for _ in range(n_transactions):
        is_anomaly = np.random.rand() < fraud_rate
        amount = np.random.lognormal(
            mean=4.0 if is_anomaly else 2.5,
            sigma=skew
        )

        records.append({
            "transaction_id": str(uuid.uuid4()),
            "customer_id": np.random.choice(customers),
            "merchant_id": np.random.choice(merchants),
            "timestamp": start_date + timedelta(
                seconds=int(np.random.uniform(0, 2_592_000))
            ),
            "amount": round(amount, 2),
            "currency": "EUR",
            "channel": np.random.choice(channels),
            "payment_method": np.random.choice(payment_methods),
            "country": np.random.choice(countries),
            "device_id": str(uuid.uuid4()),
            "ip_hash": str(uuid.uuid4()),
            "merchant_category_code": np.random.randint(1000, 5999),
            "risk_flags": int(is_anomaly),
            "anomaly_probable": int(is_anomaly)
        })

    return pd.DataFrame(records)


if __name__ == "__main__":
    df = generate_transactions(n_transactions=10_000)
    df.to_csv("synthetic_transactions.csv", index=False)