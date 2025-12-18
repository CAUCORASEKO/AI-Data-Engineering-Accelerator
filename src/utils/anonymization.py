# src/utils/anonymization.py

import hashlib
from typing import Optional


def _hash_value(value: str, salt: str) -> str:
    """
    Deterministic SHA-256 hash with salt.
    """
    return hashlib.sha256(f"{value}:{salt}".encode("utf-8")).hexdigest()


def mask_device_id(device_id: str) -> str:
    """
    Mask last characters of device_id.
    """
    if not device_id:
        return None
    return device_id[:-6] + "******"


def anonymize_record(
    record: dict,
    salt: str
) -> dict:
    """
    Anonymize a single transaction record.

    Fields anonymized:
    - customer_id → hash
    - ip_hash → hash
    - device_id → masked
    """

    anonymized = record.copy()

    anonymized["customer_id_hash"] = _hash_value(
        record["customer_id"], salt
    )

    anonymized["ip_hash"] = _hash_value(
        record["ip_hash"], salt
    )

    anonymized["device_id_masked"] = mask_device_id(
        record.get("device_id")
    )

    # Remove raw PII
    anonymized.pop("customer_id", None)
    anonymized.pop("device_id", None)

    return anonymized