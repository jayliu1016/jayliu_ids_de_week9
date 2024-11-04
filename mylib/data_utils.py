import pandas as pd


def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)


def filter_data(data, year=None, month=None):
    """Filter data based on year or month."""
    if year is not None:
        data = data[data["year"] == year]
    if month is not None:
        data = data[data["month"] == month]
    return data
