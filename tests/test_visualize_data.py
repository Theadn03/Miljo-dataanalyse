# Tester at visualiseringen kjører uten feil
import pandas as pd
from src.visualize_data import plot_temperature_trend


def test_plot_temperature_trend_runs():
    """
    Tester at plot_temperature_trend kjører uten å kaste exception.
    """
    data = pd.DataFrame({
        "Location": ["Molde"],
        "Time": pd.date_range(start="2023-01-01", periods=1),
        "elementId": ["mean(air_temperature P1D)"],
        "value": [5]
    })

    try:
        plot_temperature_trend(data)
    except Exception as e:
        assert False, f"Plotting failed: {e}"