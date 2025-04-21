import matplotlib.pyplot as plt
import seaborn as sns

def plot_temperature_trend(df):
    plt.figure(figsize=(12, 6))

    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        subset_filtered = subset[subset["elementId"] == "mean(air_temperature P1D)"]
    
        if not subset_filtered.empty:
            print(subset_filtered)
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city)

    plt.xlabel("Time")
    plt.ylabel("Temp")
    plt.title("Temperature at 12:00pm every Monday from 01.01.2020 to date")
    plt.legend()
    plt.grid()
    plt.show()
        
def plot_environmental_factors(df):
    plt.figure(figsize=(12, 6))
    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        subset_filtered = subset[subset["elementId"] == "mean(relative_humidity P1D)"]
        
        if not subset_filtered.empty:
            print(subset_filtered)
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city)
            
    plt.xlabel("Time")
    plt.ylabel("Relative humidity (%)")
    plt.title("Relative Humidity at 12:00 every Monday")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_precipitation(df):
    plt.figure(figsize=(12, 6))
    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        subset_filtered = subset[subset["elementId"] == "sum(precipitation_amount P1D)"]
        
        if not subset_filtered.empty:
            print(subset_filtered)
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city)
    plt.xlabel("Time")
    plt.ylabel("Precipitation amount (mm)")
    plt.title("Precipitation at 12:00 every Monday")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_wind_speed(df):
    plt.figure(figsize=(12, 6))
    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        subset_filtered = subset[subset["elementId"] == "mean(wind_speed P1D)"]
        
        if not subset_filtered.empty:
            print(subset_filtered)
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city)
    plt.xlabel("Time")
    plt.ylabel("Wind Speed (m/s)")
    plt.title("Wind Speed at 12:00 every Monday")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()