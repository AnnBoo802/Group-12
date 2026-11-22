# Data fact sheet

Profiled on 2026-11-22 from the raw files at `https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/`. All numbers below were computed with pandas, not copied from the course README (where they overlap, they agree). Reproduce them with [1_DatasetCharacteristics/data_profile.ipynb](../1_DatasetCharacteristics/data_profile.ipynb). Decisions taken on these facts: [DECISIONS.md](../DECISIONS.md).

**Origin and license:** provided by meteolytix GmbH (Kiel) to the opencampus.sh course; the license is not stated in the source. One bakery branch in Kiel.

---

## 1. Sales – `umsatzdaten_gekuerzt.csv`

| Item | Value |
|---|---|
| Shape | 9,334 rows × 4 columns (`id`, `Datum`, `Warengruppe`, `Umsatz`) |
| Grain | one row = one product group on one day with sales |
| Key | `id` unique; (`Datum`, `Warengruppe`) unique (0 duplicates); `id` = `YYMMDD` + group for every row |
| Period | 2013-07-01 – 2018-07-31 = 1,857 calendar days; first and last months are complete (148 and 155 rows) |
| Opening days | 1,819 days with at least one row; 38 days without any row |
| Missing values | none in any column; `Umsatz` > 0 everywhere (min 7.05) |
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
- On these days groups 1–3 together sell **860** on average, compared with **683** on other opening days, so the gaps fall on busy days and are **not random**. Possible meanings: not offered, sold out early, or not recorded. The data cannot tell which.

### Seasonal bread (group 6): season boundaries

| Season | First day | Last day | Rows |
|---|---|---|---|
| 2013/14 | 2013-10-24 | 2014-01-02 | 65 |
| 2014/15 | 2014-10-24 | 2015-01-06 | 66 |
| 2015/16 | 2015-11-02 | 2015-12-31 | 53 |
| 2016/17 | 2016-11-03 | 2016-12-29 | 52 |
| 2017/18 | 2017-10-30 | 2017-12-27 | 56 |

Rows by month: Oct 13, Nov 140, Dec 133, Jan 6. The start varies between 24 Oct and 3 Nov and the end between 27 Dec and 6 Jan; there are a few single gaps inside a season (e.g. 2013-10-28, 2013-12-31).

---

## 2. Weather – `wetter.csv`

| Item | Value |
|---|---|
| Shape | 2,601 rows × 5 columns |
| Grain / key | one row per date; `Datum` unique |
| Period | 2012-01-01 – 2019-08-01 (covers the Kaggle test year) |
| Missing dates | 169 in total (2012: 33, 2013: 120, 2016: 1, 2017: 2, 2018: 12, 2019: 1). **3 in the sales period** (2016-12-11, 2017-10-04, 2017-10-05); 13 in the Kaggle test year |
| `Bewoelkung` | 0–8 octas, mean 4.8; **10 missing**, all consecutive: 2017-10-30 – 2017-11-08 (validation year) |
| `Temperatur` | −10.3 – 32.7 °C, mean 12.1; no missing values |
| `Windgeschwindigkeit` | 3 – 35, mean 11.2, integer; 60 days > 20. **Unit doubtful**: a daily mean of 35 m/s would be hurricane force; the values may be in knots or another unit |
| `Wettercode` | 41 distinct WMO codes (0–95); **669 missing** |

**Wettercode missingness is not random.** Days without a code have lower cloud cover (mean 3.3 vs 5.3 octas; 143 of them are fully clear) and higher temperature (15.4 vs 10.9 °C). The missing share is highest in May–September (34–38 %) and lowest in December–January (11–12 %), and falls over the years (129 in 2014, 39 in 2018). This fits "no notable weather reported".

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
| Kiel Week | 223 sales rows on 45 dates; remaining 9,111 rows NA → must be set to 0 |

---

## 5. Against the canvas

- **Known in advance (block 6):** all weather columns are *observed* values, so they may be used only in the upper-limit experiment, and typical weather must be computed from training years only. Whether a confectionery row is missing on a day is not known in advance. `id` encodes the date, so it must not be used as a numeric feature.
- **What the data cannot answer (block 2):** whether the 12 non-holiday closures were planned (known to the manager) or unexpected; why confectionery rows are missing (not offered vs. sold out vs. not recorded).
