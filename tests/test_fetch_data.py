import pytest
from datetime import datetime
from src.fetch_data import fetch_data_from_frost

# -------------------------
# Test: gyldig input-data
# -------------------------

# Tester at funksjonen returnerer en liste når den får gyldig input
# Bruker en kort periode og én stasjon for å gjøre testen rask og forutsigbar
def test_fetch_data_valid_input():
    client_id = "e0cdd794-6446-4380-9df0-e6828509519c"  # API-nøkkel
    stations = {"Molde": "SN62295"}  # Kun én værstasjon
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 31)

    try:
        data = fetch_data_from_frost(client_id, stations, start, end)
        assert isinstance(data, list)  # Forventer at returverdien er en liste
    except Exception as e:
        # Testen feiler eksplisitt hvis funksjonen kaster en uventet feil
        pytest.fail(f"Function failed with error: {e}")

# -------------------------
# Test: ugyldig stasjon-ID
# -------------------------

# Tester hvordan funksjonen håndterer en ugyldig stasjonskode
# Forventer at den ikke feiler, men returnerer en tom liste
def test_fetch_data_invalid_station():
    client_id = "e0cdd794-6446-4380-9df0-e6828509519c"
    stations = {"Unknown": "SN00000"}  # Fiktiv/ugyldig værstasjon
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 2)

    data = fetch_data_from_frost(client_id, stations, start, end)
    
    assert isinstance(data, list)     # Funksjonen skal fortsatt returnere en liste
    assert len(data) == 0             # Forventer at listen er tom (ingen data for ugyldig stasjon)
