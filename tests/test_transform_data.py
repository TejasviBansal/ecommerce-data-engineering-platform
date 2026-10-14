from src.transform_data import convert_str_to_datetime
import pandas as pd

def test_datetime_conversion():
    
    data = {
        "current_date": ["2026-10-14 21:57:05", ""]
    }

    df = pd.DataFrame(data)

    converted_df = convert_str_to_datetime(df, ['current_date'])
    assert pd.api.types.is_datetime64_any_dtype(converted_df["current_date"])

def test_original_dataframe_remains_unchanged():
    data = {
            "current_date": ["2026-10-14 21:57:05", ""]
        }
    
    df = pd.DataFrame(data)

    converted_df = convert_str_to_datetime(df, ['current_date'])
    assert pd.api.types.is_string_dtype(df["current_date"])
    assert pd.api.types.is_datetime64_any_dtype(converted_df['current_date'])

def test_missing_timestamps_remain_missing():
    data = {
            "current_date": ["2026-10-14 21:57:05", ""]
        }
    
    df = pd.DataFrame(data)

    converted_df = convert_str_to_datetime(df, ['current_date'])

    assert pd.isna(converted_df['current_date'].iloc[1])