"""Checks on the raw sales data, exactly as documented in the course dataset README.

Run all checks with:  uv run pytest checks
If one of these fails, the raw data is not what we think it is: stop and look before analysing.
"""

import pandas as pd
import pytest

BASE_URL = "https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/"


@pytest.fixture(scope="module")
def sales():
    return pd.read_csv(BASE_URL + "umsatzdaten_gekuerzt.csv", parse_dates=["Datum"])


def test_sales_loads_with_expected_columns(sales):
    assert list(sales.columns) == ["id", "Datum", "Warengruppe", "Umsatz"]


def test_sales_row_count_matches_documentation(sales):
    assert len(sales) == 9334


def test_one_row_per_date_and_product_group(sales):
    assert sales["id"].is_unique
    assert not sales.duplicated(["Datum", "Warengruppe"]).any()


def test_product_groups_and_date_range(sales):
    assert set(sales["Warengruppe"]) == {1, 2, 3, 4, 5, 6}
    assert sales["Datum"].min() == pd.Timestamp("2013-07-01")
    assert sales["Datum"].max() == pd.Timestamp("2018-07-31")
