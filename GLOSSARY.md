# Glossary

One entry per term, variable or code the project uses. Keep the canonical name, the meaning, the unit and anything that is easy to get wrong.

| Term | Meaning | Unit / values | Notes |
|---|---|---|---|
| Umsatz | Turnover of one product group on one day; the forecast target | Currency not stated in source | Not a quantity in pieces. Capped by what was baked: sold-out days understate demand. |
| Warengruppe | Product group | 1 Bread, 2 Rolls, 3 Croissants, 4 Confectionery, 5 Cakes, 6 Seasonal bread | Confectionery has no row on 53 recorded opening days. Seasonal bread has 292 rows within the Oct–Jan window. |
| Opening day | A day with sales in at least one product group | 1,819 of 1,857 days (2013-07-01 – 2018-07-31) | The 38 days without sales are mostly holidays; they are not forecast. |
| Naive baseline | (superseded) Turnover of the same product group on the same weekday one week earlier | Turnover | Not available with monthly planning; replaced by the seasonal baseline. |
| Seasonal baseline | Forecast = average turnover per product group × weekday × month over the training years | Turnover | The baseline to beat (block 4). |
| Lead time | Time between the planning day and the day forecast | About 4–8 weeks | Plan on the 1st of month M for all days of month M+1. |
| Planning day | The 1st of month M, when the plan for month M+1 is made | Date | Sales-based features may use data up to the last day of month M−1 only. |
| MAPE | Mean absolute percentage error: average of abs(actual − forecast) / actual | % | Main metric (course). Exaggerates errors on small values (e.g. seasonal bread). |
| MAE | Mean absolute error: average of abs(actual − forecast) | Turnover | Shown alongside MAPE. |
| id | Row key of the sales data | `YYMMDD` + product group, e.g. 1307011 | Same format in Kaggle test/submission. Encodes the date: never use as a numeric feature. |
| Datum | Date | `YYYY-MM-DD` | Join key for all three files. |
| Bewoelkung | Mean daily cloud cover | Octas, 0 (clear) – 8 (overcast) | Observed weather: not known in advance. 10 missing (2017-10-30 – 11-08). |
| Temperatur | Mean daily temperature | °C | Observed weather: not known in advance. |
| Windgeschwindigkeit | Mean daily wind speed | Stated as m/s, integers 3–35 | Unit doubtful (35 m/s daily mean is implausible). **Not used in the project** (DECISIONS.md 2026-11-22). |
| Wettercode | WMO present-weather code of the day | 00–99 | Code 0 occurs in the source. The 669 blank days tend to be clearer and warmer. Missing codes have their own category in the upper-limit experiment. |
| KielerWoche | Kiel Week day flag | 1 in `kiwo.csv`; 0 after setting NA to 0 in the join | 9 days per year; 5 Kiel Weeks in the sales period. Known in advance. |
| Closed day | Calendar day without any sales row | 38 days in 2013-07 – 2018-07 | 26 public holidays, 12 other days of unknown cause. |
| Seasonal-bread season | Days on which product group 6 is sold | About 24 Oct – 6 Jan | Start and end vary by year (see fact sheet). |
| Validation year | 2017-08-01 – 2018-07-31, used to compare models | Dates | Only one Kiel Week and one seasonal-bread season. |
