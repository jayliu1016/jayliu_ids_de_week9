import pytest
import pandas as pd
from mylib import data_utils, stats_utils

# Sample data for testing
sample_data = {
    "year": [2000, 2001, 2002, 2002, 2003],
    "month": [1, 2, 3, 3, 4],
    "date_of_month": [1, 2, 3, 4, 5],
    "day_of_week": [6, 7, 1, 2, 3],
    "births": [100, 200, 300, 400, 500],
}
sample_df = pd.DataFrame(sample_data)


# Test for data_utils.load_data function
def test_load_data():
    # Assuming load_data is tested for reading from a CSV, we simulate this by saving and loading sample data
    sample_df.to_csv("sample_data.csv", index=False)
    loaded_data = data_utils.load_data("sample_data.csv")

    assert isinstance(loaded_data, pd.DataFrame)
    assert not loaded_data.empty
    assert len(loaded_data) == len(sample_data["year"])


# Test for data_utils.filter_data function
def test_filter_data():
    filtered_data = data_utils.filter_data(sample_df, year=2002)

    assert isinstance(filtered_data, pd.DataFrame)
    assert len(filtered_data) == 2
    assert all(filtered_data["year"] == 2002)


# Test for stats_utils.calculate_mean function
def test_calculate_mean():
    mean_births = stats_utils.calculate_mean(sample_df, "births")
    expected_mean = sum(sample_data["births"]) / len(sample_data["births"])

    assert mean_births == expected_mean


# Test for stats_utils.calculate_median function
def test_calculate_median():
    median_births = stats_utils.calculate_median(sample_df, "births")
    expected_median = 300  # Sorted births: [100, 200, 300, 400, 500]

    assert median_births == expected_median


# Test for data_utils.filter_data function with both year and month filters
def test_filter_data_year_month():
    filtered_data = data_utils.filter_data(sample_df, year=2002, month=3)

    assert isinstance(filtered_data, pd.DataFrame)
    assert len(filtered_data) == 2
    assert all(filtered_data["year"] == 2002)
    assert all(filtered_data["month"] == 3)


if __name__ == "__main__":
    pytest.main()
