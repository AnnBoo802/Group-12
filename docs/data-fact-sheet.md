# Bakery data fact sheet

The [exploration notebook](../1_DatasetCharacteristics/explore_data.ipynb) was run against all three official CSVs. The four existing [raw-sales checks](../checks/test_raw_data.py) passed. The course attributes the bakery dataset to meteolytix GmbH and gives no explicit dataset license in its documentation. [Course dataset documentation](https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/README.md)

## Source inventory

| Source | Rows × columns | What one row represents | Unique key | First and last dates | Calendar coverage |
| --- | ---: | --- | --- | --- | --- |
| `umsatzdaten_gekuerzt.csv` | 9,334 × 4 | Recorded turnover for one product group on one day | `(Datum, Warengruppe)` and `id` | 2013-07-01 to 2018-07-31 | 1,819 of 1,857 dates have sales. The first and last months reach their calendar boundaries. |
| `wetter.csv` | 2,601 × 5 | One day of measured weather in Kiel | `Datum` | 2012-01-01 to 2019-08-01 | 2,601 of 2,770 dates have observations. August 2019 contains only the first day. |
| `kiwo.csv` | 72 × 2 | One day of Kiel Week | `Datum` | 2012-06-16 to 2019-06-30 | Nine event dates each year from 2012 through 2019. Dates between events are outside the file's scope. |

Every key above is present and unique. All 9,334 sales IDs follow `YYMMDD` plus the product-group code. The Kaggle test period starts on 2018-08-01.

## Columns and missing values

| Source | Column | Parsed type | Observed range or values | Blank cells |
| --- | --- | --- | --- | ---: |
| Sales | `id` | Text | `1307011` to `1807315` | 0 |
| Sales | `Datum` | Date | 2013-07-01 to 2018-07-31 | 0 |
| Sales | `Warengruppe` | Integer code | 1–6 | 0 |
| Sales | `Umsatz` | Decimal | 7.0512–1,879.4618, currency unspecified | 0 |
| Weather | `Datum` | Date | 2012-01-01 to 2019-08-01 | 0 |
| Weather | `Bewoelkung` | Numeric | 0–8 octas | 10 |
| Weather | `Temperatur` | Decimal | −10.25–32.67 °C | 0 |
| Weather | `Windgeschwindigkeit` | Integer | 3–35 m/s, per the course documentation | 0 |
| Weather | `Wettercode` | Numeric code | Whole codes from 0 to 95 in the file | 669 |
| Kiel Week | `Datum` | Date | 2012-06-16 to 2019-06-30 | 0 |
| Kiel Week | `KielerWoche` | Integer flag | 1 on all listed dates | 0 |

Turnover is positive in every source row. All product codes, cloud-cover values, wind speeds, weather codes, and event flags passed the plausibility checks shown in the notebook.

- Weather is absent on 169 calendar dates, including 153 in 2012–2013 and three recorded sales dates. These gaps are distinct from blank cells within recorded weather rows.
- The weather code is blank on 669 of 2,601 observed days (25.7%). The rate varies by year, from 129 of 333 observed days in 2012 (38.7%) to 39 of 353 in 2018 (11.0%). Dates with a blank code have a median temperature of 16.88 °C and median wind speed of 10 m/s. Dates with a recorded code have medians of 10.46 °C and 11 m/s.
- All ten blank cloud-cover values occur in 2017 and coincide with blank weather codes. The temperature and wind speed are present for all ten. The course documentation suggests that some blank codes may represent unremarkable weather. Code 0 is an observed code, and the meaning of an individual blank remains unverified.

## Sales availability

The notebook uses a date with any recorded sales as the historical indicator of opening. It lists the 38 calendar dates with no recorded sales. The branch's schedule is needed to verify the reason for an individual gap.

| Code | Product group | Sales dates | Candidate opening dates | Dates without a sales row | Median daily turnover |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | Bread | 1,819 | 1,819 | 0 | 120.05 |
| 2 | Rolls | 1,819 | 1,819 | 0 | 370.83 |
| 3 | Croissants | 1,819 | 1,819 | 0 | 142.81 |
| 4 | Confectionery | 1,766 | 1,819 | 53 | 79.99 |
| 5 | Cakes | 1,819 | 1,819 | 0 | 265.96 |
| 6 | Seasonal bread | 292 | 596 | 304 | 62.91 |

The 596 candidate dates for seasonal bread are opening dates within October–January. The five seasons have 65, 66, 53, 52, and 56 recorded sales dates, respectively. There are six January records across the five seasons and zero records outside October–January. Confectionery gaps occur on every weekday, with 13 on Wednesdays and one on Sundays. Product availability on these dates needs confirmation from the branch.

The five highest turnover rows are all for cakes on December 31, one per year from 2013 through 2017. They range from 1,432.42 to 1,879.46.

## Date joins

The match percentages use distinct dates on each side. A left join keeps every sales row. An inner join keeps sales rows with a date in the other source.

| Join from sales on `Datum` | Shared dates | Share of sales dates | Share of source dates | Left join rows | Inner join rows | Sales rows without a match |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Weather | 1,816 | 99.84% | 69.82% | 9,334 | 9,318 | 16 |
| Kiel Week | 45 | 2.47% | 62.50% | 9,334 | 223 | 9,111 |

The three sales dates with no weather row are 2016-12-11, 2017-10-04, and 2017-10-05. The 45 matched Kiel Week dates cover nine days each year from 2014 to 2018. The other 27 event dates fall outside the sales period. Applying both left joins preserved 9,334 rows.

## Training-period observations

The notebook plots turnover distributions and Monday–Sunday medians using the approved training split. Sunday median turnover is lowest for bread and highest for rolls, croissants, confectionery, and cakes. The plots use each group's own turnover scale for the weekday view.

Paired-date Pearson correlations describe historical associations with observed weather. Temperature has the largest absolute correlation of the three measures for each product group. Its correlation is 0.62 for croissants and 0.55 for rolls, with 1,461 paired rows for each. These comparisons do not account for weekday or season. Measured weather becomes available after the monthly planning day, so the team reserves it for an upper-limit experiment. [Decision log](../DECISIONS.md)

Turnover supports the team's daily product-group forecast. Piece counts, prices, stockouts, waste, confirmed opening schedules, and product availability are absent from the files.

## Decisions for the team

| # | Decision | Options, evidence, and proposed choice |
| --- | --- | --- |
| 1 | Date joins and Kiel Week flag | Use sales-led left joins, which preserve all 9,334 rows, or use inner joins, which remove 16 rows for weather and 9,111 for Kiel Week. Proposed choice is to use left joins and set `KielerWoche` to 0 on non-event dates within the documented years. |
| 2 | Sales gaps and product availability | Keep the observed sales rows, add zero-turnover rows, or confirm availability first. The files have 38 dates with no sales, 53 confectionery gaps on recorded opening dates, and 304 seasonal-bread gaps within October–January. Proposed choice is to preserve observed rows and obtain the branch schedule and seasonal-bread offering dates for the dates being forecast. |
| 3 | Missing weather in the upper-limit experiment | Exclude affected features, restrict to complete observations, or fill gaps with training-based values and add missing indicators. The weather code is blank on 25.7% of observations, and the median temperature is 6.42 °C higher when the code is blank. Proposed choice is to start with temperature and wind, leave out the weather code, and fill gaps on the three unmatched dates using training data and a missing-weather flag. The team will use validation to decide between no weather and typical weather for the main forecast. |
| 4 | Calendar and category encoding | Use category labels or treat integer codes as ordered measurements. Proposed choice is categorical product group and weekday, weekdays displayed Monday through Sunday, a binary event flag, and the original sales ID for joins or tracing records. |
| 5 | High turnover and partial periods | Retain the observed sales range or exclude selected dates or edge periods. The five largest rows recur on December 31, and the sales boundaries are complete calendar months. Proposed choice is to retain those rows and all covered months within the approved split. |
| 6 | Holiday and opening calendar sources | Use published Schleswig-Holstein public and school holiday calendars plus the branch schedule, or defer these fields until sources are available. Proposed choice is to use official calendars and separately confirm the dates the branch will open. The team still needs to select the specific sources. |

## Proposed checks for canvas block 8

The current automated checks cover the sales columns, row count, unique keys, six group codes, and dates. Proposed additions for the team to confirm:

1. Check unique weather and Kiel Week dates. Check that both enrichment joins preserve the sales key and row count.
2. On the course snapshot, compare coverage against the measured gaps. Check that unrecorded sales rows have no manufactured turnover and that the Kiel Week flag agrees with the documented event dates.
3. Check the eligibility calendar against the confirmed branch and product schedule once they are available.
4. Check that splits are disjoint and follow the approved dates. Check that transformations use training data and that the main model uses only inputs available on the planning day.
