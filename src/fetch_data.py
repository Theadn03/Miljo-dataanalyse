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

    The data is retrieved in chunks of up to one year to avoid overly large API responses.
    For each station, observations for air temperature, precipitation, wind speed, and 
    relative humidity are collected. Each record is enriched with the city name and timestamp.

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

    # Iterate over date ranges in 1-year intervals
    while current_date < end_date:
        next_date = current_date + timedelta(days=365)
        if next_date > end_date:
            next_date = end_date

        # Fetch data for each station (i.e., city)
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

            # Make API request with Basic Auth
            response = requests.get(url, params=params, auth=(client_id, ""))
            if response.status_code == 200:
                data = response.json()
                if "data" in data:
                    # Print one sample entry (for verification/debugging)
                    print(json.dumps(data["data"][0]))
                    print("-" * 60)

                    # Extract individual observations and enrich them
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