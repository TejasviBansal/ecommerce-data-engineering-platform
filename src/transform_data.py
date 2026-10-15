from pathlib import Path
import pandas as pd
from .data_loader import load_datasets

root = Path(__file__).parents[1]
processed_order_path = root / "data" / "processed" / "olist_orders_dataset.csv"
processed_order_items_path = root / "data" / "processed" / "olist_order_items_dataset.csv"
processed_products_path = root / "data" / "processed" / "olist_products_dataset.csv"

def convert_str_to_datetime(df, datetime_list):
    processed_df = df.copy()
    for item in datetime_list:
        processed_df[item] = pd.to_datetime(processed_df[item])
    return processed_df

def nullable_integer_conversion(df, count_cols_list):
    processed_df = df.copy()
    for col in count_cols_list:
        processed_df[col] = processed_df[col].astype("Int64")

    return processed_df

def process_orders():
    df = load_datasets("olist_orders_dataset.csv")
    datetime_list = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']

    processed_df = convert_str_to_datetime(df, datetime_list)
    # print(f"Datatypes of original dataframe columns are: \n {df.dtypes}")
    # print(f"Datatypes of processed dataframe columns are: \n {processed_df.dtypes}")
    # print(f"Missing values in original dataframe: \n {df.isna().sum()}")
    # print(f"Missing values in processed dataframe: \n {processed_df.isna().sum()}")

    processed_order_path.parent.mkdir(parents=True, exist_ok=True)
    processed_df.to_csv(processed_order_path, index=False)  

    return processed_df

def process_order_items():
    df = load_datasets("olist_order_items_dataset.csv")
    datetime_list = ["shipping_limit_date"]
    processed_df = convert_str_to_datetime(df, datetime_list)
    # print(f"Datatype of processed dataframe columns are: \n {processed_df.dtypes}")
    # print(f"Missing value in processed dataframe: \n {processed_df.isna().sum()}")

    processed_order_items_path.parent.mkdir(parents=True, exist_ok=True)
    processed_df.to_csv(processed_order_items_path, index=False)

    return processed_df

def process_products():
    df = load_datasets("olist_products_dataset.csv")
    count_cols_list = ['product_name_lenght', 'product_description_lenght', 'product_photos_qty']
    processed_df = nullable_integer_conversion(df, count_cols_list)
    # print(f"Shape of processed dataframe: \n {processed_df.shape}")
    # print(f"Datatypes of processed dataframe: \n {processed_df.dtypes}")
    # print(f"Missing value count: {processed_df.isna().sum()}")

    processed_products_path.parent.mkdir(parents=True, exist_ok=True)
    processed_df.to_csv(processed_products_path, index=False)

    return processed_df

def main():
    orders_df = process_orders()
    order_items_df = process_order_items()
    products_df = process_products()

if __name__ == "__main__":
    main()