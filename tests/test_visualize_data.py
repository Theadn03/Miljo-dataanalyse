# Test that the temperature plot function runs without throwing exceptions
import pandas as pd
from src.visualize_data import plot_temperature_trend


def test_plot_temperature_trend_runs():
    """
    Smoke test:
    Verifies that the 'plot_temperature_trend' function runs without raising an exception
    when provided with minimal valid input data.

    This test does not validate the correctness of the plot output,
    only that no runtime errors occur.
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