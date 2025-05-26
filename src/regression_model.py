import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error


def train_model_for_city(df: pd.DataFrame, city: str):
    """
    Trains a linear regression model to predict relative humidity for a specific city,
    based on precipitation and temperature. Input features are standardized before training.

    Parameters:
        df (pd.DataFrame): Input dataset containing weather observations
        city (str): Name of the city to filter the data for

    Returns:
        model (LinearRegression): Trained regression model
        y_test (pd.Series): True humidity values for the test set
        y_pred (np.ndarray): Predicted humidity values from the model
    """
    print(f"\nTraining model for {city}...")

    # Filter relevant rows by city and variable
    city_df = df[
        (df["Location"] == city) &
        (df["elementId"].isin([
            "mean(air_temperature P1D)",
            "mean(relative_humidity P1D)",
            "sum(precipitation_amount P1D)"
        ]))
    ]

    # Pivot to wide format with variables as columns
    pivot = city_df.pivot_table(
        index="Time",
        columns="elementId",
        values="value"
    ).reset_index()

    # Rename columns for clarity
    pivot.rename(columns={
        "mean(air_temperature P1D)": "Temperature",
        "mean(relative_humidity P1D)": "Humidity",
        "sum(precipitation_amount P1D)": "Precipitation"
    }, inplace=True)

    # Drop rows with missing values
    pivot.dropna(inplace=True)

    # Define features and target
    X = pivot[["Precipitation", "Temperature"]]
    y = pivot["Humidity"]

    # Standardize input features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # Train linear regression model
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    # Evaluate model performance
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"R² score for {city}: {r2:.2f}")
    print(f"MSE for {city}: {mse:.2f}")

    return model, y_test, y_pred