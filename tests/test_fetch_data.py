
# Testfil for å sjekke at hent_data_fra_frost() fungerer uten å feile

import pytest
from datetime import datetime
from src.hent_data import hent_data_fra_frost

# Bruker dummy data (kortere periode og kun én stasjon for test)
def test_hent_data_med_gyldig_input():
    client_id = "e0cdd794-6446-4380-9df0-e6828509519c"  #API-nøkkel
    stasjoner = {"Molde": "SN62295"}
    start = datetime(2023, 1, 1)
    slutt = datetime(2023, 1, 31)

    try:
        data = hent_data_fra_frost(client_id, stasjoner, start, slutt)
        assert isinstance(data, list)
    except Exception as e:
        pytest.fail(f"Funksjonen feilet med feil: {e}")

# Tester med ugyldig stasjons-ID for å sjekke robusthet
def test_hent_data_med_ugyldig_stasjon():
    client_id = "e0cdd794-6446-4380-9df0-e6828509519c" #API-nøkkel
    stasjoner = {"Ukjent": "SN00000"}  # Ikke eksisterende ID
    start = datetime(2023, 1, 1)
    slutt = datetime(2023, 1, 2)

    data = hent_data_fra_frost(client_id, stasjoner, start, slutt)
    assert isinstance(data, list)
    assert len(data) == 0  # Forventer tom liste

