import matplotlib.pyplot as plt

# Visualiserer temperaturutviklingen over tid for hver by
def plot_temperature_trend(df):
    # Oppretter en ny figur med størrelse 12 x 6 tommer
    plt.figure(figsize=(12, 6))

    # Går gjennom hver unik by/sted i "Location"-kolonnen
    for city in df["Location"].unique():
        # Filtrerer DataFrame-en for kun data fra én by
        subset = df[df["Location"] == city]
        # Plotter temperatur mot tid for den aktuelle byen
        plt.plot(subset["Time"], subset["Temperature_C"], label=city)

    # Legger til aksetitler og grafens hovedtittel
    plt.xlabel("Time")  # Tidsakse (x-aksen)
    plt.ylabel("Temperature (°C)")  # Temperatur (y-aksen)
    plt.title("Temperature at 12:00pm every Monday from 01.01.2020 to date")

    # Viser en legende som forklarer hvilken linje som tilhører hvilken by
    plt.legend()

    # Aktiverer rutenett for bedre lesbarhet
    plt.grid()

    # Viser figuren/grafen
    plt.show()
