from src.transform_data import convert_str_to_datetime, nullable_integer_conversion
import pandas as pd
from pandas.testing import assert_frame_equal

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

def test_nullable_integer_conversion():
    data = {
        "col1":[10.0, 20.0, 30.0, 0.0],
        "col2":[15.0, 35.0, 14, None]
    }
    df = pd.DataFrame(data)
    df_copy = df.copy()
    count_cols_list = ['col1', 'col2']

    processed_df = nullable_integer_conversion(df, count_cols_list)

    assert all(str(processed_df[col].dtype) == "Int64" for col in count_cols_list)
    assert pd.isna(processed_df['col2'].iloc[3])
    assert_frame_equal(df_copy, df)
