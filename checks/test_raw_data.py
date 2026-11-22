"""Checks on the raw sales data (canvas block 8, checks 1, 2, 5 and 6).

Run all checks with:  uv run python -m pytest checks
If one of these fails, the raw data is not what we think it is: stop and look before analysing.
"""

import pandas as pd


# Check 1: shape, keys, product groups, period
def test_sales_loads_with_expected_columns(sales):
    assert list(sales.columns) == ["id", "Datum", "Warengruppe", "Umsatz"]


def test_sales_row_count_matches_documentation(sales):
    assert len(sales) == 9334


def test_one_row_per_date_and_product_group(sales):
    assert sales["id"].is_unique
    assert not sales.duplicated(["Datum", "Warengruppe"]).any()


def test_id_is_date_plus_product_group(sales):
    expected = sales["Datum"].dt.strftime("%y%m%d").astype(int) * 10 + sales["Warengruppe"]
    assert (sales["id"] == expected).all()


def test_product_groups_and_date_range(sales):
    assert set(sales["Warengruppe"]) == {1, 2, 3, 4, 5, 6}
    assert sales["Datum"].min() == pd.Timestamp("2013-07-01")
    assert sales["Datum"].max() == pd.Timestamp("2018-07-31")


# Check 2: turnover is present and positive
def test_turnover_has_no_missing_or_non_positive_values(sales):
    assert sales["Umsatz"].notna().all()
    assert (sales["Umsatz"] > 0).all()


# Check 5: seasonal bread only in its season
def test_seasonal_bread_only_october_to_january(sales):
    months = sales.loc[sales["Warengruppe"] == 6, "Datum"].dt.month
    assert set(months) <= {10, 11, 12, 1}


# Check 6 (raw-data part): exactly 38 closed days, none of them with a row.
# The second part ("never forecast") is checked once forecasts exist.
def test_38_closed_days_without_rows(sales):
    calendar = pd.date_range("2013-07-01", "2018-07-31")
    closed = calendar.difference(sales["Datum"].unique())
    assert len(closed) == 38
