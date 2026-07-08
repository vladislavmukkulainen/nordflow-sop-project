"""
generate_data.py

Generoi NordFlow Oy:n simuloidun mutta realistisen datasetin:
- CRM: sales_orders.csv, customers.csv
- ERP: inventory_levels.csv, purchase_orders.csv, products.csv
- Talous: budget_forecast.csv

Data on täysin synteettistä (fiktiivinen yritys), mutta sisältää tarkoituksella:
- kausivaihtelua (joulusesonki kahvinkeittimissä/pienlaitteissa)
- yhden selkeän kysyntäanomalian (löydetään myöhemmin Python-vaiheessa AI:lla)
- tavallista dataepäsiisteyttä (puuttuvia arvoja, duplikaatteja) -> SQL-siivous on aidosti tarpeen

Aja: python3 generate_data.py
Tuottaa CSV-tiedostot samaan kansioon.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

# ---------------------------------------------------------
# 1. Perusdimensiot: tuotteet, asiakkaat, aikaväli
# ---------------------------------------------------------

products = pd.DataFrame([
    {"product_id": "P001", "product_name": "ChefMix 3000 -yleiskone", "category": "Yleiskoneet", "unit_cost": 65.0},
    {"product_id": "P002", "product_name": "ChefMix Pro -yleiskone", "category": "Yleiskoneet", "unit_cost": 95.0},
    {"product_id": "P003", "product_name": "BrewDay -kahvinkeitin", "category": "Kahvinkeittimet", "unit_cost": 28.0},
    {"product_id": "P004", "product_name": "BrewDay Deluxe -kahvinkeitin", "category": "Kahvinkeittimet", "unit_cost": 42.0},
    {"product_id": "P005", "product_name": "QuickBlend -tehosekoitin", "category": "Pienlaitteet", "unit_cost": 22.0},
    {"product_id": "P006", "product_name": "ToastPro -leivänpaahdin", "category": "Pienlaitteet", "unit_cost": 18.0},
])

regions = ["Uusimaa", "Pirkanmaa", "Varsinais-Suomi", "Pohjois-Pohjanmaa", "Keski-Suomi"]
segments = ["Suuri jälleenmyyjä", "Keskisuuri jälleenmyyjä", "Pieni jälleenmyyjä", "Verkkokauppa"]

customers = pd.DataFrame([
    {
        "customer_id": f"C{i:03d}",
        "customer_name": f"Jälleenmyyjä {i}",
        "region": np.random.choice(regions),
        "segment": np.random.choice(segments, p=[0.15, 0.35, 0.35, 0.15]),
    }
    for i in range(1, 61)
])

# 24 kuukauden aikaväli
start_date = datetime(2024, 1, 1)
months = pd.date_range(start_date, periods=24, freq="MS")

# ---------------------------------------------------------
# 2. Kysyntäprofiili per tuotekategoria (trendi + kausivaihtelu)
# ---------------------------------------------------------

def seasonal_factor(month_index, category):
    month_num = (month_index % 12) + 1
    if category == "Kahvinkeittimet":
        # Joulusesonki: marras-joulukuu (11,12) selvästi korkeampi
        seasonal = {11: 1.8, 12: 2.2, 1: 0.7}.get(month_num, 1.0)
    elif category == "Pienlaitteet":
        seasonal = {11: 1.4, 12: 1.6, 1: 0.8}.get(month_num, 1.0)
    else:  # Yleiskoneet - loivempi kausivaihtelu, kevään siivous/remonttikausi
        seasonal = {3: 1.2, 4: 1.3, 11: 1.2, 12: 1.3}.get(month_num, 1.0)
    trend = 1 + 0.01 * month_index  # lievä kasvutrendi ajan myötä
    return seasonal * trend

base_demand = {
    "P001": 180, "P002": 90,
    "P003": 220, "P004": 110,
    "P005": 260, "P006": 200,
}

# ---------------------------------------------------------
# 3. Myyntitilaukset (CRM) - rivitasolla per asiakas/kuukausi/tuote
# ---------------------------------------------------------

sales_rows = []
order_counter = 1

for month_idx, month in enumerate(months):
    for _, prod in products.iterrows():
        monthly_total = base_demand[prod["product_id"]] * seasonal_factor(month_idx, prod["category"])
        # SISÄÄNRAKENNETTU ANOMALIA: äkillinen kysyntäpiikki BrewDay Deluxelle 2025-06
        if prod["product_id"] == "P004" and month == pd.Timestamp("2025-06-01"):
            monthly_total *= 3.2  # esim. some-ilmiö / yllättävä kampanja kilpailijalta pois
        monthly_total = max(0, np.random.normal(monthly_total, monthly_total * 0.08))

        # Jaetaan kuukauden kokonaismyynti satunnaisesti eri asiakkaille (n. 8-15 tilausriviä/kk/tuote)
        n_orders = np.random.randint(8, 16)
        weights = np.random.dirichlet(np.ones(n_orders))
        chosen_customers = np.random.choice(customers["customer_id"], size=n_orders, replace=True)

        for cust_id, w in zip(chosen_customers, weights):
            qty = max(1, round(monthly_total * w))
            order_date = month + timedelta(days=int(np.random.randint(0, 27)))
            unit_price = round(prod["unit_cost"] * np.random.uniform(1.6, 2.0), 2)
            sales_rows.append({
                "order_id": f"SO{order_counter:05d}",
                "order_date": order_date.strftime("%Y-%m-%d"),
                "customer_id": cust_id,
                "product_id": prod["product_id"],
                "quantity": int(qty),
                "unit_price": unit_price,
            })
            order_counter += 1

sales_orders = pd.DataFrame(sales_rows)

# --- Tietoinen dataepäsiisteys: muutama puuttuva arvo ja duplikaatti ---
missing_idx = np.random.choice(sales_orders.index, size=25, replace=False)
sales_orders.loc[missing_idx[:15], "unit_price"] = np.nan
sales_orders.loc[missing_idx[15:], "customer_id"] = None
# Muutama täysin duplikoitu rivi (yleinen ERP/CRM-integraatio-ongelma)
duplicate_rows = sales_orders.sample(10, random_state=1)
sales_orders = pd.concat([sales_orders, duplicate_rows], ignore_index=True)

# ---------------------------------------------------------
# 4. Varastotasot (ERP) - kuukausittain per tuote
# ---------------------------------------------------------

inventory_rows = []
for _, prod in products.iterrows():
    stock = np.random.randint(300, 600)
    for month_idx, month in enumerate(months):
        monthly_demand = base_demand[prod["product_id"]] * seasonal_factor(month_idx, prod["category"])
        incoming = monthly_demand * np.random.uniform(0.85, 1.15)  # ostot eivät täysin osu kysyntään -> pointti tälle projektille
        stock = max(0, stock + incoming - monthly_demand)
        inventory_rows.append({
            "month": month.strftime("%Y-%m-%d"),
            "product_id": prod["product_id"],
            "closing_stock": round(stock),
        })

inventory_levels = pd.DataFrame(inventory_rows)

# ---------------------------------------------------------
# 5. Ostotilaukset (ERP) - toimittajilta, suunniteltu vs. toteutunut saapuminen
# ---------------------------------------------------------

po_rows = []
po_counter = 1
for month_idx, month in enumerate(months):
    for _, prod in products.iterrows():
        n_po = np.random.randint(1, 3)
        for _ in range(n_po):
            order_date = month + timedelta(days=int(np.random.randint(0, 20)))
            planned_lead_time = np.random.randint(14, 30)
            planned_arrival = order_date + timedelta(days=planned_lead_time)
            # Toteutunut saapuminen: n. 20% tilauksista myöhässä -> OTIF-mittarin pohja
            delay = np.random.randint(3, 15) if np.random.rand() < 0.2 else 0
            actual_arrival = planned_arrival + timedelta(days=int(delay))
            qty = np.random.randint(150, 400)
            po_rows.append({
                "po_id": f"PO{po_counter:05d}",
                "product_id": prod["product_id"],
                "order_date": order_date.strftime("%Y-%m-%d"),
                "planned_arrival": planned_arrival.strftime("%Y-%m-%d"),
                "actual_arrival": actual_arrival.strftime("%Y-%m-%d"),
                "quantity": qty,
            })
            po_counter += 1

purchase_orders = pd.DataFrame(po_rows)

# ---------------------------------------------------------
# 6. Talouden oma budjettiennuste (Excel/erillinen prosessi)
# ---------------------------------------------------------

budget_rows = []
for month_idx, month in enumerate(months):
    for _, prod in products.iterrows():
        # Talous ennustaa karkeasti edellisvuoden pohjalta ilman kausivaihtelun tarkkaa huomiointia
        naive_forecast = base_demand[prod["product_id"]] * (1 + 0.02 * month_idx)
        budget_rows.append({
            "month": month.strftime("%Y-%m-%d"),
            "product_id": prod["product_id"],
            "budgeted_units": round(naive_forecast),
            "budgeted_revenue_eur": round(naive_forecast * prod["unit_cost"] * 1.8),
        })

budget_forecast = pd.DataFrame(budget_rows)

# ---------------------------------------------------------
# Tallennus
# ---------------------------------------------------------

products.to_csv("products.csv", index=False)
customers.to_csv("customers.csv", index=False)
sales_orders.to_csv("sales_orders.csv", index=False)
inventory_levels.to_csv("inventory_levels.csv", index=False)
purchase_orders.to_csv("purchase_orders.csv", index=False)
budget_forecast.to_csv("budget_forecast.csv", index=False)

print("Data generoitu onnistuneesti:")
for f in ["products.csv", "customers.csv", "sales_orders.csv",
          "inventory_levels.csv", "purchase_orders.csv", "budget_forecast.csv"]:
    df = pd.read_csv(f)
    print(f"  {f}: {len(df)} riviä")
