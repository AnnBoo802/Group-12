# Decisions

Newest first. One entry per decision taken at a stop point.

<!--
## YYYY-MM-DD: <short title>
**Canvas block:** <number>
**Decision:** <what was decided>
**Reason:** <why>
**Alternatives considered:** <what else, and why not>
**Decided by:** <names>
-->

## 2026-11-22: Gaps in cloud cover and days without weather are left empty
**Canvas block:** 7
**Decision:** The 10 missing `Bewoelkung` values (2017-10-30 – 11-08) and the 3 sales dates without any weather (2016-12-11, 2017-10-04, 2017-10-05; 16 sales rows) stay empty (NA); no interpolation.
**Reason:** Team choice: do not invent weather values. Only relevant for the upper-limit experiment; models that cannot handle NA must say how they treat these rows.
**Alternatives considered:** linear interpolation from neighbouring days (recommended by the agent); dropping the rows.
**Decided by:** Group 12

## 2026-11-22: Missing weather code gets its own category
**Canvas block:** 7
**Decision:** `Wettercode` is not used for typical weather. In the upper-limit experiment, a missing code becomes its own category ("nothing notable reported").
**Reason:** Missingness is not random (clearer, warmer days: cloud cover 3.3 vs 5.3 octas, 15.4 vs 10.9 °C); the absence itself carries information.
**Alternatives considered:** drop the column; impute a code.
**Decided by:** Group 12

## 2026-11-22: Wind speed is dropped
**Canvas block:** 7
**Decision:** The column `Windgeschwindigkeit` is not used. There is no "bad weather" rule based on wind.
**Reason:** The unit is doubtful (daily means up to 35 "m/s") and the proposed rule (wind > 10 and no weather code) would flag 200 days with a threshold near the median.
**Alternatives considered:** use as relative scale; bad-weather rule wind > 10 (see superseded entry below).
**Decided by:** Group 12
**Consequence:** supersedes "Wind speed and 'bad weather' rule" (2026-11-22).

## 2026-11-22: Checks for block 8
**Canvas block:** 8
**Decision:** Keep all 10 proposed checks (listed in CANVAS.md block 8): raw-data shape and keys, no missing/non-positive turnover, join keeps 9,334 rows, Kiel Week flag 0/1 with 45 dates, seasonal bread only Oct–Jan, closed days never forecast, split boundaries, sales features only up to month M−1, training-only fitting, weekday order Monday–Sunday.
**Reason:** Each one protects a fact the analysis depends on; a failure means stop and look.
**Alternatives considered:** a subset (would leave the leakage rules unchecked).
**Decided by:** Group 12

## 2026-11-22: Limits of the data (block 2): unplanned closures, unknown reason for missing confectionery
**Canvas block:** 2, 1
**Decision:** The 12 days without sales that are not public holidays are treated as **unplanned closures**. The reason why confectionery rows are missing on 53 days is **unknown**. Both are recorded as things the data cannot answer.
**Reason:** No information from the bakery explains them.
**Consequence:** refines block 1 "closed days are known to the manager": this holds for public holidays only; unplanned closures can happen and cannot be forecast.
**Decided by:** Group 12

## 2026-11-22: Encoding of product group and weekday
**Canvas block:** 7
**Decision:** Product group and weekday (Monday–Sunday) are encoded as categories (one dummy column per value), not as numbers.
**Reason:** The codes 1–6 and 0–6 are labels, not quantities; as numbers a linear model would assume e.g. that group 4 lies "between" groups 3 and 5.
**Alternatives considered:** numeric codes (false ordering); separate model per group (possible later as an experiment).
**Decided by:** Group 12

## 2026-11-22: Wind speed and "bad weather" rule (SUPERSEDED: wind speed is dropped, see above)
**Canvas block:** 7
**Decision:** Wind speed is used as given (unit doubtful, no conversion). A day counts as **bad weather** if wind speed > 10 and no further weather information is available (interpreted as: `Wettercode` missing).
**Reason:** Team rule: strong wind is the only remaining signal on days without a weather code.
**Evidence:** in the sales period this flags 200 of the 463 days without a weather code (884 of 1,854 days have wind > 10, so > 10 is close to the median).
**Limit:** based on observed weather, so usable only in the upper-limit experiment (block 6); the unit of wind speed is uncertain.
**Decided by:** Group 12

## 2026-11-22: Typical weather from training years only
**Canvas block:** 6, 7
**Decision:** "Typical weather" = average per calendar week, computed on the training years (2013-07-01 – 2017-07-31) only.
**Reason:** Calendar week is known in advance; using validation or test years would leak.
**Alternatives considered:** monthly average (coarser); no weather at all (still an option for the main result).
**Decided by:** Group 12

## 2026-11-22: Extreme values are kept
**Canvas block:** 7
**Decision:** Keep all extreme values (e.g. cakes on 31 Dec ≈ 1,880, rolls/croissants on 2014-05-05 and 2013-08-03, confectionery on February Sundays) as real demand; capture New Year's Eve with a calendar feature.
**Reason:** They are plausible high-demand days; capping or removing them would make the model underestimate exactly these days.
**Alternatives considered:** capping (winsorising); removing.
**Decided by:** Group 12

## 2026-11-22: Closed days are not forecast
**Canvas block:** 1, 7
**Decision:** All 38 days without sales (26 public holidays, 12 unplanned closures) have no row and are not forecast.
**Reason:** No sales to learn from or to evaluate; the 12 non-holiday closures are recorded as a limit.
**Alternatives considered:** flagging days before/after a closure (only 12 cases).
**Decided by:** Group 12

## 2026-11-22: Seasonal-bread season is known in advance
**Canvas block:** 6, 7
**Decision:** The seasonal-bread season counts as known in advance. Forecast group 6 only on days that have a row (or appear in the Kaggle test file).
**Reason:** The manager decides when seasonal bread is offered; season start (24 Oct – 3 Nov) and end (27 Dec – 6 Jan) vary by year.
**Alternatives considered:** fixed window 24 Oct – 6 Jan (would create in-window days without sales).
**Decided by:** Group 12

## 2026-11-22: Missing confectionery rows are not filled
**Canvas block:** 7
**Decision:** The 53 opening days without a confectionery (group 4) row stay without a row: not used for training, not forecast, not in the MAPE.
**Reason:** The gaps fall on busier-than-usual days (groups 1–3: 860 vs 683), so they are not zero demand; filling with 0 or an estimate would invent data, and MAPE is undefined at 0.
**Alternatives considered:** fill with 0; fill with weekday average.
**Decided by:** Group 12

## 2026-11-22: Left join of weather and Kiel Week onto sales
**Canvas block:** 7
**Decision:** Join `wetter.csv` and `kiwo.csv` onto the sales data with a left join on `Datum` (`how="left"`), so every sales row stays. Days without a Kiel Week entry get `KielerWoche` = 0.
**Reason:** Sales rows are the unit we forecast; no sales day may be lost or duplicated. Checked: the join keeps all 9,334 rows; 16 rows (3 dates) get no weather.
**Alternatives considered:** inner join (would drop the 16 sales rows without weather); outer join (would add weather-only days without sales).
**Decided by:** Group 12

## 2026-11-17: Time-based split with one validation year
**Canvas block:** 7
**Decision:** Training 2013-07-01 – 2017-07-31; validation 2017-08-01 – 2018-07-31; test = Kaggle year, used once at the end. No shuffling across time.
**Reason:** One full validation year covers all seasons and mirrors the length of the Kaggle test year.
**Alternatives considered:** last 3 months as validation (misses most seasons).
**Decided by:** Group 12
**Limit:** the validation year has only one Kiel Week and one seasonal-bread season.

## 2026-11-17: Known in advance: calendar yes, observed weather only as an upper-limit experiment
**Canvas block:** 6
**Decision:** Calendar, holidays, school holidays and Kiel Week dates may be used. Sales only up to the last day of month M−1 for days in month M+1. Main result without observed weather (no weather or typical weather); observed weather only in a separate experiment, reported as an upper limit.
**Reason:** The manager cannot know actual weather 4–8 weeks ahead; calendar events are published in advance.
**Alternatives considered:** observed weather in the main model (leakage for the real plan, although the Kaggle test data includes it).
**Decided by:** Group 12

## 2026-11-17: Seasonal baseline replaces "same weekday last week"
**Canvas block:** 4
**Decision:** Baseline = average turnover per product group × weekday × month, computed on training years only.
**Reason:** "Same weekday last week" is not available 4–8 weeks ahead; the average is stable and captures weekly and seasonal patterns.
**Alternatives considered:** same weekday in the same week one year earlier (depends on single random days).
**Decided by:** Group 12

## 2026-11-17: Monthly planning, one month ahead
**Canvas block:** 1, 6
**Decision:** On the 1st of month M the manager plans all opening days of month M+1. Sales up to the planning day are known.
**Reason:** A monthly plan is realistic for ordering and staff scheduling and still allows recent sales as input.
**Alternatives considered:** once a year for 12 months (Kaggle setting, no recent sales).
**Decided by:** Group 12
**Consequence:** refines "Forecast is made weeks to months ahead, without recent sales" (2026-11-17): sales up to the planning day are now available.

## 2026-11-17: Success criterion and metrics
**Canvas block:** 4
**Decision:** Main metric MAPE per product group, with MAE alongside. Under- and over-forecasts count equally. Good enough = lower MAPE than the naive baseline in each of product groups 1–5 on validation data; seasonal bread reported separately.
**Reason:** MAPE is the course requirement; MAE shows the error in turnover, which small groups' percentages exaggerate. No cost data for sold-out vs. leftovers.
**Alternatives considered:** MAPE only (misleading for small groups); asymmetric loss (needs cost data we lack).
**Decided by:** Group 12

## 2026-11-17: Audiences
**Canvas block:** 3
**Decision:** Operations manager gets a plain table/chart with the typical error; technical readers get notebooks, README and the baseline comparison.
**Reason:** The manager acts on numbers, not on models; the course assesses the method.
**Alternatives considered:** one shared report for both (too technical for the manager, too thin for reviewers).
**Decided by:** Group 12

## 2026-11-17: Forecast is made weeks to months ahead, without recent sales
**Canvas block:** 1, 6
**Decision:** The forecast is made weeks to months ahead of the forecast day; no sales after the planning moment are available.
**Reason:** Matches the course's Kaggle setting (test year Aug 2018 – Jul 2019 comes without sales).
**Alternatives considered:** 1 day ahead ("tomorrow"); 7 days ahead. Both would allow recent sales as input.
**Decided by:** Group 12
**Consequence:** supersedes the baseline "same weekday last week" (2026-11-17), which needs last week's sales. Replacement: see next round.

## 2026-11-17: Naive baseline is "same weekday last week"
**Canvas block:** 1, 4
**Decision:** The baseline to beat is the turnover of the same product group on the same weekday one week earlier. It stands in for the manager's current practice.
**Reason:** It is the simplest rule a real manager would use and can be computed from the data.
**Alternatives considered:** average of recent weeks (less common in practice); gut feeling (cannot be reproduced).
**Decided by:** Group 12

## 2026-11-17: Scope is one branch, six product groups, opening days only
**Canvas block:** 1
**Decision:** Forecast all six product groups; seasonal bread only in its Oct–Jan season; no forecasts for closed days.
**Reason:** The manager knows in advance when seasonal bread is on offer and when the branch is closed.
**Alternatives considered:** forecasting closed days as zero (adds no value for the decision).
**Decided by:** Group 12

## 2026-11-17: Deliver a turnover forecast, not baking quantities
**Canvas block:** 1, 2
**Decision:** We forecast turnover per product group and day; the manager converts it into baking quantities.
**Reason:** The data contains turnover only, no piece counts, prices or waste.
**Alternatives considered:** quantities in pieces (no data); forecast plus safety margin (needs leftover vs. sold-out costs; parked).
**Decided by:** Group 12
