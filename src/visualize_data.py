import matplotlib.pyplot as plt

def vis_temperaturgraf(df):
    plt.figure(figsize=(12, 6))
    for city in df["Lokasjon"].unique():
        subset = df[df["Lokasjon"] == city]
        plt.plot(subset["Tidspunkt"], subset["Temperatur_C"], label=city)
    plt.xlabel("Tid")
    plt.ylabel("Temperatur (°C)")
    plt.title("Temperatur kl 12:00 hver mandag fra 01.01.2020")
    plt.legend()
    plt.grid()
    plt.show()
