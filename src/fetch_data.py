from datetime import datetime, timedelta
import requests
import json


def fetch_data_from_frost(
    client_id: str,
    stations: dict,
    start_date: datetime,
    end_date: datetime
) -> list:
    """
    Fetches weather data from the Frost API for a set of stations
    between a given start and end date.

    Parameters:
        client_id (str): Frost API client ID.
        stations (dict): Mapping of city names to station IDs.
        start_date (datetime): Start of the observation period.
        end_date (datetime): End of the observation period.

    Returns:
        list: List of observation dictionaries with added 'Time' and 'Location'.
    """
    weather_data = []
    current_date = start_date

    # Fetch data in 1-year intervals to avoid large API responses
    while current_date < end_date:
        next_date = current_date + timedelta(days=365)
        if next_date > end_date:
            next_date = end_date

        for city, station_id in stations.items():
            url = "https://frost.met.no/observations/v0.jsonld"
            params = {
                "sources": station_id,
                "elements": (
                    "mean(air_temperature P1D),"
                    "sum(precipitation_amount P1D),"
                    "mean(wind_speed P1D),"
                    "mean(relative_humidity P1D)"
                ),
                "referencetime": f"{current_date.date()}/{next_date.date()}"
            }

            response = requests.get(url, params=params, auth=(client_id, ""))
            if response.status_code == 200:
                data = response.json()
                if "data" in data:
                    print(json.dumps(data["data"][0]))
                    print("-" * 60)

                    for item in data["data"]:
                        for obs in item["observations"]:
                            obs_record = {
                                **obs,
                                "Time": item["referenceTime"],
                                "Location": city
                            }
                            weather_data.append(obs_record)

        current_date = next_date

    return weather_data