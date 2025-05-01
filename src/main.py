import os
from datetime import datetime
from fetch_data import fetch_data_from_frost
from process_data import process_and_clean_data
from visualize_data import plot_histogram
from visualize_data import plot_scatterplot
from regression_model import train_model_for_city
from visualize_data import (
    plot_temperature_trend,
    plot_environmental_factors,
    plot_precipitation,
    plot_wind_speed
)
from analyze_data import (
    print_basic_statistics,
    print_correlation,
    plot_distribution,
    print_skewness
)

# 1. Konfigurasjon og datainnhenting
client_id = "e0cdd794-6446-4380-9df0-e6828509519c"  # API-nøkkel for tilgang til Frost-tjenesten

stations = {
    "Steinkjer": "SN70680",
    "Molde": "SN62295",
    "Ålesund": "SN60945"
}

# Satt startdato 1. jan 2023 og sluttdato 1. mai 2025 for datainnhentingen
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 5, 1)

print("Fetching data...")
weather_data = fetch_data_from_frost(client_id, stations, start_date, end_date)

# 2. Databehandling og rensing
print("Processing and cleaning data...")
df = process_and_clean_data(weather_data)
df = df.infer_objects(copy=False)  # Legg til denne linjen
df.interpolate(method="linear", inplace=True)

# 3. Visualisering
print("Creating visualization...")
plot_temperature_trend(df)
plot_environmental_factors(df)
plot_precipitation(df)
plot_wind_speed(df)

plot_histogram(df, "mean(air_temperature P1D)", "Air Temperature (°C)")
plot_histogram(df, "mean(relative_humidity P1D)", "Relative Humiditiy (%)")

for city in df["Location"].unique():
    model, y_test, y_pred = train_model_for_city(df, city)
    plot_scatterplot(y_test, y_pred, city)

# 4. Statistisk analyse
print("Running statistical analysis...")
print_basic_statistics(df)
print_correlation(df)
print_skewness(df)
plot_distribution(df, "Air temperature (°C)")  # Valgfritt: vis fordeling av temperatur

# 5. Eksport av data
os.makedirs("../data", exist_ok=True)  # Sørg for at den lagrer seg i "data" mappen og at den eksisterer

df.to_csv("data/weekly_weather_data.csv", index=False, encoding='utf-8')
print("'weekly_weather_data.csv' saved in 'data/' folder.")
print(f"Data contains {len(df)} records.")