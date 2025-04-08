import matplotlib.pyplot as plt
import seaborn as sns

def plot_temperature_trend(df):
    plt.figure(figsize=(12, 6))
    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        plt.plot(subset["Time"], subset["Temperature_C"], label=city)
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature at 12:00pm every Monday from 01.01.2020 to date")
    plt.legend()
    plt.grid()
    plt.show()

def plot_environmental_factors(df):
    plt.figure(figsize=(12, 6))
    for location in df["Location"].unique():
        subset = df[df["Location"] == location]
        plt.plot(subset["Timestamp"], subset["Humidity_percent"], label=location)
    plt.xlabel("Time")
    plt.ylabel("Relative Humidity (%)")
    plt.title("Relative Humidity at 12:00 every Monday")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_precipitation(df):
    plt.figure(figsize=(12, 6))
    for location in df["Location"].unique():
        subset = df[df["Location"] == location]
        plt.plot(subset["Timestamp"], subset["Precipitation_mm"], label=location)
    plt.xlabel("Time")
    plt.ylabel("Precipitation (mm)")
    plt.title("Precipitation at 12:00 every Monday")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_wind_speed(df):
    plt.figure(figsize=(12, 6))
    for location in df["Location"].unique():
        subset = df[df["Location"] == location]
        plt.plot(subset["Timestamp"], subset["WindSpeed_mps"], label=location)
    plt.xlabel("Time")
    plt.ylabel("Wind Speed (m/s)")
    plt.title("Wind Speed at 12:00 every Monday")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()