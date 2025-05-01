import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

# Farger basert på byenes farge på fotballdrakt (våre hjembyer)
city_colors = {
    "Steinkjer": "#FFD700",   # gul
    "Molde": "#0072B2",       # blå
    "Ålesund": "#FF8000"      # oransje
}


def plot_temperature_trend(df):
    plt.figure(figsize=(12, 6))

    # Går igjennom hver by i datasettet
    for city in df["Location"].unique():
        subset = df[df["Location"] == city]
        subset_filtered = subset[subset["elementId"] == "mean(air_temperature P1D)"]

        # Plotter temperaturdata dersom det finnes 
        if not subset_filtered.empty:
            print(subset_filtered)  # For feilsøking
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city, color=city_colors.get(city, None))

    # Legget til aksetitler, tittel og instillinger for graf
    plt.xlabel("Time")
    plt.ylabel("Temp")
    plt.title("Temperature at 12:00 every Monday from 01.01.2023 to 01.05.2025")
    plt.legend()
    plt.grid()
    plt.show()

        
def plot_environmental_factors(df):
    plt.figure(figsize=(12, 6))
    # Går igjennom hver by i datasettet
    for city in df["Location"].unique():
        # Filtrerer data for byen og for luftfuktighet
        subset = df[df["Location"] == city]
        subset_filtered = subset[subset["elementId"] == "mean(relative_humidity P1D)"]
        
        # Plotter data dersom det finnes
        if not subset_filtered.empty:
            print(subset_filtered)  # For feilsøking
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city, color=city_colors.get(city, None))
    
    # Legget til aksetitler, tittel og instillinger for graf
    plt.xlabel("Time")
    plt.ylabel("Relative humidity (%)")
    plt.title("Relative Humidity at 12:00 every Monday from 01.01.2023 to 01.05.2025")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
    

def plot_precipitation(df):
    plt.figure(figsize=(12, 6))
    # Går igjennom hver by i datasettet
    for city in df["Location"].unique():
        # Filtrer data for byen og for nedbør
        subset = df[df["Location"] == city]
        subset_filtered = subset[subset["elementId"] == "sum(precipitation_amount P1D)"]
        
        # Plotter data dersom det finnes
        if not subset_filtered.empty:
            print(subset_filtered)  # For feilsøking 
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city, color=city_colors.get(city, None))
    
    # Legget til aksetitler, tittel og instillinger for graf
    plt.xlabel("Time")
    plt.ylabel("Precipitation amount (mm)")
    plt.title("Precipitation at 12:00 every Monday from 01.01.2023 to 01.05.2025")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
    

def plot_wind_speed(df):
    plt.figure(figsize=(12, 6))
    # Går igjennom hver by i datasettet
    for city in df["Location"].unique():
        # Filtrerer data for byen og for vindhastighet
        subset = df[df["Location"] == city]
        subset_filtered = subset[subset["elementId"] == "mean(wind_speed P1D)"]
        
        # Plotter data dersom det finnes
        if not subset_filtered.empty:
            print(subset_filtered)  # For feilsøking
            plt.plot(subset_filtered["Time"], subset_filtered["value"], label=city, color=city_colors.get(city, None))
    
    # Legget til aksetitler, tittel og instillinger for graf
    plt.xlabel("Time")
    plt.ylabel("Wind Speed (m/s)")
    plt.title("Wind Speed at 12:00 every Monday from 01.01.2023 to 01.05.2025")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
    
# Lager et dyniamsk histogram for en valgt værvariabel basert på elementId
def plot_histogram(df, element_id, label):
    # Henter unike byer i datasettet
    locations = df["Location"].unique()
    # Går igjennom hver by og filtrer ut verdiene for ønsket værvariabel (elementID)
    filtered_df = df[df["elementId"] == element_id]

    # Hvis det ikke finnes data for  valgt elementID, gi beskjed og avslutt funksjonen
    if filtered_df.empty:
        print(f"No data available for {element_id}")
        return

    # Lager histogram for verdier i valgt værvariabel, gruppert etter by
    fig = px.histogram(
        filtered_df,
        x="value",
        color="Location",
        barmode="overlay",
        nbins=20,
        labels={"value": label},
        title=f"Interactive Distribution of {label} by Location",
        color_discrete_map={
            "Steinkjer": "#FFD700",
            "Molde": "#0072B2",
            "Ålesund": "#FF8000"
        }
        
    )
    # Tilpasser layout med hvit bakgrunn og lyse rutelinjer
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor="lightgrey"),
        yaxis=dict(showgrid=True, gridcolor="lightgrey")
    )
    
    fig.show()
    
    
# Prediktiv analyse med scatterplot 
# Viser faktisk v predikert luftfuktighet som scatterplot for valgt by
def plot_scatterplot(y_test, y_pred, city):
    plt.figure(figsize=(10, 5))
    plt.scatter(y_test, y_pred, label="Predictions", alpha=0.6)

    # Lager en stiplet linje som viser perfekt prefiksjon (y=x)
    plt.plot(
        [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())],
        [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())],
        'r--',
        label="Perfect Prediction", color=city_colors.get(city, None)
    )
    plt.xlabel("Actual Humidity (%)")
    plt.ylabel("Predicted Humidity (%)")
    plt.title(f"Actual vs. Predicted Humidity – {city}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()