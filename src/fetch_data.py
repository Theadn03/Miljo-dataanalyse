import requests
from datetime import datetime, timedelta

def fetch_data_from_frost(client_id, stations, start_date, end_date):
    weather_data = []
    current_date = start_date

    while current_date < end_date:
        next_date = current_date + timedelta(days=365)
        if next_date > end_date:
            next_date = end_date

        for city, station_id in stations.items():
            url = "https://frost.met.no/observations/v0.jsonld"
            params = {
                "sources": station_id,
                "elements": "air_temperature,precipitation_amount,wind_speed,relative_humidity",
                "referencetime": f"{current_date.date()}/{next_date.date()}"
            }
            response = requests.get(url, params=params, auth=(client_id, ""))
            if response.status_code == 200:
                data = response.json()
                if "data" in data:
                    for obs in data["data"]:
                        obs_time = datetime.fromisoformat(obs["referenceTime"].replace("Z", "+00:00"))
                       if obs_time.weekday() == 0 and obs_time.hour == 12:
                            values = {entry["elementId"]: entry["value"] for entry in obs["observations"]}
                            weather_data.append({
                                "Lokasjon": city,
                                "Tidspunkt": obs["referenceTime"],
                                "Temperatur (°C)": values.get("air_temperature"),
                                "Nedbør (mm)": values.get("precipitation_amount"),
                                "Vindhastighet (m/s)": values.get("wind_speed"),
                                "Luftfuktighet (%)": values.get("relative_humidity")
                            })
        current_date = next_date
    return weather_data
