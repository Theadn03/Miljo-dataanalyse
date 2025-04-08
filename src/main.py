from datetime import datetime
from fetch_data import fetch_data_from_frost
from process_data import process_and_clean_data
from visualize_data import plot_temperature_trend

# -----------------------
# 1. Konfigurasjon og datainnhenting
# -----------------------

# Henter værdata fra tre værstasjoner (Molde, Ålesund og Steinkjer)
# Data hentes fra MET (Meteorologisk institutt), som regnes som en svært pålitelig kilde.
# Værstasjonene er valgt fordi de ligger nært våre hjemsteder og har god tilgjengelighet.

client_id = "e0cdd794-6446-4380-9df0-e6828509519c"  # API-nøkkel for tilgang til Frost-tjenesten

stations = {
    "Molde": "SN62295",
    "Ålesund": "SN60945",
    "Steinkjer": "SN70680"
}

# Definerer tidsperioden for innhenting av data
start_date = datetime(2020, 1, 1)
end_date = datetime.now()

# Henter rå værdata for alle definerte stasjoner i valgt tidsperiode
print("Fetching data...")
weather_data = fetch_data_from_frost(client_id, stations, start_date, end_date)

# -----------------------
# 2. Databehandling og rensing
# -----------------------

# Renser og prosesserer rådata til en strukturert DataFrame
print("Processing and cleaning data...")
df = process_and_clean_data(weather_data)

# -----------------------
# 3. Visualisering
# -----------------------

# Lager en linjegraf som viser temperaturutvikling for hver by over tid
print("Creating visualization...")
plot_temperature_trend(df)

# -----------------------
# 4. Eksport av data
# -----------------------

# Lagrer den rensede og strukturerte dataen til en CSV-fil
# CSV-filer gjør det enkelt å bruke data videre i f.eks. Excel, Python, Power BI, etc.
df.to_csv("data/weekly_weather_data.csv", index=False, encoding='utf-8')
print("'weekly_weather_data.csv' saved.")


print(f"Data contains {len(df)} records.")
