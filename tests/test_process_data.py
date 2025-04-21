# Denne renser data og håndterer NaN
import pandas as pd
from src.process_data import process_and_clean_data

# Positiv test: gyldig input med en NaN-verdi
def test_process_and_clean_data_interpolates():
    testdata = [
        {"Location": "Molde", "Time": "2023-01-01", "Air temperature (°C)": 2.0},
        {"Location": "Molde", "Time": "2023-01-08", "Air temperature (°C)": None},
    ]
    df = process_and_clean_data(testdata)
    assert not df.isnull().any().any()
    assert "Air temperature (°C)" in df.columns
    
# Negativ test: tomt input
def test_process_and_clean_data_empty_input():
    df= process_and_clean_data([])
    assert df.empty