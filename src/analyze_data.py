import pandas as pd
import matplotlib.pyplot as plt

# Funksjon for å skrive ut gjennomsnitt, median og standardavvik for alle relevante variabler
def print_basic_statistics(df):
    print("\nDescriptive statistics (temperature, precipitation, wind, humidity):")
    
    variables = {
        "mean(air_temperature P1D)": "Air Temperature (°C)",
        "sum(precipitation_amount P1D)": "Precipitation (mm)",
        "mean(wind_speed P1D)": "Wind Speed (m/s)",
        "mean(relative_humidity P1D)": "Relative Humidity (%)"
    }

    for element_id, label in variables.items():
        subset = df[df["elementId"] == element_id]["value"]
        if not subset.empty:
            print(f"\n{label}:")
            print(f"  Mean:      {subset.mean():.2f}")
            print(f"  Median:    {subset.median():.2f}")
            print(f"  Std. dev.: {subset.std():.2f}")
        else:
            print(f"\n{label}: No data available")

# Funksjon for å vise korrelasjon mellom temperatur og de andre variablene
def print_correlation(df):
    print("\nCorrelation between temperature and other variables:")

    temp = df[df["elementId"] == "mean(air_temperature P1D)"][["Time", "Location", "value"]].rename(columns={"value": "Temperature"})
    
    for element_id, label in [
        ("mean(relative_humidity P1D)", "Humidity"),
        ("mean(wind_speed P1D)", "Wind Speed"),
        ("sum(precipitation_amount P1D)", "Precipitation"),
    ]:
        other = df[df["elementId"] == element_id][["Time", "Location", "value"]].rename(columns={"value": label})
        merged = pd.merge(temp, other, on=["Time", "Location"])
        if not merged.empty:
            print(f"  Temp vs. {label}: {merged['Temperature'].corr(merged[label]):.2f}")
        else:
            print(f"  Temp vs. {label}: No data available")

# Funksjon for å plotte fordelingen (histogram) av en valgt variabel
def plot_distribution(df, element_id):
    subset = df[df["elementId"] == element_id]["value"]
    if subset.empty:
        print(f"No data found for: {element_id}")
        return
    
    plt.figure(figsize=(10, 5))
    subset.hist(bins=20)
    plt.title(f"Distribution of {element_id}")
    plt.xlabel(element_id)
    plt.ylabel("Count")
    plt.grid()
    plt.tight_layout()
    plt.show()

# Funksjon for å skrive ut skjevhet (asymmetri) i datasettet for hver variabel
def print_skewness(df):
    print("\nSkewness in key variables:")
    
    variables = {
        "mean(air_temperature P1D)": "Temperature",
        "mean(wind_speed P1D)": "Wind Speed",
        "sum(precipitation_amount P1D)": "Precipitation",
        "mean(relative_humidity P1D)": "Humidity"
    }

    for element_id, label in variables.items():
        subset = df[df["elementId"] == element_id]["value"]
        if not subset.empty:
            print(f"  {label}: {subset.skew():.2f}")
        else:
            print(f"  {label}: No data")