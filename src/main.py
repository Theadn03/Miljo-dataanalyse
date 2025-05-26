"""
Main script for fetching, processing, analyzing, and visualizing weather data.

This pipeline performs the following steps:
1. Loads configuration and retrieves data from the Frost API
2. Cleans and prepares the data
3. Generates visualizations for exploratory data analysis
4. Performs basic statistical and correlation analysis
5. Trains regression models per city and visualizes predictions
6. Saves the final dataset to CSV for further use
"""

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

# Step 1: Configuration and data fetching
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

# Step 2: Data cleaning and preparation
df = handle_missing_values(df_raw, visualize=True)

# Step 3: Visualization
print("Creating visualization...")

plot_temperature_trend(df)
plot_environmental_factors(df)
plot_precipitation(df)
plot_wind_speed(df)

plot_histogram(df, "mean(air_temperature P1D)", "Air Temperature (°C)")
plot_histogram(df, "mean(relative_humidity P1D)", "Relative Humidity (%)")

# Train and evaluate models per city
for city in df["Location"].unique():
    model, y_test, y_pred = train_model_for_city(df, city)
    plot_scatterplot(y_test, y_pred, city)

# Step 4: Statistical analysis
print("Running statistical analysis...")

print_basic_statistics(df)
print_correlation(df)
print_skewness(df)

# Optional: Additional distribution plot
plot_distribution(df, "Air temperature (°C)")

# Step 5: Export data to CSV
os.makedirs("../data", exist_ok=True)

df.to_csv(
    "../data/weekly_weather_data.csv",
    index=False,
    encoding="utf-8"
)

print("'weekly_weather_data.csv' saved in 'data/' folder.")
print(f"Data contains {len(df)} records.")