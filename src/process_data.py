import pandas as pd

def process_and_clean_data(weather_data):
    df = pd.DataFrame(weather_data)
    df["Tidspunkt"] = pd.to_datetime(df["Tidspunkt"])
    df = df.infer_objects(copy=False)
    df.interpolate(method="linear", inplace=True)
    df.rename(columns={"Temperatur (°C)": "Temperatur_C"}, inplace=True)
    return df

