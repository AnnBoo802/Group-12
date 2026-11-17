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
- **Closed days** (holidays without sales) are known to the manager and are not forecast.
- **Today, without this analysis:** the manager uses typical values per product group, weekday and month (team assumption, stands in for the real practice; see seasonal baseline in block 4).

### 2. Questions 👤
<!-- The analysis questions that would change the decision. For each: what the data can answer, and what it cannot. -->
- **Main question:** what turnover will each product group reach on a given opening day, as known on the 1st of the month before (sales up to that day available)?
- **The data cannot answer:** quantities in pieces (only turnover); demand above what was baked (sold-out days look like low demand); cost of leftovers (no waste data); other branches (one branch only).
- **Thin evidence:** Kiel Week (5 occurrences, 2014–2018) and seasonal bread (5 seasons) rest on 5 cases each.

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

### 8. Checks 🤖
<!-- Checkpoints and the invariants that must hold at each (row counts, keys, date ranges, IDs, baseline). Link checks/. -->

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
