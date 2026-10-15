def validate_schema(expected_cols, actual_cols):
    missing_cols = expected_cols - actual_cols

    if missing_cols:
        raise ValueError(f"Missing columns found {missing_cols}")

    unexpected_cols = actual_cols - expected_cols

    if unexpected_cols:
        raise ValueError(f"Unexpected columns found {unexpected_cols}")

def validate_required_fields(df, required_cols):
    missing_mask = df.isna().sum()
    req_missing_mask = missing_mask[list(required_cols)] > 0
    required_missing_cols = set(req_missing_mask[req_missing_mask].index)

    if required_missing_cols:
        raise ValueError(f"Required missing columns {required_missing_cols}")

def validate_unique_keys(df, unique_keys):
    duplicate_count = df.duplicated(subset=unique_keys).sum()

    if duplicate_count:
        raise ValueError(f"Duplicate keys found for {unique_keys}: {duplicate_count}")

def report_duplicate_rows(df):
    duplicate_count = df.duplicated().sum()
    return duplicate_count

def validate_allowed_values(series, column, allowed_values):
    series_values = set(series.unique())
    invalid_values = series_values - allowed_values

    if invalid_values:
        raise ValueError(f"Invalid values found for {column}: {invalid_values}")

def validate_numeric_range(series, column, minimum, maximum):
    min_value = series.min()
    max_value = series.max()

    if (minimum is not None and min_value < minimum) or (maximum is not None and max_value > maximum):
        raise ValueError(f"Invalid numeric range for {column}: \n Allowed minimum value: {minimum} \n Allowed maximum value: {maximum} \n Observed minimum value: {min_value} \n Observed maximum value: {max_value} ")

def validate_referential_integrity(child_series, parent_series):
    child_ids = set(child_series.unique())
    parent_ids = set(parent_series.unique())

    invalid_child_ids = child_ids - parent_ids

    if invalid_child_ids:
        raise ValueError(f"Invalid foreign key reference found: {invalid_child_ids}")

def validate_whole_numbers(series, column):
    no_null_value = series.dropna()
    fractional_values = (no_null_value % 1) != 0

    if any(fractional_values):
        raise ValueError(f"Fractional values present in {column}: {no_null_value[fractional_values]}") 