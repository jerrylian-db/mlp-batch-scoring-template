"""
This module defines the following routines used by the 'preprocessing' step of the batch
scoring pipeline:

- ``process_data``: Defines customizable logic for processing & cleaning the dataset produced by the
ingest step.
"""

from pandas import DataFrame


def process_data(
    ingest_df: DataFrame
) -> DataFrame:
    """
    Perform additional processing on the split datasets.

    :param train_df: The training dataset produced by the data splitting procedure.
    :param validation_df: The validation dataset produced by the data splitting procedure.
    :param test_df: The test dataset produced by the data splitting procedure.
    :return: A tuple containing, in order: the processed training dataset, the processed
             validation dataset, and the processed test dataset.
    """

    def process(df: DataFrame):
        # Drop invalid data points
        cleaned = df.dropna()
        # Filter out invalid fare amounts and trip distance
        cleaned = cleaned[
            (cleaned["fare_amount"] > 0)
            & (cleaned["trip_distance"] < 400)
            & (cleaned["trip_distance"] > 0)
            & (cleaned["fare_amount"] < 1000)
        ]

        cleaned["pickup_dow"] = cleaned["tpep_pickup_datetime"].dt.dayofweek
        cleaned["pickup_hour"] = cleaned["tpep_pickup_datetime"].dt.hour
        trip_duration = (
            cleaned["tpep_dropoff_datetime"] - cleaned["tpep_pickup_datetime"]
        )
        cleaned["trip_duration"] = trip_duration.map(lambda x: x.total_seconds() / 60)

        return cleaned

    return process(ingest_df)
