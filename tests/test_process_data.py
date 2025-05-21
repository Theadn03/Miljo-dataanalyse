import pandas as pd
from src.process_data import handle_missing_values


def test_process_and_clean_data_interpolates():
    """
    Tester at en NaN-verdi i temperaturkolonnen blir håndtert korrekt.
    """
    testdata = [
        {
            "Location": "Molde",
            "Time": "2023-01-01",
            "Air temperature (°C)": 2.0
        },
        {
            "Location": "Molde",
            "Time": "2023-01-08",
            "Air temperature (°C)": None
        },
    ]
    df = handle_missing_values(testdata)
    assert not df.isnull().any().any()
    assert "Air temperature (°C)" in df.columns


def test_handle_missing_values_empty_input():
    """
    Tester at funksjonen returnerer en tom DataFrame ved tom input.
    """
    df = handle_missing_values([])
    assert df.empty