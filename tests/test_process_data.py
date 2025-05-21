# Denne renser data og håndterer NaN
import pandas as pd
from src.process_data import handle_missing_values

# Positiv test: gyldig input med en NaN-verdi
def test_process_and_clean_data_interpolates():
    testdata = [
        {"Location": "Molde", "Time": "2023-01-01", "Air temperature (°C)": 2.0},
        {"Location": "Molde", "Time": "2023-01-08", "Air temperature (°C)": None},
    ]
    df = handle_missing_values(testdata)
    assert not df.isnull().any().any()
    assert "Air temperature (°C)" in df.columns
    
# Negativ test: tomt input
def test_handle_missing_values_empty_input():
    df= handle_missing_values([])
    assert df.empty