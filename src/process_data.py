import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno

def handle_missing_values(df: pd.DataFrame, visualize: bool = True) -> pd.DataFrame:
    """
    Cleans a DataFrame by handling missing values.

    Operations:
    - Drops rows with missing 'timestamp' or 'city'
    - Interpolates temperature (linear)
    - Forward- and backward-fills humidity
    - Fills remaining numeric columns with median values
    - Optionally visualizes missing data before and after cleaning

    Parameters:
        df (pd.DataFrame): Input dataset
        visualize (bool): Whether to show missing data plots (default: True)

    Returns:
        pd.DataFrame: Cleaned dataset
    """
    cleaned_df = df.copy()

    if visualize:
        print("Visualizing missing values before cleaning:")
        msno.matrix(cleaned_df)
        plt.title("Before Cleaning")
        plt.show()

    # Drop rows missing critical identifiers
    cleaned_df = cleaned_df.dropna(subset=["Time", "Location"])

    # Interpolate temperature
    if "temperature" in cleaned_df.columns:
        cleaned_df["temperature"] = cleaned_df["temperature"].interpolate(
            method="linear"
        )

    # Forward/backward fill humidity
    if "humidity" in cleaned_df.columns:
        cleaned_df["humidity"] = (
            cleaned_df["humidity"]
            .fillna(method="ffill")
            .fillna(method="bfill")
        )

    # Fill remaining numeric columns with median
    numeric_cols = cleaned_df.select_dtypes(
        include=["float64", "int64"]
    ).columns
    for col in numeric_cols:
        if cleaned_df[col].isnull().sum() > 0:
            cleaned_df[col] = cleaned_df[col].fillna(
                cleaned_df[col].median()
            )

    if visualize:
        print("Visualizing missing values after cleaning:")
        msno.matrix(cleaned_df)
        plt.title("After Cleaning")
        plt.show()

    return cleaned_df