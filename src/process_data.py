import pandas as pd

def process_and_clean_data(weather_data):
    df = pd.DataFrame(weather_data)
    df["time"] = pd.to_datetime(df["time"])
    df = df.infer_objects(copy=False)
    df.interpolate(method="linear", inplace=True)
    df.rename(columns={"Temperature (°C)": "Temperature_C"}, inplace=True)
    return df

