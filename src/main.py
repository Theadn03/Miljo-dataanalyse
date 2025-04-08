from datetime import datetime
from data.hent_data import hent_data_fra_frost
from Prosessering.behandle_data import behandle_og_rens_data
from Visualisering.vis_data import vis_temperaturgraf

# Oppsett
client_id = "e0cdd794-6446-4380-9df0-e6828509519c"
stations = {
    "Molde": "SN62295",
    "Ålesund": "SN60945",
    "Steinkjer": "SN70680"
}
start_date = datetime(2020, 1, 1)
end_date = datetime.now()

# Kjøring
print("Henter data...")
weather_data = hent_data_fra_frost(client_id, stations, start_date, end_date)

print("Renser og bearbeider data...")
df = behandle_og_rens_data(weather_data)

print("Lager visualisering...")
vis_temperaturgraf(df)

df.to_csv("ukedata.csv", index=False, encoding='utf-8')
print("Ukedata lagret som 'ukedata.csv'")
