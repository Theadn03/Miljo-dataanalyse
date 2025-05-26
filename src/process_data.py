import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno


def handle_missing_values(df: pd.DataFrame, visualize: bool = True) -> pd.DataFrame:
    """
    Visualizes and cleans missing values in the dataset.

    Parameters:
        df (pd.DataFrame): Raw dataset from Frost API
        visualize (bool): Whether to plot missingno matrices

    Returns:
        pd.DataFrame: Cleaned dataset with critical fields preserved
    """
    # Make a copy of the full original dataset
    cleaned_df = df.copy()

    # Check that required metadata columns exist
    required_cols = ["Time", "Location"]
    for col in required_cols:
        if col not in cleaned_df.columns:
            raise ValueError(f"Missing required column: '{col}'")

    if visualize:
        print("Visualizing missing values before cleaning:")
        msno.matrix(cleaned_df)
        plt.title("Before Cleaning")
        plt.show()

    # Drop rows with missing time or location
    cleaned_df = cleaned_df.dropna(subset=["Time", "Location"])

    # Fill missing numeric columns (e.g., 'value') with median
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