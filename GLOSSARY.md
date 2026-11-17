# Glossary

One entry per term, variable or code the project uses. Keep the canonical name, the meaning, the unit and anything that is easy to get wrong.

| Term | Meaning | Unit / values | Notes |
|---|---|---|---|
| Umsatz | Turnover of one product group on one day; the forecast target | Currency not stated in source | Not a quantity in pieces. Capped by what was baked: sold-out days understate demand. |
| Warengruppe | Product group | 1 Bread, 2 Rolls, 3 Croissants, 4 Confectionery, 5 Cakes, 6 Seasonal bread | Seasonal bread only Oct–Jan. Confectionery has no row on 53 days. |
| Opening day | A day with sales in at least one product group | 1,819 of 1,857 days (2013-07-01 – 2018-07-31) | The 38 days without sales are mostly holidays; they are not forecast. |
| Naive baseline | (superseded) Turnover of the same product group on the same weekday one week earlier | Turnover | Not available with monthly planning; replaced by the seasonal baseline. |
| Seasonal baseline | Forecast = average turnover per product group × weekday × month over the training years | Turnover | The baseline to beat (block 4). |
| Lead time | Time between the planning day and the day forecast | About 4–8 weeks | Plan on the 1st of month M for all days of month M+1. |
| Planning day | The 1st of month M, when the plan for month M+1 is made | Date | Sales-based features may use data up to the last day of month M−1 only. |
| MAPE | Mean absolute percentage error: average of abs(actual − forecast) / actual | % | Main metric (course). Exaggerates errors on small values (e.g. seasonal bread). |
| MAE | Mean absolute error: average of abs(actual − forecast) | Turnover | Shown alongside MAPE. |
| Validation year | 2017-08-01 – 2018-07-31, used to compare models | Dates | Only one Kiel Week and one seasonal-bread season. |
