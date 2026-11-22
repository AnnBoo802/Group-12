"""Checks on the joined data (canvas block 8, checks 3 and 4).

The join is a left join of weather and Kiel Week onto sales (DECISIONS.md, 2026-11-22).
"""


# Check 3: the join neither drops nor duplicates sales rows
def test_join_keeps_every_sales_row(sales, merged):
    assert len(merged) == len(sales) == 9334
    assert not merged.duplicated(["Datum", "Warengruppe"]).any()


# Check 4: Kiel Week flag is 0/1, with 45 Kiel Week dates (5 Kiel Weeks) in the sales period
def test_kiel_week_flag_is_binary_with_45_dates(merged):
    assert set(merged["KielerWoche"]) == {0, 1}
    assert merged.loc[merged["KielerWoche"] == 1, "Datum"].nunique() == 45
