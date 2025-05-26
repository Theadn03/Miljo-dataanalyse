import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error


def train_model_for_city(df: pd.DataFrame, city: str):
    """
    Trains a regression model to predict humidity based on temperature
    and precipitation, with standardized input features.

    Parameters:
        df (pd.DataFrame): Input dataset
        city (str): Name of the city to filter on

    Returns:
        model, y_test, y_pred: Trained model and predictions
    """
    print(f"\nTraining model for {city}...")

    city_df = df[
        (df["Location"] == city) &
        (df["elementId"].isin([
            "mean(air_temperature P1D)",
            "mean(relative_humidity P1D)",
            "sum(precipitation_amount P1D)"
        ]))
    ]

    pivot = city_df.pivot_table(
        index="Time",
        columns="elementId",
        values="value"
    ).reset_index()

    pivot.rename(columns={
        "mean(air_temperature P1D)": "Temperature",
        "mean(relative_humidity P1D)": "Humidity",
        "sum(precipitation_amount P1D)": "Precipitation"
    }, inplace=True)

    pivot.dropna(inplace=True)

    X = pivot[["Precipitation", "Temperature"]]
    y = pivot["Humidity"]

    # Standardiser input-variabler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    x_train, x_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"R² score for {city}: {r2:.2f}")
    print(f"MSE for {city}: {mse:.2f}")

    return model, y_test, y_pred