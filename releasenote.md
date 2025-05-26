# Release Note – Miljødataanalyseapplikasjon

*Versjon:* 1.0  
*Dato:* 2025-05-26  
*Gruppe:* Gruppe 50
*Emne:* TDT4114 – Anvendt programmering  
*Levering:* Mappeinnlevering Vår 2025

## Hva er levert

Denne versjonen inkluderer en komplett og fungerende applikasjon for innhenting, analyse og visualisering av miljødata. Prosjektet er levert som en Jupyter Notebook-applikasjon med tilhørende modulstruktur i Python.

## Hovedfunksjonalitet

- *Datainnhenting:*  
  Henter værdata via API (Frost) og lagrer dem som .csv ved hjelp av fetch_data.py.

- *Databehandling:*  
  Rensing, transformasjon og statistiske analyser implementert i process_data.py med bruk av Pandas og NumPy.

- *Visualisering:*  
  Interaktive og statiske grafer (temperatur, nedbør, vind og luftfuktighet) med Plotly og Matplotlib via visualize_data.py.

- *Prediktiv analyse:*  
  Lineær regresjon for prediksjon av temperatur, med modell evaluert per by (scikit-learn). Resultatene vises som scatterplots med predikert vs. faktisk verdi.

- *Refleksjonsnotat:*  
  Vedlagt som reflective_note.pdf, inneholder læringspunkter, vurdering av resultat, samarbeid og forslag til forbedringer.

## Teknisk struktur

  - src/: Python-moduler
  - notebooks/: Hovedapplikasjon
  - data/: Automatisk lagring av .csv
  - tests/: Enhetstester
  - .gitignore, README.md, og requirements.txt

- API-nøkkel lagres i .env og lastes inn med python-dotenv.


## Testing

- Enhetstester for sentrale funksjoner implementert med unittest.
- Negative testtilfeller inkludert.
- Testene kan kjøres via python -m unittest discover tests/.

## Krav og avhengigheter

Se requirements.txt for liste over nødvendige Python-pakker. Krever Python 3.9 eller nyere.

## Konklusjon

Prosjektet er utviklet i tråd med læringsmålene i TDT4114 og demonstrerer ferdigheter innen programmering, datavitenskap, programstruktur, testing og dokumentasjon.