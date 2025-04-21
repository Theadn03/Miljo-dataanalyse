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
    
# Lager et histogram for en valgt værvariabel basert på elementId
def plot_histogram(df, element_id, label, color_map=None):
    locations = df["Location"].unique()
    plt.figure(figsize=(12, 6))

    for loc in locations:
        subset = df[(df["Location"] == loc) & (df["elementId"] == element_id)]["value"]
        if not subset.empty:
            plt.hist(subset, bins=20, alpha=0.5, label=loc, edgecolor="black")

    plt.title(f"Distribution of {label} by Location")
    plt.xlabel(label)
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
   
# Prediktiv analyse med scatterplot 
def plot_scatterplot(y_test, y_pred, city):
    plt.figure(figsize=(10, 5))
    plt.scatter(y_test, y_pred, label="Predictions", alpha=0.6)
    plt.plot(
        [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())],
        [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())],
        'r--',
        label="Perfect Prediction"
    )
    plt.xlabel("Actual Temperature (°C)")
    plt.ylabel("Predicted Temperature (°C)")
    plt.title(f"Actual vs. Predicted Temperature – {city}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()