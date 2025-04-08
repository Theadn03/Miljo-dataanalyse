import pandas as pd
import matplotlib.pyplot as plt

# Funksjon for å skrive ut gjennomsnitt, median og standardavvik for alle relevante variabler
def print_basic_statistics(df):
    print("\nDescriptive statistics (temperature, precipitation, wind, humidity):")
    variables = ["Air temperature (°C)", "Precipitation amount (mm)", "Wind-speed (m/s)", "Reltive humidity (%)"]
    
    for var in variables:
        print(f"\n{var}:")
        print(f"  Mean:      {df[var].mean():.2f}")
        print(f"  Median:    {df[var].median():.2f}")
        print(f"  Std. dev.: {df[var].std():.2f}")

# Funksjon for å vise korrelasjon mellom temperatur og de andre variablene
def print_correlation(df):
    print("\nCorrelation between temperature and other variables:")
    print("  Temp vs. Humidity:", df["Air temperature (°C)"].corr(df["Reltive humidity (%)"]))
    print("  Temp vs. Wind Speed:", df["Air temperature (°C)"].corr(df["Wind-speed (m/s)"]))
    print("  Temp vs. Precipitation:", df["Air temperature (°C)"].corr(df["Precipitation amount (mm)"]))

# Funksjon for å plotte fordelingen (histogram) av en valgt variabel
def plot_distribution(df, column):
    plt.figure(figsize=(10, 5))
    df[column].hist(bins=20)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.grid()
    plt.tight_layout()
    plt.show()

# Funksjon for å skrive ut skjevhet (asymmetri) i datasettet for hver variabel
def print_skewness(df):
    print("\nSkewness in key variables:")
    for col in ["Air temperature (°C)", "Wind-speed (m/s)", "Wind-speed (m/s)", "Reltive humidity (%)"]:
        print(f"  {col}: {df[col].skew():.2f}")