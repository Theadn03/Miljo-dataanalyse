import os
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv

from fetch_data import fetch_data_from_frost
from process_data import handle_missing_values
from regression_model import train_model_for_city
from visualize_data import (
    plot_temperature_trend,
    plot_environmental_factors,
    plot_precipitation,
    plot_wind_speed,
    plot_histogram,
    plot_scatterplot
)
from analyze_data import (
    print_basic_statistics,
    print_correlation,
    plot_distribution,
    print_skewness
)

# 1. Konfigurasjon og datainnhenting
load_dotenv()
client_id = os.getenv("API-KEY")

stations = {
    "Steinkjer": "SN70680",
    "Molde": "SN62295",
    "Ålesund": "SN60945"
}

start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 5, 1)

print("Fetching data...")
weather_data = fetch_data_from_frost(
    client_id, stations, start_date, end_date
)

df_raw = pd.DataFrame(weather_data)

# 2. Databehandling og rensing
df = handle_missing_values(df_raw, visualize=True)

# 3. Visualisering
print("Creating visualization...")

plot_temperature_trend(df)
plot_environmental_factors(df)
plot_precipitation(df)
plot_wind_speed(df)

plot_histogram(df, "mean(air_temperature P1D)", "Air Temperature (°C)")
plot_histogram(df, "mean(relative_humidity P1D)", "Relative Humidity (%)")

for city in df["Location"].unique():
    model, y_test, y_pred = train_model_for_city(df, city)
    plot_scatterplot(y_test, y_pred, city)

# 4. Statistisk analyse
print("Running statistical analysis...")

print_basic_statistics(df)
print_correlation(df)
print_skewness(df)

# Optional: Show distribution of air temperature
plot_distribution(df, "Air temperature (°C)")

# 5. Eksport av data
os.makedirs("../data", exist_ok=True)

df.to_csv(
    "../data/weekly_weather_data.csv",
    index=False,
    encoding="utf-8"
)

print("'weekly_weather_data.csv' saved in 'data/' folder.")
print(f"Data contains {len(df)} records.")