import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno


def handle_missing_values(
    df: pd.DataFrame,
    visualize: bool = True
) -> pd.DataFrame:
    """
    Clean the input DataFrame by handling missing values.

    Operations:
    - Drop rows with missing 'Time' or 'Location'
    - Interpolate 'temperature' values lineært
    - Fill 'humidity' values with forward- and backward-fill
    - Fill other numeric columns with median values
    - Optional visualization before and after cleaning

    Parameters:
        df (pd.DataFrame): Input dataset
        visualize (bool): If True, displays missing value plots

    Returns:
        pd.DataFrame: Cleaned dataset
    """
    cleaned_df = df.copy()

    required_cols = ["Time", "Location"]
    for col in required_cols:
        if col not in cleaned_df.columns:
            raise ValueError(f"Missing required column: '{col}'")

    if visualize:
        print("Visualizing missing values before cleaning:")
        msno.matrix(cleaned_df)
        plt.title("Before Cleaning")
        plt.show()

    cleaned_df = cleaned_df.dropna(subset=["Time", "Location"])

    if "temperature" in cleaned_df.columns:
        cleaned_df["temperature"] = cleaned_df["temperature"].interpolate(
            method="linear"
        )

    if "humidity" in cleaned_df.columns:
        cleaned_df["humidity"] = (
            cleaned_df["humidity"]
            .fillna(method="ffill")
            .fillna(method="bfill")
        )

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