# Vaihe 3 — Synteettinen ERP/CRM-data

## Tausta

NordFlow'n data elää lähtötilanteessa kolmessa erillisessä lähteessä — juuri se ongelma, joka myöhemmissä vaiheissa ratkaistaan SQL:llä. Tässä vaiheessa generoidaan realistinen, mutta täysin synteettinen datasetti, joka simuloi näitä kolmea lähdettä 24 kuukauden ajalta (2024-01 – 2025-12).

Data on tuotettu skriptillä [`generate_data.py`](./generate_data.py) (Python: `pandas`, `numpy`), jotta koko datageneraation logiikka on läpinäkyvästi nähtävissä ja toistettavissa.

## Datamalli

### CRM
| Tiedosto | Kuvaus | Avainkentät |
|---|---|---|
| `customers.csv` | 60 jälleenmyyjää | `customer_id`, `region`, `segment` |
| `sales_orders.csv` | 1 705 toteutunutta myyntitilausriviä | `order_id`, `order_date`, `customer_id`, `product_id`, `quantity`, `unit_price` |

### ERP
| Tiedosto | Kuvaus | Avainkentät |
|---|---|---|
| `products.csv` | 6 tuotetta, 3 kategoriaa | `product_id`, `category`, `unit_cost` |
| `inventory_levels.csv` | Kuukausittainen varastosaldo per tuote | `month`, `product_id`, `closing_stock` |
| `purchase_orders.csv` | 208 ostotilausta toimittajilta, suunniteltu vs. toteutunut saapuminen | `po_id`, `product_id`, `order_date`, `planned_arrival`, `actual_arrival`, `quantity` |

### Talous
| Tiedosto | Kuvaus | Avainkentät |
|---|---|---|
| `budget_forecast.csv` | Talouden oma, karkea ennuste (ei huomioi kausivaihtelua tarkasti) | `month`, `product_id`, `budgeted_units`, `budgeted_revenue_eur` |

## Tietoisesti sisäänrakennetut ilmiöt

Nämä on rakennettu dataan tarkoituksella, jotta myöhemmät vaiheet (SQL-siivous, Python-ennuste, AI-anomaliatunnistus) ovat aidosti perusteltuja — ei vain kosmeettisia harjoituksia:

1. **Kausivaihtelu**
   - *Kahvinkeittimet* ja *Pienlaitteet*: selkeä joulusesonki (marras-joulukuu), tammikuu hiljaisempi
   - *Yleiskoneet*: loivempi kevätpiikki (maalis-huhtikuu)

2. **Kysyntäanomalia (kesäkuu 2025)**
   - Tuote **P004 (BrewDay Deluxe)** saa äkillisen, n. 3–3.5-kertaisen kysyntäpiikin kesäkuussa 2025 (454 kpl vs. normaali ~120–130 kpl/kk).
   - Simuloi esim. yllättävää viraaliksi noussutta some-mainintaa tai kilpailijan toimitusongelmaa.
   - Tämä on tarkoituksella "piilotettu" dataan, jotta Vaiheen 5 AI-anomaliatunnistus löytää sen aidosti, ei ennalta tiedettynä.

3. **Toimitusten myöhästymiset**
   - N. 20 % ostotilauksista saapuu 3–15 päivää myöhässä suunnitellusta (`planned_arrival` vs. `actual_arrival`) → mahdollistaa OTIF-mittarin laskennan Vaiheessa 4–6.

4. **Dataepäsiisteys** (`sales_orders.csv`)
   - 10 riviä, joilta puuttuu `customer_id`
   - 15 riviä, joilta puuttuu `unit_price`
   - 10 täysin duplikoitua riviä
   - Simuloi tyypillistä CRM/ERP-integraation laatuongelmaa, jonka SQL-vaihe (Vaihe 4) korjaa validointisäännöin.

5. **Kilpailevat ennusteet**
   - `budget_forecast.csv` sisältää talouden oman, yksinkertaistetun ennusteen (lineaarinen trendi ilman kausivaihtelua), joka poikkeaa systemaattisesti toteutuneesta myynnistä — havainnollistaa juuri Vaiheen 1 ongelman ("myynti, ostot ja talous ennustavat erikseen").

## Datan generointi uudelleen

```bash
cd 03_data
python3 generate_data.py
```

Skripti käyttää kiinteää satunnaislukusiementä (`np.random.seed(42)`), joten tulos on toistettavissa identtisenä.

---
⬅ [Vaihe 2 — Projektisuunnitelma](../02_project_plan) | [Takaisin päätasolle](../README.md) | Seuraava: [Vaihe 4 — SQL](../04_sql)
