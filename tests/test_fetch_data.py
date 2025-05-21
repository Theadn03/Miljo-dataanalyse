import os
from datetime import datetime

import pytest
from dotenv import load_dotenv
from src.fetch_data import fetch_data_from_frost


def test_fetch_data_valid_input():
    """
    Positive test: Fetches data using valid client ID and station ID.
    """
    load_dotenv()
    client_id = os.getenv("API-KEY")
    stations = {"Molde": "SN62295"}
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 2)

    data = fetch_data_from_frost(client_id, stations, start, end)
    assert isinstance(data, list)


def test_fetch_data_invalid_station():
    """
    Negative test: Returns empty list for unknown station ID.
    """
    load_dotenv()
    client_id = os.getenv("API-KEY")
    stations = {"Unknown": "SN00000"}  # Nonexistent station
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 2)

    data = fetch_data_from_frost(client_id, stations, start, end)
    assert data == []