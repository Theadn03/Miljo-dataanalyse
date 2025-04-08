# Tester for behandle_data.py og vis_data.py

import pandas as pd
from src.behandle_data import behandle_og_rens_data

# Dummy værdata (to rader, med én manglende verdi)
testdata = [
    {
        "Lokasjon": "Molde",
        "Tidspunkt": "2023-01-02T12:00:00+00:00",
        "Temperatur (°C)": 2.0,
        "Nedbør (mm)": 0.5,
        "Vindhastighet (m/s)": 3.2,
        "Luftfuktighet (%)": 85
    },
    {
        "Lokasjon": "Molde",
        "Tidspunkt": "2023-01-09T12:00:00+00:00",
        "Temperatur (°C)": None,
        "Nedbør (mm)": 0.0,
        "Vindhastighet (m/s)": 2.9,
        "Luftfuktighet (%)": 80
    }
]

def test_behandle_og_rens_data_interpolerer():
    df = behandle_og_rens_data(testdata)
    assert not df.isnull().any().any(), "Det finnes fortsatt NaN-verdier etter interpolasjon"
    assert "Temperatur_C" in df.columns, "Kolonnen 'Temperatur_C' ble ikke opprettet"
    assert isinstance(df, pd.DataFrame), "Returnert verdi er ikke en DataFrame"

# Eksempel på visuell test (kjøres ikke automatisk, men kan brukes manuelt)
# Bruk 'pytest -s' for å vise plott
from src.vis_data import vis_temperaturgraf

def test_vis_temperaturgraf_viser_plot():
    df = behandle_og_rens_data(testdata)
    try:
        vis_temperaturgraf(df)
    except Exception as e:
        assert False, f"Feil under plotting: {e}"
