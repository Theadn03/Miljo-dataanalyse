import pandas as pd
import matplotlib.pyplot as plt


def print_basic_statistics(df: pd.DataFrame) -> None:
    """
    Print basic descriptive statistics (mean, median, std. dev.) for key environmental variables.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing environmental data with 'elementId' and 'value' columns.
    """
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


def print_correlation(df: pd.DataFrame) -> None:
    """
    Print correlation values between temperature and selected environmental variables.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing time-series data with 'elementId', 'Time', 'Location' and 'value'.
    """
    print("\nCorrelation between temperature and other variables:")

    # Extract temperature data
    temp = df[df["elementId"] == "mean(air_temperature P1D)"][
        ["Time", "Location", "value"]
    ].rename(columns={"value": "Temperature"})

    # Define other variables to correlate with temperature
    variables = [
        ("mean(relative_humidity P1D)", "Humidity"),
        ("mean(wind_speed P1D)", "Wind Speed"),
        ("sum(precipitation_amount P1D)", "Precipitation"),
    ]

    for element_id, label in variables:
        other = df[df["elementId"] == element_id][
            ["Time", "Location", "value"]
        ].rename(columns={"value": label})

        # Join temperature with the current variable on time and location
        merged = pd.merge(temp, other, on=["Time", "Location"])
        if not merged.empty:
            corr = merged["Temperature"].corr(merged[label])
            print(f"  Temp vs. {label}: {corr:.2f}")
        else:
            print(f"  Temp vs. {label}: No data available")


def plot_distribution(df: pd.DataFrame, element_id: str) -> None:
    """
    Generate and display a histogram of the distribution for the given elementId.

    Parameters:
        df (pd.DataFrame): DataFrame containing environmental data.
        element_id (str): The elementId of the variable to plot (e.g., "mean(air_temperature P1D)").
    """
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


def print_skewness(df: pd.DataFrame) -> None:
    """
    Print the skewness of selected environmental variables.

    Parameters:
        df (pd.DataFrame): DataFrame containing environmental data with 'elementId' and 'value' columns.
    """
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