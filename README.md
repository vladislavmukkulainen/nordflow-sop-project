# NordFlow Oy — S&OP-prosessin rakentaminen datavetoiseksi kokonaisuudeksi

**Simuloitu, realistinen konsultointiprojekti**, joka esittelee end-to-end-lähestymistavan Sales & Operations Planning (S&OP) -prosessin kehittämiseen keskisuuressa yrityksessä: liiketoimintaongelmasta datan konsolidointiin, ennustemalliin, dashboardiin, pilviarkkitehtuuriin ja johdolle esitettävään business caseen asti.

> ⚠️ Yritys ("NordFlow Oy"), data ja luvut ovat fiktiivisiä/synteettisiä. Projekti on rakennettu portfoliotarkoitukseen osoittamaan konsultoinnin ja teknisen toteutuksen yhdistämistä.

## Miksi tämä projekti on olemassa

Tämä repo demonstroi kykyä toimia **hybridikonsulttina**, joka pystyy sekä ymmärtämään liiketoiminnan (myynti, operaatiot, talous) että toteuttamaan teknisen ratkaisun itse (data, ennustaminen, visualisointi, pilvi) — ei vain kirjoittamaan diaesitystä ratkaisusta, vaan rakentamaan sen.

## Projektin rakenne

| Kansio | Sisältö | Ydintaidot |
|---|---|---|
| [`01_business_context`](./01_business_context) | Case, ongelma, tavoitteet, sidosryhmät, KPI:t | Liiketoimintaymmärrys, S&OP |
| [`02_project_plan`](./02_project_plan) | Agile-projektisuunnitelma, sprintit, milestonet | Projektinhallinta |
| [`03_data`](./03_data) | Synteettinen ERP/CRM-data ja skeemat | Datamallinnus |
| [`04_sql`](./04_sql) | Datan haku, puhdistus, konsolidointi | SQL |
| [`05_forecasting`](./05_forecasting) | Kysyntäennustemalli + AI-anomaliatunnistus | Python, Applied AI |
| [`06_dashboard`](./06_dashboard) | KPI-dashboard (Power BI) | Power BI |
| [`07_azure`](./07_azure) | Pilviarkkitehtuuri datan skaalaamiseen | Microsoft Azure |
| [`08_business_case`](./08_business_case) | ROI-laskelma, kustannus-hyötyanalyysi | Business Case Development |
| [`09_stakeholder_comms`](./09_stakeholder_comms) | Johtoryhmäesitys ja viestintä | Stakeholder Communication |

## Projektin eteneminen

- [x] Vaihe 1: Liiketoimintakonteksti ja ongelman määrittely
- [x] Vaihe 2: Agile-projektisuunnitelma
- [ ] Vaihe 3: Synteettinen data (ERP/CRM)
- [ ] Vaihe 4: SQL — datan konsolidointi
- [ ] Vaihe 5: Python — kysyntäennuste ja anomaliatunnistus
- [ ] Vaihe 6: Power BI -dashboard
- [ ] Vaihe 7: Azure-arkkitehtuuri
- [ ] Vaihe 8: Business case (ROI)
- [ ] Vaihe 9: Stakeholder-viestintä

## Tekijä

Vladislav — liiketoiminnan ja teknologian yhdistävä konsultti (ICT-myynti, supply chain & operaatiot -tausta; SQL, Power BI, Python, AI).
