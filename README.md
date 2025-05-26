# Miljødataanalyse – Gruppe 50  
## Prosjektoppgave i Anvendt programmering

Dette prosjektet analyserer og visualiserer historiske værdata hentet fra Meteorologisk institutts **Frost API** for tre norske byer: **Molde, Ålesund og Steinkjer**.

Vi fokuserer på observasjoner gjort **hver mandag kl. 12:00**, i perioden fra **01.01.2023 til 01.05.2025**. Målet er å undersøke og sammenligne klima- og værtrender mellom byene basert på faktorer som temperatur, nedbør, luftfuktighet og vind.


## Bakgrunn og formål
Vi har valgt tre geografisk ulike byer i Norge:

- **Molde** – ligger på vestkysten med relativt mildt kystklima  
- **Ålesund** – en kystby lenger sørvest med høy eksponering for nedbør og vind  
- **Steinkjer** – en innlandsby i Trøndelag med større temperatursvingninger  

Geografisk plassering har stor betydning for lokale værforhold. Kystnære byer som Ålesund og Molde påvirkes av havklima, noe som gir høyere luftfuktighet, jevnere temperatur og mer nedbør. Steinkjer, som ligger lenger inn i landet, opplever typisk kaldere vintre og mer markerte sesongvariasjoner.

**Fargekoder for byer**
I våre visualiseringer har vi brukt fargene blå, oransje og gul. Vi har tatt insiprasjon fra byene sine fotballag slik at hver farge representerer hver sin by. På den måten er det enklere å se hva som illustrer hvilken by.

**<span style="color:#FFD700">Steinkjer er gul</span>**    
**<span style="color:#0072B2">Molde er blå</span>**
**<span style="color:#FF8000">Ålesund er oransje</span>**

<img src="resources/images/steinkjer_logo.png" alt="Steinkjer FK logo" width="150"/>

<img src="resources/images/molde_logo.png" alt="Molde FK logo" width="150"/>

<img src="resources/images/aalesund_logo.png" alt="Aalesund FK logo" width="80"/>


Her kan man se de ulike fotballagene vi har hentet farge inspirasjon fra.

## Datagrunnlag
Dataene er hentet fra [Meteorologisk institutt sitt Frost API](https://frost.met.no/). 
Følgende parametere er samlet inn:

- **Lufttemperatur (°C)**  
- **Luftfuktighet (%)**  
- **Vindhastighet (m/s)** *(merk: enkelte verdier mangler)*  
- **Nedbør (mm)**  

Dataene er begrenset til **mandager kl. 12:00**, fra **1. januar 2023 til 1. mai 2025**, for å sikre jevne og sammenlignbare målepunkter over tid.


## Resultater og visualisering
Vi har laget flere typer visualiseringer basert på de innsamlede dataene:

- **Linjediagram** – Temperatur- og fuktighetstrender over tid  
- **Histogram** – Fordeling av værparametere  
- **Scatterplot med lineær regresjon** – Sammenheng mellom f.eks. temperatur og nedbør  

Visualiseringene gir innsikt i hvordan klimaet varierer mellom byene og over tid.


## Prosjektstruktur
├── data/           # Inneholder rå og behandlet data
├── docs/           # Dokumentasjon 
├── images/         # Bilder
├── notebooks/      # Jupyter Notebooks for analyse og visualisering
├── src/            # Python-moduler for datahenting og -behandling
├── tests/          # Enhetstester
├── .gitignore     
├── [README.md](README.md)       # Hoveddokumentasjon
├── [releasenote.md](releasenote.md)  # Endringslogg
└── requirements.txt

## Undermapper
- [src/README.md](src/README.md) – Dokumentasjon for Python-modulene
- [data/README.md](data/README.md) – Beskrivelse av datastrukturen
- [notebooks/README.md](notebooks/README.md) – Notebook og bruksinstruksjoner
- [tests/README.md](tests/README.md) – Oversikt over enhetstester