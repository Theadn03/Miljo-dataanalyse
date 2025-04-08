import pandas as pd

# Renser og strukturerer rå værdata til en analyseklar DataFrame
def process_and_clean_data(weather_data):
    # Konverterer rådata til en Pandas DataFrame
    df = pd.DataFrame(weather_data)

    # Konverterer 'time'-kolonnen til datetime-format for enklere tidsbasert analyse
    df["time"] = pd.to_datetime(df["time"])

    # Gjetter og optimaliserer datatyper der det er mulig (f.eks. int, float, kategorisk)
    df = df.infer_objects(copy=False)

    # Fyller inn eventuelle manglende verdier med lineær interpolasjon (f.eks. manglende temperaturmålinger)
    df.interpolate(method="linear", inplace=True)

    # Endrer navn på temperaturkolonnen til en mer programmeringsvennlig variant
    df.rename(columns={"Temperature (°C)": "Temperature_C"}, inplace=True)

    # Returnerer den rensede DataFrame-en
    return df
