# Vaihe 2 — Agile-projektisuunnitelma

## Metodologia

Projekti toteutetaan kevyellä **Scrum-henkisellä** lähestymistavalla: 2 viikon sprintit, joista jokainen tuottaa konkreettisen, asiakkaalle (simuloidulle NordFlow Oy:lle) esiteltävän deliverablen.

## Sprintit

| Sprintti | Kesto | Tavoite | Deliverable | Kansio repossa |
|---|---|---|---|---|
| Sprint 0 | vk 1 | Alustus & scoping | Business context, tavoitteet, KPI:t | [`01_business_context`](../01_business_context) |
| Sprint 1 | vk 2–3 | Data-perusta | Synteettinen ERP/CRM-data, skeemat | [`03_data`](../03_data) |
| Sprint 2 | vk 3–4 | Datan konsolidointi | SQL-skriptit, puhdas datamalli | [`04_sql`](../04_sql) |
| Sprint 3 | vk 4–6 | Ennustemalli | Python-ennuste + anomaliatunnistus | [`05_forecasting`](../05_forecasting) |
| Sprint 4 | vk 6–7 | Visualisointi | Power BI -dashboard | [`06_dashboard`](../06_dashboard) |
| Sprint 5 | vk 7–8 | Skaalautuvuus | Azure-arkkitehtuurin kuvaus | [`07_azure`](../07_azure) |
| Sprint 6 | vk 8–9 | Perustelu johdolle | ROI / business case | [`08_business_case`](../08_business_case) |
| Sprint 7 | vk 9–10 | Käyttöönotto | Stakeholder-esitys, viestintä | [`09_stakeholder_comms`](../09_stakeholder_comms) |

## Roolit

- **Konsultti / Data & Analytics Lead** — kokonaisvastuu projektista; SQL-, Python-, Power BI- ja Azure-toteutus; business casen laadinta
- **Product Owner** (NordFlow'n operaatiojohtaja, simuloitu) — priorisoi backlogin, hyväksyy sprinttien deliverablet
- **Sponsor** (NordFlow'n toimitusjohtaja, simuloitu) — hyväksyy lopullisen business casen ja investointipäätöksen

## Riskit ja hallintakeinot

| Riski | Vaikutus | Hallintakeino |
|---|---|---|
| Datan laatu heikko (puuttuvat arvot, epäyhtenäiset formaatit) | Ennuste epätarkka, dashboard harhaanjohtava | SQL-vaiheessa validointi- ja siivoussäännöt |
| Sidosryhmät eivät sitoudu uuteen prosessiin | Käyttöönotto epäonnistuu | Varhainen osallistaminen (Sprint 0), selkeä ROI (Sprint 6) |
| Ennustemalli liian monimutkainen liiketoiminnalle | Mallia ei luoteta, sitä ei käytetä | Yksinkertainen, selitettävä baseline-malli |
| Projektin laajuus kasvaa hallitsemattomasti (scope creep) | Aikataulu venyy, fokus hämärtyy | Tiukka rajaus jo Vaiheessa 1 |

## Definition of Done (per sprintti)

1. Koodi/tiedostot ovat oikeassa kansiossa repossa
2. Kansiolla on oma `README.md`, joka selittää mitä tehtiin ja miksi
3. README linkittää edelliseen ja seuraavaan vaiheeseen
4. Muutokset on committoitu ja pushattu GitHubiin selkeällä commit-viestillä

## Backlog-periaate

Backlog pidetään tässä tiedostossa sprinttitaulukkona. Laajemmassa tiimityössä tarkempi backlog siirrettäisiin GitHub Projects / Issues -työkaluun — mainitaan myös lopullisessa stakeholder-esityksessä osana skaalautuvuussuositusta.

---
⬅ [Vaihe 1 — Liiketoimintakonteksti](../01_business_context) | [Takaisin päätasolle](../README.md) | Seuraava: [Vaihe 3 — Data](../03_data)