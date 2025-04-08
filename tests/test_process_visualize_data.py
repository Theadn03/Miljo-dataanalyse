import pandas as pd
from src.process_data import process_and_clean_data

testdata = [
    {
        "Lokasjon": "Molde",
        "Tidspunkt": "2023-01-02T12:00:00+00:00",
        "Temperatur (°C)": 2.0,
        "Nedbør (mm)": 0.5,
        "Vindhastighet (m/s)": 3.2,
        "Luftfuktighet (%)": 85
    },
    {
        "Lokasjon": "Molde",
        "Tidspunkt": "2023-01-09T12:00:00+00:00",
        "Temperatur (°C)": None,
        "Nedbør (mm)": 0.0,
        "Vindhastighet (m/s)": 2.9,
        "Luftfuktighet (%)": 80
    }
]

def test_process_and_clean_data_interpolates():
    df = process_and_clean_data(testdata)
    assert not df.isnull().any().any(), "NaN values remain after interpolation"
    assert "Temperatur_C" in df.columns, "'Temperatur_C' column was not created"
    assert isinstance(df, pd.DataFrame), "Returned object is not a DataFrame"

# Visuell test (kjøres ikke automatisk av pytest, men for manuell kontroll)
from src.visualize_data import plot_temperature_trend

def test_plot_temperature_trend_shows_plot():
    df = process_and_clean_data(testdata)
    try:
        plot_temperature_trend(df)
    except Exception as e:
        assert False, f"Error during plotting: {e}"

