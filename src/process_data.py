import pandas as pd

# Renser og prosesserer værdata:
# - Konverterer tid til datetime-format
# - Gjetter riktige datatyper
# - Fyller inn manglende verdier (lineær interpolering)
# - Endrer kolonnenavn for temperatur 
def process_and_clean_data(weather_data):
    df = pd.DataFrame(weather_data)
    df["time"] = pd.to_datetime(df["time"])
    df = df.infer_objects(copy=False)
    df.interpolate(method="linear", inplace=True)
    df.rename(columns={"Temperature (°C)": "Temperature_C"}, inplace=True)
    return df

