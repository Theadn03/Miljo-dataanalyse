import pandas as pd
import matplotlib.pyplot as plt

# Funksjon for å skrive ut gjennomsnitt, median og standardavvik for alle relevante variabler
def print_basic_statistics(df):
    print("\nDescriptive statistics (temperature, precipitation, wind, humidity):")
    variables = ["Temperature_C", "Precipitation_mm", "WindSpeed_mps", "Humidity_percent"]
    
    for var in variables:
        print(f"\n{var}:")
        print(f"  Mean:      {df[var].mean():.2f}")
        print(f"  Median:    {df[var].median():.2f}")
        print(f"  Std. dev.: {df[var].std():.2f}")

# Funksjon for å vise korrelasjon mellom temperatur og de andre variablene
def print_correlation(df):
    print("\nCorrelation between temperature and other variables:")
    print("  Temp vs. Humidity:", df["Temperature_C"].corr(df["Humidity_percent"]))
    print("  Temp vs. Wind Speed:", df["Temperature_C"].corr(df["WindSpeed_mps"]))
    print("  Temp vs. Precipitation:", df["Temperature_C"].corr(df["Precipitation_mm"]))

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
    for col in ["Temperature_C", "Precipitation_mm", "WindSpeed_mps", "Humidity_percent"]:
        print(f"  {col}: {df[col].skew():.2f}")

