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
