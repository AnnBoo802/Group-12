# Agentic Data Science Canvas

**Project:** Group 12 – Bakery sales forecast
**Team (GitHub usernames):** aqibzaidi35, AnnBoo802, kalathokiprashant30-dotcom
**Version:** 2026-11-17

> Owners: 👤 human decides · 🤖 agent drafts, human approves.
> Keep each block short. Details go in linked files; decisions go in `DECISIONS.md`.

---

## Problem

### 1. Decision 👤
<!-- Who decides what, when and how often? What happens today without this analysis? -->
**Decision:** each month, the operations manager plans how much of each product group to bake on every opening day of the following month. (Original question: *how much of each product group should we bake for tomorrow?*)
- **Who / what:** the operations manager of one branch decides how much to bake per product group (all six; seasonal bread only in its Oct–Jan season).
- **What we deliver:** a forecast of the **turnover** per product group per opening day. The manager converts it into baking quantities (we have no piece counts or prices).
- **When / how often:** once a month. On the 1st of month M the manager plans every opening day of month M+1 (lead time about 4–8 weeks). Sales up to the planning day are known.
- **Closed days** (holidays without sales) are known to the manager and are not forecast. Unplanned closures (12 days in the data) are not known in advance (see block 2).
- **Today, without this analysis:** the manager uses typical values per product group, weekday and month (team assumption, stands in for the real practice; see seasonal baseline in block 4).

### 2. Questions 👤
<!-- The analysis questions that would change the decision. For each: what the data can answer, and what it cannot. -->
- **Main question:** what turnover will each product group reach on a given opening day, as known on the 1st of the month before (sales up to that day available)?
- **The data cannot answer:** quantities in pieces (only turnover); demand above what was baked (sold-out days look like low demand); cost of leftovers (no waste data); other branches (one branch only).
- **Also cannot answer:** unplanned closures (12 non-holiday days without sales) cannot be foreseen; why confectionery has no row on 53 days is unknown.
- **Thin evidence:** Kiel Week (5 occurrences, 2014–2018) and seasonal bread (5 seasons) rest on 5 cases each.
- **Tested hypotheses (2026-11-22):** training years only (2013-07-01 – 2017-07-31); daily turnover of groups 1–5 on the 1,409 days with all five groups; regression on log turnover with weekday, month and year held fixed (effects in %, 95 % confidence interval).
  - **H1 Rain → less sales: confirmed, small.** About −2 % on rainy days (CI −3.7 to −0.6 %); the same with only days that have a weather code, and with temperature added (temperature itself: +0.1 % per °C, no effect). By group: bread −4.6 %, croissants −2.9 %, cakes −2.6 %; rolls (−1.2 %) and confectionery (−0.1 %) show no clear difference. Raw averages hide it (rain 1,031 vs dry 1,024) because the season matters far more. Rain = WMO rain, drizzle or shower codes. *Limit:* observed weather, not known in advance → upper-limit experiment only.
  - **H2 Kiel Week → more sales: confirmed.** About +15 % (CI +9 to +20 %). Every year shows it vs the same weekdays 3 weeks before and after: 2014 +10 %, 2015 +13 %, 2016 +10 %, 2017 +8 %. By group: croissants +24 %, rolls +19 %, cakes +7 %; bread (+8 %) and confectionery (+10 %) not clearly different from zero. *Limit:* only 4 Kiel Weeks (34 days) in the training years.
  - **H3 Higher sales in autumn and winter: rejected; the opposite holds.** Mean daily turnover: summer 1,304, autumn 1,013, spring 987, winter 892. Compared with summer (weekday and year fixed): autumn −24 %, winter −32 %; autumn equals spring (−0.3 %), winter about −11 % below spring. Peak in July/August (1,312 / 1,465), low in November–January (858–884); unchanged without 24–31 Dec. Croissants and rolls drive the summer peak (croissants 242 summer vs 110 winter); only confectionery is higher in winter (100 vs 82). Seasonal bread (about 60–80 per day) does not change the pattern. Why sales peak in summer (e.g. tourists) is not in the data.
  - **Consequence:** calendar (month/season, weekday) and Kiel Week carry the strongest signal and are known in advance; rain adds about 2 %, and only in the upper-limit experiment.

### 3. Audiences 👤
<!-- Who receives which result, in which form? At least: the decision-maker and the technical reader. -->
- **Operations manager (decision-maker):** table or chart per day and product group, typical error in plain words ("usually off by about X %"), no model details.
- **Technical readers (course instructors, other teams):** notebooks, README with errors per product group, comparison to both baselines.

### 4. Success 👤
<!-- Metric(s), the baseline to beat, what is good enough to act on. Which errors are worse than others? -->
- **Metrics:** MAPE per product group (main, course requirement) and MAE in turnover alongside (shows what an error means in money terms).
- **Error direction:** too low (sold out) and too high (leftovers) are weighted equally, because their costs are unknown. Limit: the manager may need a safety margin on top.
- **Good enough:** lower MAPE than the seasonal baseline in each of product groups 1–5 on validation data. Seasonal bread (6) is reported separately (only 5 seasons).
- **Segments to check:** product group, weekday, holidays, Kiel Week (only 5 occurrences: report with that limit).
- **Baseline to beat:** seasonal baseline = average turnover per product group × weekday × month, computed on the training years only. Second reference: linear regression (course requirement).

---

## Data and method

### 5. Data 🤖
<!-- Sources, unit of observation, period covered, keys, known gaps. Link the data fact sheet. -->
See the [data fact sheet](docs/data-fact-sheet.md) for source coverage, missing values, and join results.

- **Sales:** 9,334 rows, one per product group × opening day, 2013-07-01 – 2018-07-31; key (`Datum`, `Warengruppe`) unique; no NAs. 1,819 opening days; 38 days without sales (26 public holidays, 12 others of unknown cause).
- **Gaps:** confectionery has no row on 53 opening days, mostly in 2013–14 and late December. Sales across groups 1–3 are higher on those days. Seasonal bread has sales on 292 of 596 recorded opening days in October–January. Its observed season starts between 24 Oct and 3 Nov and ends between 27 Dec and 6 Jan.
- **Weather:** 2012 – 2019-08-01, one row per date; 3 sales dates without weather; `Wettercode` missing on 669 days (not at random: clearer, warmer days); cloud cover missing on 10 consecutive validation days; wind-speed unit doubtful. Observed values only.
- **Kiel Week:** 9 days per year 2012–2019; 5 Kiel Weeks (45 days) inside the sales period.
- **Join:** left join on `Datum` keeps 9,334 rows; Kiel Week NA → 0.

### 6. Known in advance 👤
<!-- What information is available at the moment the result is needed? Everything else is leakage. -->
**Moment:** the 1st of month M; the forecast covers all opening days of month M+1.
- **Known:** calendar (date, weekday, month, year); public holidays and school holidays (published years ahead; external source, not yet chosen); Kiel Week dates; seasonal-bread season; closed days.
- **Known up to the planning day only:** sales. For a day in month M+1, sales-based features may use data **up to the last day of month M−1** at most, never later (e.g. no "same weekday last week").
- **Not known:** actual weather. The main result uses no weather or typical weather (e.g. average temperature of the calendar week). Observed weather only in a separate experiment, reported as an upper limit ("if the weather were known exactly").
- **Not known:** any value from month M+1 itself, or from month M after the planning day.

### 7. Data decisions 👤
<!-- Joins, missing values, encodings, exclusions, each with a reason. Link the entries in DECISIONS.md. -->
- **Split (time-based, see DECISIONS.md):** training 2013-07-01 – 2017-07-31; validation 2017-08-01 – 2018-07-31; test = Kaggle year 2018-08-01 – 2019-07-31, used once at the end. Learned transformations are fitted on training data only.
- **Join (see DECISIONS.md):** left join of weather and Kiel Week onto sales on `Datum`; every sales row stays (9,334); missing `KielerWoche` → 0.
- **Missing confectionery rows (53 days):** not filled; not trained on, not forecast, not in MAPE.
- **Seasonal bread:** season known in advance; forecast only days with a row / Kaggle test id.
- **Closed days (38):** no row, not forecast.
- **Extreme values:** kept; New Year's Eve as calendar feature.
- **Typical weather:** calendar-week average from training years only.
- **Wind speed:** dropped (unit doubtful); no bad-weather rule.
- **Weather gaps (upper-limit experiment only):** missing `Wettercode` = own category; the 10 cloud-cover gaps and 3 days without weather stay empty (NA).
- **Encoding:** product group and weekday (Mon–Sun) as categories (dummy columns).

### 8. Checks 🤖
<!-- Checkpoints and the invariants that must hold at each (row counts, keys, date ranges, IDs, baseline). Link checks/. -->
Run with `uv run python -m pytest checks`. ✅ marks checks implemented in [checks/](checks/).

1. ✅ Raw sales: 9,334 rows; (`Datum`, `Warengruppe`) unique; `id` = YYMMDD + group; product groups 1–6; dates 2013-07-01 – 2018-07-31.
2. ✅ No missing or ≤ 0 `Umsatz`.
3. ✅ Every join keeps exactly 9,334 rows.
4. ✅ `KielerWoche` only 0/1 after the join; 45 Kiel Week dates in the sales period.
5. ✅ Group 6 rows only in Oct–Jan.
6. The 38 closed days have no rows (✅) and are never forecast (to add once forecasts exist).
7. Split: training max 2017-07-31; validation 2017-08-01 – 2018-07-31; no overlap.
8. Sales-based features for a day in month M+1 use data up to the last day of month M−1 only.
9. Seasonal baseline, typical weather and every fitted transformation use training dates only.
10. Weekday order in outputs is Monday–Sunday.

---

## Evidence and action

### 9. Experiments 🤖
<!-- Experiment cards and their status; best result so far vs. baseline. Link experiments/LOG.md. -->

### 10. Findings 🤖
<!-- What we learned, how sure we are, and what the data cannot tell. -->

### 11. Recommendation 👤
<!-- What the decision-maker should do, under which conditions. Signed off by the team. -->

---

## Open questions
<!-- Parking lot. Each item names who resolves it. -->
- **Kaggle submission vs. monthly setting:** the Kaggle test year has no sales, so sales-based features cannot be computed there. Submit a model without sales features, or skip such features for Kaggle? *Team decides before modelling.*
- **No weather vs. typical weather** for the main result: *team decides from validation results (both allowed, no observed weather).*
- **Source for holidays and school holidays (Schleswig-Holstein):** *team picks a source; agent adds it to AGENTS.md and the README.*
- **Safety margin** for sold-out vs. leftovers: possible extension; needs cost information from the manager. *Team.*
- **Validation year has one Kiel Week and one seasonal-bread season:** results for these are single cases. *Report as limit.*

## Decision log
See `DECISIONS.md`.
