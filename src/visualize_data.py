import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

# Farger til de ulike byene
city_colors = {
    "Steinkjer": "#FFD700",   # gul
    "Molde": "#0072B2",       # blå
    "Ålesund": "#FF8000"     # oransje
}

def plot_temperature_trend(df):
    plt.figure(figsize=(12, 6))

    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        subset_filtered = subset[subset["elementId"] == "mean(air_temperature P1D)"]
    
        if not subset_filtered.empty:
            print(subset_filtered)
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city, color=city_colors.get(city, None))

    plt.xlabel("Time")
    plt.ylabel("Temp")
    plt.title("Temperature at 12:00pm every Monday from 01.01.2020 to 01.05.2025")
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
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city, color=city_colors.get(city, None))
            
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
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city, color=city_colors.get(city, None))
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
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city, color=city_colors.get(city, None))
    plt.xlabel("Time")
    plt.ylabel("Wind Speed (m/s)")
    plt.title("Wind Speed at 12:00 every Monday")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
    
# Lager et dyniamsk histogram for en valgt værvariabel basert på elementId
def plot_histogram(df, element_id, label):
    locations = df["Location"].unique()
    filtered_df = df[df["elementId"] == element_id]

    if filtered_df.empty:
        print(f"No data available for {element_id}")
        return

    fig = px.histogram(
        filtered_df,
        x="value",
        color="Location",
        barmode="overlay",
        nbins=20,
        labels={"value": label},
        title=f"Interactive Distribution of {label} by Location",
        color_discrete_map={
            "Steinkjer": "#FFD700",
            "Molde": "#0072B2",
            "Ålesund": "#FF8000"
        }
    )
    
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor="lightgrey"),
        yaxis=dict(showgrid=True, gridcolor="lightgrey")
    )
    
    fig.show()
    
    
# Prediktiv analyse med scatterplot 
def plot_scatterplot(y_test, y_pred, city):
    plt.figure(figsize=(10, 5))
    plt.scatter(y_test, y_pred, label="Predictions", alpha=0.6)
    plt.plot(
        [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())],
        [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())],
        'r--',
        label="Perfect Prediction", color=city_colors.get(city, None)
    )
    plt.xlabel("Actual Humidity (%)")
    plt.ylabel("Predicted Humidity (%)")
    plt.title(f"Actual vs. Predicted Humidity – {city}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()