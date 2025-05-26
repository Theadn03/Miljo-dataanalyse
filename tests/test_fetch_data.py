import os
from datetime import datetime

import pytest
from dotenv import load_dotenv
from src.fetch_data import fetch_data_from_frost


def test_fetch_data_valid_input():
    """
    Positive test:
    Verifies that the function returns a list of observations when called
    with a valid API key and a known weather station ID.

    Expected behavior:
    - The function returns a list (possibly non-empty).
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
    Negative test:
    Ensures that an unknown or invalid station ID results in an empty list,
    rather than raising an exception or returning malformed data.

    Expected behavior:
    - The function returns an empty list.
    """
    load_dotenv()
    client_id = os.getenv("API-KEY")
    stations = {"Unknown": "SN00000"}  # Invalid or non-existent station
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 2)

    data = fetch_data_from_frost(client_id, stations, start, end)
    assert data == []