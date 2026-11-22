# Bakery data fact sheet

The [data profile notebook](../1_DatasetCharacteristics/data_profile.ipynb) and the [exploration notebook](../1_DatasetCharacteristics/explore_data.ipynb) use the three official course CSVs. The profile covers sales gaps and season boundaries. The exploration covers column ranges, join coverage, and training-period patterns. The team’s choices are recorded in the [decision log](../DECISIONS.md).

The course dataset covers one bakery branch in Kiel and is attributed to meteolytix GmbH. The course documentation gives no explicit dataset license. [Course dataset documentation](https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/README.md)

---

## 1. Sales – `umsatzdaten_gekuerzt.csv`

| Item | Value |
|---|---|
| Shape | 9,334 rows × 4 columns (`id`, `Datum`, `Warengruppe`, `Umsatz`) |
| Grain | one row = one product group on one day with sales |
| Key | `id` unique; (`Datum`, `Warengruppe`) unique (0 duplicates); `id` = `YYMMDD` + group for every row |
| Period | 2013-07-01 – 2018-07-31 = 1,857 calendar days; first and last months are complete (148 and 155 rows) |
| Opening days | 1,819 days with at least one row; 38 days without any row |
| Turnover and missing values | Every column is complete. `Umsatz` ranges from 7.0512 to 1,879.4618. The source gives no currency unit. |
| Product groups per opening day | 6 groups: 276 days · 5 groups: 1,506 days · 4 groups: 37 days |

### Turnover per product group

| Group | Rows | Mean | Median | Min | Max | Outliers > 3 IQR |
|---|---|---|---|---|---|---|
| 1 Bread | 1,819 | 122 | 120 | 23 | 417 | 8 |
| 2 Rolls | 1,819 | 402 | 371 | 175 | 1,203 | 1 |
| 3 Croissants | 1,819 | 163 | 143 | 38 | 566 | 1 |
| 4 Confectionery | 1,766 | 88 | 80 | 27 | 431 | 27 |
| 5 Cakes | 1,819 | 277 | 266 | 121 | 1,879 | 9 |
| 6 Seasonal bread | 292 | 67 | 63 | 7 | 173 | 0 |

Extreme values: Cakes on 31 Dec (1,879 in 2014, 1,870 in 2015, 1,705 in 2016); Rolls and Croissants on 2014-05-05 and 2013-08-03 (cause unknown); Confectionery peaks on Sundays in February (2014-02-23: 431; 2014-02-09: 366; 2015-02-22: 330).

### Days without sales (38)

- **26 are public holidays:** 1 Jan (5×), Good Friday (5×), 1 May (4×), 25/26 Dec (10×), Whit Monday 2018-05-21, Reformation Day 2017-10-31.
- **12 are not public holidays:** 2013-12-28, 2014-05-03, 2014-05-04, 2014-08-17, 2016-03-24 (Maundy Thursday), 2016-07-07, 2016-07-18, 2016-08-14, 2016-08-15, 2016-12-17, 2017-07-04, 2017-10-23. Reason unknown (closure, technical failure, missing data?).
- The branch opens on other holidays (Easter Monday, Ascension Day, 3 Oct, and Whit Monday before 2018 have sales).

### Confectionery (group 4): 53 opening days without a row

- By year: 2013: 16 · 2014: 23 · 2015: 10 · 2016: 4 · 2017–2018: 0.
- By month: December 16, July 11; others ≤ 5. Includes 24 Dec and 31 Dec in 2013 and 2014.
- On these days groups 1–3 together sell **860** on average, compared with **683** on other opening days, so the gaps fall on busy days and are **not random**. Possible meanings: not offered, sold out early, or not recorded. The data cannot tell which. The gaps occur on every weekday, with 13 on Wednesdays and one on Sundays.

### Seasonal bread (group 6): season boundaries

| Season | First day | Last day | Rows |
|---|---|---|---|
| 2013/14 | 2013-10-24 | 2014-01-02 | 65 |
| 2014/15 | 2014-10-24 | 2015-01-06 | 66 |
| 2015/16 | 2015-11-02 | 2015-12-31 | 53 |
| 2016/17 | 2016-11-03 | 2016-12-29 | 52 |
| 2017/18 | 2017-10-30 | 2017-12-27 | 56 |

The October–January window has 596 recorded opening days, including the 292 days with seasonal-bread sales. By month there are 13 rows in October, 140 in November, 133 in December, and 6 in January. The start varies between 24 Oct and 3 Nov and the end between 27 Dec and 6 Jan; there are a few single gaps inside a season (e.g. 2013-10-28, 2013-12-31).

---

## 2. Weather – `wetter.csv`

| Item | Value |
|---|---|
| Shape | 2,601 rows × 5 columns |
| Grain / key | one row per date; `Datum` unique |
| Period | 2012-01-01 – 2019-08-01, with observations on 2,601 of 2,770 calendar days |
| Missing dates | 169 in total (2012: 33, 2013: 120, 2016: 1, 2017: 2, 2018: 12, 2019: 1). **3 in the sales period** (2016-12-11, 2017-10-04, 2017-10-05); 13 in the Kaggle test year |
| `Bewoelkung` | 0–8 octas, mean 4.8; **10 missing**, all consecutive: 2017-10-30 – 2017-11-08 (validation year) |
| `Temperatur` | −10.25 to 32.67 °C, mean 12.1 °C. Every row has a value. |
| `Windgeschwindigkeit` | 3 – 35, mean 11.2, integer; 60 days > 20. **Unit doubtful**: a daily mean of 35 m/s would be hurricane force; the values may be in knots or another unit |
| `Wettercode` | 41 distinct WMO codes (0–95); **669 missing** |

**Wettercode missingness is not random.** Days without a code have lower cloud cover (mean 3.3 vs 5.3 octas; 143 of them are fully clear) and higher temperature (15.4 vs 10.9 °C). The code is blank on 25.7% of observed dates. The missing share is highest in May–September (34–38%) and lowest in December–January (11–12%). Code 0 occurs in the source. In the upper-limit experiment, the team assigns blank codes their own category for days with nothing notable reported.

---

## 3. Kiel Week – `kiwo.csv`

| Item | Value |
|---|---|
| Shape | 72 rows × 2 columns; `KielerWoche` is always 1 |
| Grain / key | one row per Kiel Week day; `Datum` unique |
| Coverage | 2012–2019, 9 consecutive days per year (Saturday to Sunday of the following week, mid/late June) |
| In the sales period | 2014–2018 = **5 Kiel Weeks, 45 days**, all with sales. Kiel Week 2013 (22–30 June) is just before the sales data starts |

---

## 4. Joins (sales ← weather, sales ← Kiel Week, on `Datum`, left join)

| Check | Result |
|---|---|
| Row count after both joins | 9,334 (unchanged) |
| Sales dates with weather | 1,816 of 1,819; 16 sales rows get no weather |
| Missing after join | `Temperatur`/`Windgeschwindigkeit` 16, `Bewoelkung` 70, `Wettercode` 2,325 |
| Kiel Week | 223 sales rows on 45 dates. The other 9,111 rows get a flag of 0. |

Weather matches 99.84% of sales dates (69.82% of weather dates). Kiel Week matches 2.47% of sales dates (62.50% of event dates). An inner join would keep 9,318 sales rows for weather or 223 for Kiel Week.

---

## 5. Training-period observations

The exploration notebook shows turnover distributions and weekday medians in Monday–Sunday order. On Sunday, median turnover is lowest for bread and highest for rolls, croissants, confectionery, and cakes compared with those groups’ other weekdays.

Temperature has the largest absolute Pearson correlation with turnover among the three observed weather measures for every product group. Its correlation is 0.62 for croissants and 0.55 for rolls, each based on 1,461 paired dates. These comparisons are unadjusted for weekday or season. The [canvas](../CANVAS.md) also records the team’s regression findings with calendar adjustments.

## 6. Forecast inputs and checks

- The weather file contains observations. The upper-limit experiment may use observed weather, with wind speed excluded under the team’s decision. Typical weather uses training data only. The sales `id` encodes the date and serves as a row identifier.
- The team treats the 12 non-holiday dates without sales as unplanned closures. The reasons for the missing confectionery rows remain unknown. The data provides turnover. Piece counts, prices, stockouts, and waste are unavailable.
- The [canvas](../CANVAS.md#8-checks-) lists the approved checks. The implemented checks are in [checks/](../checks/).
