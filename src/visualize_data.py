import matplotlib.pyplot as plt

def plot_temperature_trend(df):
    plt.figure(figsize=(12, 6))
    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        plt.plot(subset["Time"], subset["Temperature_C"], label=city)
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature at 12:00pm every Monday from 01.01.2020")
    plt.legend()
    plt.grid()
    plt.show()

