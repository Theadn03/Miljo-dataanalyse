import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Farger basert på hjembyenes fotballdrakter
city_colors = {
    "Steinkjer": "#FFD700",   # gul
    "Molde": "#0072B2",       # blå
    "Ålesund": "#FF8000"      # oransje
}


def plot_temperature_trend(df: pd.DataFrame) -> None:
    """
    Plot temperature trend over tid for hver by.
    """
    plt.figure(figsize=(12, 6))

    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        filtered = subset[
            subset["elementId"] == "mean(air_temperature P1D)"
        ]
        if not filtered.empty:
            plt.plot(
                filtered["Time"],
                filtered["value"],
                label=city,
                color=city_colors.get(city, None)
            )

    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title(
        "Temperature at 12:00 every Monday from 01.01.2023 to 01.05.2025"
    )
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


def plot_environmental_factors(df: pd.DataFrame) -> None:
    """
    Plot relative humidity for hver by over tid.
    """
    plt.figure(figsize=(12, 6))

    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        filtered = subset[
            subset["elementId"] == "mean(relative_humidity P1D)"
        ]
        if not filtered.empty:
            plt.plot(
                filtered["Time"],
                filtered["value"],
                label=city,
                color=city_colors.get(city, None)
            )

    plt.xlabel("Time")
    plt.ylabel("Relative humidity (%)")
    plt.title(
        "Relative Humidity at 12:00 every Monday "
        "from 01.01.2023 to 01.05.2025"
    )
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


def plot_precipitation(df: pd.DataFrame) -> None:
    """
    Plot nedbør over tid for hver by.
    """
    plt.figure(figsize=(12, 6))

    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        filtered = subset[
            subset["elementId"] == "sum(precipitation_amount P1D)"
        ]
        if not filtered.empty:
            plt.plot(
                filtered["Time"],
                filtered["value"],
                label=city,
                color=city_colors.get(city, None)
            )

    plt.xlabel("Time")
    plt.ylabel("Precipitation amount (mm)")
    plt.title(
        "Precipitation at 12:00 every Monday "
        "from 01.01.2023 to 01.05.2025"
    )
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


def plot_wind_speed(df: pd.DataFrame) -> None:
    """
    Plot vindhastighet over tid for hver by.
    """
    plt.figure(figsize=(12, 6))

    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        filtered = subset[
            subset["elementId"] == "mean(wind_speed P1D)"
        ]
        if not filtered.empty:
            plt.plot(
                filtered["Time"],
                filtered["value"],
                label=city,
                color=city_colors.get(city, None)
            )

    plt.xlabel("Time")
    plt.ylabel("Wind Speed (m/s)")
    plt.title(
        "Wind Speed at 12:00 every Monday "
        "from 01.01.2023 to 01.05.2025"
    )
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


def plot_histogram(df: pd.DataFrame, element_id: str, label: str) -> None:
    """
    Lag et interaktivt histogram for valgt værvariabel (elementId).
    """
    filtered = df[df["elementId"] == element_id]
    if filtered.empty:
        print(f"No data available for {element_id}")
        return

    fig = px.histogram(
        filtered,
        x="value",
        color="Location",
        barmode="overlay",
        nbins=20,
        labels={"value": label},
        title=f"Interactive Distribution of {label} by Location",
        color_discrete_map=city_colors
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor="lightgrey"),
        yaxis=dict(showgrid=True, gridcolor="lightgrey")
    )

    fig.show()


def plot_scatterplot(
    y_test: pd.Series,
    y_pred: pd.Series,
    city: str
) -> None:
    """
    Scatterplot av faktisk vs. predikert luftfuktighet for én by.
    """
    plt.figure(figsize=(10, 5))
    plt.scatter(y_test, y_pred, label="Predictions", alpha=0.6)

    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())

    plt.plot(
        [min_val, max_val],
        [min_val, max_val],
        'r--',
        label="Perfect Prediction",
        color=city_colors.get(city, None)
    )

    plt.xlabel("Actual Humidity (%)")
    plt.ylabel("Predicted Humidity (%)")
    plt.title(f"Actual vs. Predicted Humidity – {city}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()