import pytest
from datetime import datetime
from src.fetch_data import fetch_data_from_frost

# Bruker dummy data (kortere periode og kun én stasjon for test)
def test_fetch_data_valid_input():
    client_id = "e0cdd794-6446-4380-9df0-e6828509519c"  # API-nøkkel
    stations = {"Molde": "SN62295"}
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 31)

    try:
        data = fetch_data_from_frost(client_id, stations, start, end)
        assert isinstance(data, list)
    except Exception as e:
        pytest.fail(f"Function failed with error: {e}")

# Tester med ugyldig stasjons-ID for å sjekke robusthet
def test_fetch_data_invalid_station():
    client_id = "e0cdd794-6446-4380-9df0-e6828509519c"
    stations = {"Unknown": "SN00000"}  # Ikke-eksisterende ID
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 2)

    data = fetch_data_from_frost(client_id, stations, start, end)
    assert isinstance(data, list)
    assert len(data) == 0  # Forventer tom liste
