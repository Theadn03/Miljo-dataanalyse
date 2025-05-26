import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno


def handle_missing_values(df: pd.DataFrame, visualize: bool = True) -> pd.DataFrame:
    """
    Cleans the input DataFrame by:
    - Selecting relevant columns only
    - Dropping rows missing 'Time' or 'Location'
    - Interpolating temperature values if present
    - Forward and backward filling humidity values if present
    - Filling remaining numeric columns with their median
    - Optionally visualizing missing values before and after cleaning

    Parameters:
        df (pd.DataFrame): Raw input dataset
        visualize (bool): Whether to display missing value matrices

    Returns:
        pd.DataFrame: Cleaned dataset ready for analysis
    """
    # Keep only relevant columns for analysis
    columns_to_keep = ["elementId", "value", "Time", "Location"]
    cleaned_df = df[columns_to_keep].copy()

    # Ensure critical columns exist
    required_cols = ["Time", "Location"]
    for col in required_cols:
        if col not in cleaned_df.columns:
            raise ValueError(f"Missing required column: '{col}'")

    if visualize:
        print("Visualizing missing values before cleaning:")
        msno.matrix(cleaned_df)
        plt.title("Before Cleaning")
        plt.show()

    # Drop rows missing timestamp or location
    cleaned_df = cleaned_df.dropna(subset=["Time", "Location"])

    # Interpolate temperature if available
    if "temperature" in cleaned_df.columns:
        cleaned_df["temperature"] = cleaned_df["temperature"].interpolate(method="linear")

    # Fill missing humidity values using forward and backward fill
    if "humidity" in cleaned_df.columns:
        cleaned_df["humidity"] = (
            cleaned_df["humidity"]
            .fillna(method="ffill")
            .fillna(method="bfill")
        )

    # Fill other numeric columns with their median value
    numeric_cols = cleaned_df.select_dtypes(include=["float64", "int64"]).columns
    for col in numeric_cols:
        if cleaned_df[col].isnull().sum() > 0:
            cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].median())

    if visualize:
        print("Visualizing missing values after cleaning:")
        msno.matrix(cleaned_df)
        plt.title("After Cleaning")
        plt.show()

    return cleaned_df