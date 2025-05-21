import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno


def handle_missing_values(df: pd.DataFrame, visualize: bool = True) -> pd.DataFrame:
    """
    Cleans the input DataFrame by:
    - Keeping only relevant columns
    - Dropping rows missing 'Time' or 'Location'
    - Interpolating 'temperature'
    - Forward/backward-filling 'humidity'
    - Filling other numeric columns with median values
    - Optionally visualizing missing values before and after

    Parameters:
        df (pd.DataFrame): Raw input dataset
        visualize (bool): Whether to show missingno matrix plots

    Returns:
        pd.DataFrame: Cleaned dataset
    """
    # Behold kun de kolonnene som er relevante for videre analyse
    columns_to_keep = ["elementId", "value", "Time", "Location"]
    cleaned_df = df[columns_to_keep].copy()

    # Valider at nødvendige kolonner finnes
    required_cols = ["Time", "Location"]
    for col in required_cols:
        if col not in cleaned_df.columns:
            raise ValueError(f"Missing required column: '{col}'")

    if visualize:
        print("Visualizing missing values before cleaning:")
        msno.matrix(cleaned_df)
        plt.title("Before Cleaning")
        plt.show()

    # Dropp rader med manglende tid/sted
    cleaned_df = cleaned_df.dropna(subset=["Time", "Location"])

    # Interpoler temperatur hvis tilstede
    if "temperature" in cleaned_df.columns:
        cleaned_df["temperature"] = cleaned_df["temperature"].interpolate(
            method="linear"
        )

    # Fyll luftfuktighet hvis tilstede
    if "humidity" in cleaned_df.columns:
        cleaned_df["humidity"] = (
            cleaned_df["humidity"]
            .fillna(method="ffill")
            .fillna(method="bfill")
        )

    # Medianfyll for andre numeriske kolonner
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