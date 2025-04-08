# Plotter temperaturutvikling over tid for hver by i datasettet.
# Hver by får sin egen linje i diagrammet.
def plot_temperature_trend(df):
    plt.figure(figsize=(12, 6))  # Lager en figur med størrelse 12x6 tommer

    for city in df["Location"].unique():  # Går gjennom alle unike byer i kolonnen "Location"
        subset = df[df["Location"] == city]  # Filtrerer data for én by om gangen
        plt.plot(subset["Time"], subset["Temperature_C"], label=city)  # Plotter tid mot temperatur

    plt.xlabel("Time")  # Setter etikett for x-aksen
    plt.ylabel("Temperature (°C)")  # Setter etikett for y-aksen
    plt.title("Temperature at 12:00pm every Monday from 01.01.2020 to date")  # Tittel på grafen
    plt.legend()  # Viser en forklaring/legende for hvilke linjer som hører til hvilke byer
    plt.grid()  # Viser rutenett i bakgrunnen
    plt.show()  # Viser selve grafen
