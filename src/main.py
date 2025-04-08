from datetime import datetime
from fetch_data import fetch_data_from_frost
from process_data import process_and_clean_data
from visualize_data import plot_temperature_trend

# Setup
client_id = "e0cdd794-6446-4380-9df0-e6828509519c"
stations = {
    "Molde": "SN62295",
    "Ålesund": "SN60945",
    "Steinkjer": "SN70680"
}
start_date = datetime(2020, 1, 1)
end_date = datetime.now()

# Run
print("Fetching data...")
weather_data = fetch_data_from_frost(client_id, stations, start_date, end_date)

print("Processing and cleaning data...")
df = process_and_clean_data(weather_data)

print("Creating visualization...")
plot_temperature_trend(df)

df.to_csv("data/weekly_weather_data.csv", index=False, encoding='utf-8')
print("'weekly_weather_data.csv' saved.")