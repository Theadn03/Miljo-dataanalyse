import pandas as pd
from src.process_data import handle_missing_values


def test_process_and_clean_data_interpolates():
    """
    Positive test:
    Verifies that missing values in the 'Air temperature (°C)' column are handled properly
    via interpolation, and that the cleaned DataFrame contains no NaNs.

    Expected behavior:
    - No NaNs remain in the result
    - Column 'Air temperature (°C)' is preserved
    """
    testdata = pd.DataFrame([
        {"Location": "Molde", "Time": "2023-01-01", "Air temperature (°C)": 2.0},
        {"Location": "Molde", "Time": "2023-01-08", "Air temperature (°C)": None},
    ])
    
    df = handle_missing_values(testdata)
    
    assert not df.isnull().any().any()
    assert "Air temperature (°C)" in df.columns


def test_handle_missing_values_empty_input():
    """
    Negative test:
    Ensures that passing an empty input results in an empty DataFrame being returned.

    Expected behavior:
    - Output DataFrame is empty
    """
    df = handle_missing_values(pd.DataFrame([]))
    assert df.empty