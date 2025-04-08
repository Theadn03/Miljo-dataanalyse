import pandas as pd

def behandle_og_rens_data(weather_data):
    df = pd.DataFrame(weather_data)
    df["Tidspunkt"] = pd.to_datetime(df["Tidspunkt"])
    df = df.infer_objects(copy=False)
    df.interpolate(method="linear", inplace=True)
    df.rename(columns={"Temperatur (°C)": "Temperatur_C"}, inplace=True)
    return df
