import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

def train_regression_model(df):
    # Filtrer ut relevante elementer
    pivot = df[df["elementId"].isin([
        "mean(air_temperature P1D)",
        "mean(relative_humidity P1D)",
        "mean(wind_speed P1D)",
        "sum(precipitation_amount P1D)"
    ])]

    # Konverter til bredt format
    pivot = pivot.pivot_table(
        index=["Time", "Location"],
        columns="elementId",
        values="value"
    ).reset_index()

    pivot.columns.name = None
    pivot.rename(columns={
        "mean(air_temperature P1D)": "Temperature",
        "mean(relative_humidity P1D)": "Humidity",
        "mean(wind_speed P1D)": "Wind Speed",
        "sum(precipitation_amount P1D)": "Precipitation"
    }, inplace=True)

    # Fjern rader med manglende verdier
    pivot.dropna(inplace=True)

    # Split variabler
    X = pivot[["Humidity", "Wind Speed", "Precipitation"]]
    y = pivot["Temperature"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Evaluer modellen
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"\nR^2 Score: {r2:.2f}")
    print(f"Mean Squared Error: {mse:.2f}")

    # Visualiser resultat
    plt.figure(figsize=(10, 5))
    plt.scatter(y_test, y_pred)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], '--', color='red')
    plt.xlabel("Actual Temperature (°C)")
    plt.ylabel("Predicted Temperature (°C)")
    plt.title("Actual vs. Predicted Temperature")
    plt.grid()
    plt.tight_layout()
    plt.show()

    return model