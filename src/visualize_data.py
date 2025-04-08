import matplotlib.pyplot as plt

def plot_temperature_trend(df):
    plt.figure(figsize=(12, 6))
    for city in df["Lokasjon"].unique():
        subset = df[df["Lokasjon"] == city]
        plt.plot(subset["Tidspunkt"], subset["Temperatur_C"], label=city)
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature at 12:00 every Monday from 01.01.2020")
    plt.legend()
    plt.grid()
    plt.show()

