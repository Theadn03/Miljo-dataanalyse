# Denne sikrer at API-integrasjonen fungerer og at feilhåndtering er på plass
import os
import pytest
from datetime import datetime
from src.fetch_data import fetch_data_from_frost
from dotenv import load_dotenv

# Positiv test: henter data med gyldig klient-ID og stasjon
def test_fetch_data_valid_input():
    load_dotenv()
    client_id = os.getenv("API-KEY")
    stations = {"Molde": "SN62295"}
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 2)
    
    data = fetch_data_from_frost(client_id, stations, start, end)
    assert isinstance(data, list)

# Negativ test: ugyldig stasjons-ID
def test_fetch_data_invalid_station():
    load_dotenv()
    client_id = os.getenv("API-KEY")
    stations = {"Unknown": "SN00000"}  # Ikke-eksisterende ID
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 2)

    data = fetch_data_from_frost(client_id, stations, start, end)
    assert data == []  # Forventer tom liste