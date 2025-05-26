import pandas as pd
import matplotlib.pyplot as plt


def print_basic_statistics(df: pd.DataFrame) -> None:
    """
    Print descriptive statistics (mean, median, standard deviation) for selected
    environmental variables.
    
    Parameters:
        df (pd.DataFrame): Input dataset containing 'elementId' and 'value' columns.
    """
    print("\nDescriptive statistics (temperature, precipitation, wind, humidity):")

    # Map each elementId to a readable label for output
    variables = {
        "mean(air_temperature P1D)": "Air Temperature (°C)",
        "sum(precipitation_amount P1D)": "Precipitation (mm)",
        "mean(wind_speed P1D)": "Wind Speed (m/s)",
        "mean(relative_humidity P1D)": "Relative Humidity (%)"
    }

    # Print mean, median, and std for each variable if data is available
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
    Print Pearson correlation coefficient between temperature and other selected
    environmental variables.

    Parameters:
        df (pd.DataFrame): Input dataset with 'elementId', 'Location', 'Time', 'value'.
    """
    print("\nCorrelation between temperature and other variables:")

    # Filter temperature data and rename column for clarity
    temp = df[df["elementId"] == "mean(air_temperature P1D)"][
        ["Time", "Location", "value"]
    ].rename(columns={"value": "Temperature"})

    # List of variables to compare against temperature
    variables = [
        ("mean(relative_humidity P1D)", "Humidity"),
        ("mean(wind_speed P1D)", "Wind Speed"),
        ("sum(precipitation_amount P1D)", "Precipitation"),
    ]

    # Merge temperature data with each variable and calculate correlation
    for element_id, label in variables:
        other = df[df["elementId"] == element_id][
            ["Time", "Location", "value"]
        ].rename(columns={"value": label})

        merged = pd.merge(temp, other, on=["Time", "Location"])
        if not merged.empty:
            corr = merged["Temperature"].corr(merged[label])
            print(f"  Temp vs. {label}: {corr:.2f}")
        else:
            print(f"  Temp vs. {label}: No data available")


def plot_distribution(df: pd.DataFrame, element_id: str) -> None:
    """
    Plot histogram of the distribution for a selected variable (elementId).

    Parameters:
        df (pd.DataFrame): Input dataset.
        element_id (str): The variable to visualize (e.g., 'mean(air_temperature P1D)').
    """
    subset = df[df["elementId"] == element_id]["value"]
    if subset.empty:
        print(f"No data found for: {element_id}")
        return

    # Plot the histogram for the selected variable
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
    Print skewness values for selected environmental variables.

    Parameters:
        df (pd.DataFrame): Input dataset containing 'elementId' and 'value'.
    """
    print("\nSkewness in key variables:")

    # Define the variables and their output labels
    variables = {
        "mean(air_temperature P1D)": "Temperature",
        "mean(wind_speed P1D)": "Wind Speed",
        "sum(precipitation_amount P1D)": "Precipitation",
        "mean(relative_humidity P1D)": "Humidity"
    }

    # Calculate and print skewness for each variable
    for element_id, label in variables.items():
        subset = df[df["elementId"] == element_id]["value"]
        if not subset.empty:
            print(f"  {label}: {subset.skew():.2f}")
        else:
            print(f"  {label}: No data")