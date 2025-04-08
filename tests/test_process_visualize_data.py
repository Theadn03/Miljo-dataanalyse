import pandas as pd
from src.process_data import process_and_clean_data

# -------------------------
# Dummy testdata for Molde
# -------------------------
# Består av to målinger:
# - én komplett
# - én med manglende temperatur, som skal interpoleres

testdata = [
    {
        "Location": "Molde",
        "Time": "2023-01-02T12:00:00+00:00",
        "Air temperature (°C)": 2.0,
        "Precipitation (mm)": 0.5,
        "Wind-speed (m/s)": 3.2,
        "Relative humidity (%)": 85
    },
    {
        "Location": "Molde",
        "Time": "2023-01-09T12:00:00+00:00",
        "Air temperature (°C)": None,  # Skal fylles med interpolasjon
        "Precipitation amount (mm)": 0.0,
        "Wind-speed (m/s)": 2.9,
        "Relative humidity (%)": 80
    }
]

# -------------------------
# Test: Interpolasjon og kolonnenavn
# -------------------------

# Sjekker at manglende verdier blir fylt inn (interpolert)
# og at funksjonen returnerer en gyldig DataFrame med korrekt kolonnenavn
def test_process_and_clean_data_interpolates():
    df = process_and_clean_data(testdata)
    
    # Sjekker at det ikke finnes noen manglende verdier igjen
    assert not df.isnull().any().any(), "NaN values remain after interpolation"
    
    # Sjekker at kolonnenavnet er endret som forventet
    assert "Temperatur_C" in df.columns, "'Temperatur_C' column was not created"
    
    # Sjekker at returverdien er en DataFrame
    assert isinstance(df, pd.DataFrame), "Returned object is not a DataFrame"


# -------------------------
# Visuell test: Plotting
# -------------------------
# Denne testen kjører ikke automatisk med pytest, men er nyttig for manuell kontroll
# Sjekker at visualiseringsfunksjonen kan kjøres uten å kaste feil

from src.visualize_data import plot_temperature_trend

def test_plot_temperature_trend_shows_plot():
    df = process_and_clean_data(testdata)
    try:
        plot_temperature_trend(df)
    except Exception as e:
        assert False, f"Error during plotting: {e}"
