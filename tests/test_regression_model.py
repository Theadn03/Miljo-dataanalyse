# Tester at regresjonsmodellen faktisk trenes og gir output som forventet
from src.regression_model import train_model_for_city
import pandas as pd

# Positiv test: et lite gyldig datasett med riktige elementId-verdier
def test_train_model_for_city_output():
    data = pd.DataFrame({
        "Location": ["Molde"] * 9,
        "Time": pd.to_datetime([
            "2023-01-01"]*3 + ["2023-01-02"]*3 + ["2023-01-03"]*3
        ),
        "elementId": [
            "mean(air_temperature P1D)", "sum(precipitation_amount P1D)", "mean(relative_humidity P1D)",
            "mean(air_temperature P1D)", "sum(precipitation_amount P1D)", "mean(relative_humidity P1D)",
            "mean(air_temperature P1D)", "sum(precipitation_amount P1D)", "mean(relative_humidity P1D)"
        ],
        "value": [5, 2, 85, 6, 3, 80, 7, 1, 90]
    })

    model, y_test, y_pred = train_model_for_city(data, "Molde")
    assert hasattr(model, "predict")
    assert len(y_test) == len(y_pred)

# Negativ test: tom dataframe
def test_train_model_for_city_empty():
    df = pd.DataFrame(columns=["Location", "Time", "elementId", "value"])
    try:
        train_model_for_city(df, "Molde")
        assert False, "Function should fail on empty input"
    except ValueError:
        pass