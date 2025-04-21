# Tester at regresjonsmodellen faktisk trenes og gir output som forventet
from regression_model import train_model_for_city
import pandas as pd

def test_train_model_for_city_output():
    dummy_data = pd.DataFrame({
        "Location": ["Molde"] * 4,
        "Time": pd.date_range(start="2023-01-01", periods=4, freq="D"),
        "elementId": ["mean(air_temperature P1D)", "sum(precipitation_amount P1D)",
                      "mean(relative_humidity P1D)", "mean(relative_humidity P1D)"],
        "value": [3.0, 1.2, 85, 90]
    })

    try:
        model, y_test, y_pred, x_test = train_model_for_city(dummy_data, "Molde")
        assert hasattr(model, "predict")
        assert len(y_test) == len(y_pred)
    except Exception as e:
        assert False, f"train_model_for_city() failed: {e}"