from pathlib import Path
import pandas as pd
from .data_loader import load_datasets

root = Path(__file__).parents[1]
processed_order_dir = root / "data" / "processed" / "olist_orders_dataset.csv"

def convert_str_to_datetime(df, datetime_list):
    processed_df = df.copy()
    for item in datetime_list:
        processed_df[item] = pd.to_datetime(processed_df[item])
    return processed_df


def process_orders():
    df = load_datasets("olist_orders_dataset.csv")
    datetime_list = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']

    processed_df = convert_str_to_datetime(df, datetime_list)
    # print(f"Datatypes of original dataframe columns are: \n {df.dtypes}")
    # print(f"Datatypes of processed dataframe columns are: \n {processed_df.dtypes}")
    # print(f"Missing values in original dataframe: \n {df.isna().sum()}")
    # print(f"Missing values in processed dataframe: \n {processed_df.isna().sum()}")

    processed_order_dir.parent.mkdir(parents=True, exist_ok=True)
    processed_df.to_csv(processed_order_dir, index=False)  

    return processed_df

def main():
    orders_df = process_orders()

if __name__ == "__main__":
    main()