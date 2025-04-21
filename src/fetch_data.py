from datetime import datetime, timedelta
import requests
import json

def fetch_data_from_frost(client_id, stations, start_date, end_date):
    weather_data = []
    current_date = start_date

# Loopen henter data i årlige bolker for å unngå store API-responser
    while current_date < end_date:
        next_date = current_date + timedelta(days=365)
        if next_date > end_date:
            next_date = end_date

        for city, station_id in stations.items():
            url = "https://frost.met.no/observations/v0.jsonld"
            params = {
                "sources": station_id,
                "elements": "mean(air_temperature P1D),sum(precipitation_amount P1D),mean(wind_speed P1D),mean(relative_humidity P1D)",
                "referencetime": f"{current_date.date()}/{next_date.date()}"
            }
            response = requests.get(url, params=params, auth=(client_id, ""))
            if response.status_code == 200:
                data = response.json()
                if "data" in data:
                    print(json.dumps(data["data"][0]))
                    print("----------------------------------------------------")
                    for x in data["data"]:
                        for observation in x["observations"]:
                            #weather_data.append({**observation, "Time": x["referenceTime"], "Location": x["sourceId"]})
                            weather_data.append({**observation, "Time": x["referenceTime"], "Location": city})
                        
        current_date = next_date
    return weather_data