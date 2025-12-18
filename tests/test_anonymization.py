# tests/test_anonymization.py

from src.utils.anonymization import anonymize_record


def test_anonymization_removes_pii():
    record = {
        "customer_id": "C000123",
        "device_id": "device-abcdef123456",
        "ip_hash": "192.168.1.1",
        "amount": 100.0
    }

    anonymized = anonymize_record(record, salt="test_salt")

    assert "customer_id" not in anonymized
    assert "device_id" not in anonymized
    assert "customer_id_hash" in anonymized
    assert "device_id_masked" in anonymized


def test_hash_is_deterministic():
    record = {
        "customer_id": "C000123",
        "device_id": "x",
        "ip_hash": "1.1.1.1"
    }

    a1 = anonymize_record(record, salt="same_salt")
    a2 = anonymize_record(record, salt="same_salt")

    assert a1["customer_id_hash"] == a2["customer_id_hash"]