import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


def train_model_for_city(df: pd.DataFrame, city: str):
    """
    Trains a linear regression model for a given city to predict humidity
    based on temperature and precipitation.

    Parameters:
        df (pd.DataFrame): Input dataset
        city (str): City name to filter data

    Returns:
        tuple: (trained model, y_test, y_pred)
    """
    print(f"\nTraining model for {city}...")

    # Filter data for the selected city and variables
    city_df = df[
        (df["Location"] == city)
        & (df["elementId"].isin([
            "mean(air_temperature P1D)",
            "mean(relative_humidity P1D)",
            "sum(precipitation_amount P1D)"
        ]))
    ]

    # Pivot to wide format
    pivot = city_df.pivot_table(
        index="Time",
        columns="elementId",
        values="value"
    ).reset_index()

    pivot.rename(
        columns={
            "mean(air_temperature P1D)": "Temperature",
            "mean(relative_humidity P1D)": "Humidity",
            "sum(precipitation_amount P1D)": "Precipitation"
        },
        inplace=True
    )

    pivot.dropna(inplace=True)

    # Define predictors and target
    X = pivot[["Precipitation", "Temperature"]]
    y = pivot["Humidity"]

    # Split into train and test sets
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train the model
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    # Evaluate the model
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"R² score for {city}: {r2:.2f}")
    print(f"MSE for {city}: {mse:.2f}")

    return model, y_test, y_pred