import pytest
import pandas as pd
from src.validators import validate_numeric_range, validate_schema, validate_allowed_values, validate_referential_integrity, validate_required_fields, validate_unique_keys, report_duplicate_rows, validate_whole_numbers

incorrect_data = pd.Series([-50, 10, 300, 60])
non_negative_data = pd.Series([10,20,30,40,50, 100, 300])
max_value_data = pd.Series([10,20,30,100]) 

# Numeric Range

def test_numeric_range_rejects_negative_values():
    with pytest.raises(ValueError):
        validate_numeric_range(incorrect_data, 'A', 0, None)

def test_numeric_range_accepts_valid_values():
    validate_numeric_range(non_negative_data, 'B', 0, None)

def test_numeric_range_rejects_values_above_maximum():
    with pytest.raises(ValueError):
        validate_numeric_range(non_negative_data, 'C', 0, 100)

def test_numeric_range_accepts_maximum_value():
    validate_numeric_range(max_value_data, 'D', 0, 100)

# Schema validation test

actual_col = {'A', 'B', 'C', 'D'}
expected_col = {'B', 'C', 'D', 'E'}
def test_schema_rejects_missing_cols():
    with pytest.raises(ValueError):
        validate_schema(expected_col, actual_col)

actual_col2 = {'A', 'B', 'C', 'D', 'E'}
expected_col2 = {'A', 'B', 'C'}
def test_schema_unexpected_cols():
    with pytest.raises(ValueError):
        validate_schema(actual_col2, expected_col2)

actual_col3 = {'A', 'B', 'C'}
expected_col3 = {'A', 'B', 'C'}
def test_schema():
    validate_schema(actual_col3, expected_col3)

# Allowed values

series = pd.Series(['alpha', 'beta', 'gama'])
allowed_values = {'alpha', 'beta'}
def test_allowed_values():
    with pytest.raises(ValueError):
        validate_allowed_values(series, 'ABC', allowed_values)

correct_allowed_values = {'alpha', 'beta', 'gama'}
def test_allowed_values_with_correct_set():
    validate_allowed_values(series, 'ABC', correct_allowed_values)

# Referential Integrity test

child_series = pd.Series(['A', 'B', 'C', 'D'])
incorrect_child_series = pd.Series(['A', 'B', 'C', 'D', 'E'])
parent_series = pd.Series(['A', 'B', 'C', 'D'])
def test_referential_integrity_with_incorrect_data():
    with pytest.raises(ValueError):
        validate_referential_integrity(incorrect_child_series, parent_series)

def test_referential_integrity_with_correct_data():
    validate_referential_integrity(child_series, parent_series)

# Report Duplicate rows 

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
    'Age': [25, 30, 35, 25],
    'City': ['New York', 'London', 'Paris', 'New York']
}

df = pd.DataFrame(data)

def test_duplicate_rows():
    count = report_duplicate_rows(df)
    assert count == 1

info = {
    'id': [10, 20, 30],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

dataframe = pd.DataFrame(info)

def test_duplicate_rows_with_no_duplicate():
    count = report_duplicate_rows(dataframe)
    assert count == 0

# Unique Keys

unique_keys = ['id']
def test_unique_keys():
    validate_unique_keys(dataframe, unique_keys)

infos = {
    'id': [10, 20, 30, 20],
    'Name': ['Alice', 'Bob', 'Charlie', 'Angel'],
    'Age': [25, 30, 35, 30],
    'City': ['New York', 'London', 'Paris', 'UK']
}

dataframe2 = pd.DataFrame(infos)

non_unique_keys = ['id', 'Age']
def test_non_unique_keys():
    with pytest.raises(ValueError):
        validate_unique_keys(dataframe2, non_unique_keys)

# Required columns

req_cols = ['id', 'Name']
def test_required_cols():
    validate_required_fields(dataframe, req_cols)

information = {
    'id': [None, 10, 20],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

dataframe3 = pd.DataFrame(information)

missing_req_cols = ['id', 'Name']
def test_missing_required_cols():
    with pytest.raises(ValueError):
        validate_required_fields(dataframe3, missing_req_cols)

def test_whole_numbers():
    series = pd.Series([10.0, 20.0, 30.0, 40.0])
    validate_whole_numbers(series, "product_count")

def test_whole_numbers_with_fractional_values():
    series = pd.Series([10.5, 20.75, 30.0, 40.0])
    with pytest.raises(ValueError):
        validate_whole_numbers(series, "product_count")

def test_whole_numbers_with_missing_values():
    series = pd.Series([10.0, 20.0, 30.0, None])
    validate_whole_numbers(series, "product_count")