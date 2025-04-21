import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

def train_regression_model(df):
    # Fjern rader med manglende verdier
    df = df.dropna()

    # Definer input-variabler (X) og målvariabel (y)
    X = df[["Humidity_percent", "WindSpeed_mps", "Precipitation_mm"]]
    y = df["Temperature_C"]

    # Split data i trenings- og testsett
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Tren modellen
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Lag prediksjoner
    y_pred = model.predict(X_test)

    # Evaluer modell
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"R^2 score: {r2:.2f}")
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
