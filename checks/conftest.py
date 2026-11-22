"""Shared fixtures for the checks: the three raw files, loaded once per test run.

Raw data is read-only: the checks only read it from the course repository.
"""

import pandas as pd
import pytest

BASE_URL = "https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/"


@pytest.fixture(scope="session")
def sales():
    return pd.read_csv(BASE_URL + "umsatzdaten_gekuerzt.csv", parse_dates=["Datum"])


@pytest.fixture(scope="session")
def weather():
    return pd.read_csv(BASE_URL + "wetter.csv", parse_dates=["Datum"])


@pytest.fixture(scope="session")
def kiel_week():
    return pd.read_csv(BASE_URL + "kiwo.csv", parse_dates=["Datum"])


@pytest.fixture(scope="session")
def merged(sales, weather, kiel_week):
    """The join decided by the team (DECISIONS.md, 2026-11-22): left join on the date."""
    data = sales.merge(weather, on="Datum", how="left").merge(kiel_week, on="Datum", how="left")
    data["KielerWoche"] = data["KielerWoche"].fillna(0).astype(int)
    return data
