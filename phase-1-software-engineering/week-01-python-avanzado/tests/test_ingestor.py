"""
Tests unitarios para GenericAsyncIngestor
"""
import pytest
from src.ingestor import GenericAsyncIngestor, DataRecord

def test_data_record_validation():
    payload = {"id": 1, "title": "Test Item", "body": "Sample body"}
    record = DataRecord(**payload)
    assert record.id == 1
    assert record.title == "Test Item"
