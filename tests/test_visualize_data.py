# Tester at visualiseringen kjører uten feil
from src.visualize_data import plot_temperature_trend
import pandas as pd

# Positiv test: gir korrekt formatert dataframe
def test_plot_temperature_trend_runs():
    data = pd.DataFrame ({
        "Location": ["Molde"],
        "Time": pd.date_range(start="2023-01-01", periods=1),
        "elementId": ["mean(air_temperature P1D)"],
        "value": [5]
    })
    try:
        plot_temperature_trend(data)
    except Exception as e:
        assert False, f"Plotting failed: {e}"