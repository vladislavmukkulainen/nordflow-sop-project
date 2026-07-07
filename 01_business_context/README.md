# Vaihe 1 — Liiketoimintakonteksti ja ongelman määrittely

## Yritys: NordFlow Oy

NordFlow Oy on keskisuuri suomalainen yritys, joka maahantuo ja jälleenmyy kodinelektroniikkaa (esim. keittiökoneet) pääasiassa B2B-kanavaan (jälleenmyyjät) sekä pienessä määrin suoraan verkkokauppaan.

- **Liikevaihto:** n. 45 M€
- **Henkilöstö:** n. 120
- **Toiminta:** Keskusvarasto Suomessa, jakelija/tytäryhtiö Ruotsissa
- **Asiakkaat:** n. 60 jälleenmyyjää Pohjoismaissa + oma verkkokauppa

## Lähtötilanne (Pain Points)

1. **Myynti** ennustaa Excelissä, pääosin edellisvuoden toteuman ja kokemusperäisen arvion pohjalta. Kampanjoita, sesonkivaihtelua tai jälleenmyyjien omia varastotasoja ei huomioida systemaattisesti.
2. **Operaatiot/hankinta** tekee ostotilaukset omalla, erillisellä logiikallaan → syntyy sekä ylivarastoa (sitoutunut pääoma, hävikkiriski) että toimitusvajeita (menetetty myynti, tyytymättömät jälleenmyyjät).
3. **Talous** rakentaa budjetin kolmannen, itsenäisen oletuksen perusteella → kvartaalitulokset poikkeavat toistuvasti budjetista.
4. Yhtiöllä **ei ole yhtenäistä kuukausittaista S&OP-prosessia**, jossa myynti, operaatiot ja talous kohtaisivat saman, yhteisen datan äärellä.
5. Data on hajallaan kolmessa paikassa: **CRM** (myynti/asiakkaat), **ERP** (varasto/tilaukset/toimitukset) ja erilliset **Excel-taulukot** (budjetit, kampanjakalenteri).

## Tavoite (Business Objective)

Rakentaa NordFlow'lle kuukausittainen **S&OP-prosessi**, jota tukee:

1. Yksi yhtenäinen, SQL:llä konsolidoitu datapohja
2. Tilastollinen ja AI-avusteinen kysyntäennuste
3. Reaaliaikainen KPI-dashboard johtoryhmän päätöksenteon tueksi
4. Selkeä, euromääräinen business case investointipäätöksen tueksi

## Sidosryhmät

| Rooli | Keskeinen intressi | Rooli S&OP-prosessissa |
|---|---|---|
| Toimitusjohtaja | Kannattavuus, pääoman tehokas käyttö | Hyväksyy lopullisen suunnitelman |
| Myyntijohtaja | Palvelutaso, ei menetettyä myyntiä | Tuo myyntinäkymän/kampanjat |
| Operaatio-/hankintajohtaja | Optimaaliset varastotasot, kustannustehokkuus | Sovittaa kapasiteetin kysyntään |
| Talousjohtaja | Ennustettavuus, budjettitarkkuus | Yhdistää suunnitelman euroihin |
| IT | Datan hallittavuus, skaalautuvuus | Mahdollistaa data-alustan (Azure) |

## Onnistumisen mittarit (KPIs)

| KPI | Määritelmä | Nykytila (oletus) | Tavoite |
|---|---|---|---|
| Ennustetarkkuus (MAPE) | Ennusteen keskimääräinen virheprosentti | ~35 % | < 20 % |
| Palvelutaso (OTIF) | Ajallaan ja täydellisenä toimitetut tilaukset | ~85 % | > 95 % |
| Varaston kiertonopeus | Myynti / keskivarasto | 4x/vuosi | 6x/vuosi |
| Budjettipoikkeama | Ennuste vs. toteuma (€) | ± 15 % | ± 5 % |

## Rajaukset (Scope)

- Projekti kattaa NordFlow'n **Suomen-toiminnot** ensimmäisessä vaiheessa (Ruotsi rajattu myöhempään laajennukseen).
- Keskitytään **kuukausitason** S&OP-sykliin (ei viikko- tai päivätason operatiiviseen ohjaukseen).
- Tuoteryhmätaso: keittiökoneiden 3 pääkategoriaa (esim. yleiskoneet, kahvinkeittimet, pienlaitteet).

---
⬅ [Takaisin päätasolle](../README.md) | Seuraava: [Vaihe 2 — Projektisuunnitelma](../02_project_plan)
