# Test that the regression model is properly trained and produces predictions
import pandas as pd
from src.regression_model import train_model_for_city


def test_train_model_for_city_output():
    """
    Positive test:
    Verifies that the regression model is trained correctly with minimal valid input.
    
    Expected behavior:
    - The returned model has a 'predict' method
    - The length of predicted and actual target arrays match
    """
    data = pd.DataFrame({
        "Location": ["Molde"] * 9,
        "Time": pd.to_datetime(
            ["2023-01-01"] * 3 +
            ["2023-01-02"] * 3 +
            ["2023-01-03"] * 3
        ),
        "elementId": [
            "mean(air_temperature P1D)",
            "sum(precipitation_amount P1D)",
            "mean(relative_humidity P1D)",
            "mean(air_temperature P1D)",
            "sum(precipitation_amount P1D)",
            "mean(relative_humidity P1D)",
            "mean(air_temperature P1D)",
            "sum(precipitation_amount P1D)",
            "mean(relative_humidity P1D)"
        ],
        "value": [5, 2, 85, 6, 3, 80, 7, 1, 90]
    })

    model, y_test, y_pred = train_model_for_city(data, "Molde")
    assert hasattr(model, "predict")
    assert len(y_test) == len(y_pred)


def test_train_model_for_city_empty():
    """
    Negative test:
    Ensures the function raises an error when given an empty input DataFrame.
    
    Expected behavior:
    - A ValueError is raised
    """
    df = pd.DataFrame(columns=["Location", "Time", "elementId", "value"])
    try:
        train_model_for_city(df, "Molde")
        assert False, "Function should raise ValueError on empty input"
    except ValueError:
        pass