import pytest
import os
import pandas as pd
from pandas import DataFrame
from steps.data_clean import clean


@pytest.fixture
def sample_data():
    return pd.read_parquet(
        os.path.join(os.path.dirname(__file__), "test_sample.parquet")
    )


def test_preprocessing_fn_returns_datasets_with_correct_spec(sample_data):
    ingest_data = sample_data
    ingest_processed = process_data(ingest_data)
    assert isinstance(ingest_processed, DataFrame)


def test_preprocessing_fn_returns_non_empty_datasets(sample_data):
    ingest_data = sample_data
    ingest_processed = process_data(ingest_data)

    assert not ingest_processed.empty
