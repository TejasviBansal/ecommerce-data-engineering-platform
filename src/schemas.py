CUSTOMERS_COLUMNS={
    "customer_id",
    "customer_unique_id",
    "customer_zip_code_prefix",
    "customer_city",
    "customer_state"
}

GEOLOCATION_COLUMNS={
    "geolocation_zip_code_prefix",
    "geolocation_lat",
    "geolocation_lng",
    "geolocation_city",
    "geolocation_state"
}

ORDERS_COLUMNS={
    "order_id",
    "customer_id",
    "order_status",
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
}

ORDER_ITEMS_COLUMNS={
    "order_id",
    "order_item_id",
    "product_id",
    "seller_id",
    "shipping_limit_date",
    "price",
    "freight_value"
}

ORDER_PAYMENTS_COLUMNS={
    "order_id",
    "payment_sequential",
    "payment_type",
    "payment_installments",
    "payment_value"
}

ORDER_REVIEWS_COLUMNS={
    "review_id",
    "order_id",
    "review_score",
    "review_comment_title",
    "review_comment_message",
    "review_creation_date",
    "review_answer_timestamp"
}

PRODUCTS_COLUMNS={
    "product_id",
    "product_category_name",
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
}

SELLERS_COLUMNS={
    "seller_id",
    "seller_zip_code_prefix",
    "seller_city",
    "seller_state"
}

PRODUCT_CATEGORY_NAME_TRANSLATION_COLUMNS={
    "product_category_name",
    "product_category_name_english"
}

EXPECTED_SCHEMAS = {
    "olist_customers_dataset.csv": CUSTOMERS_COLUMNS,
    "olist_geolocation_dataset.csv": GEOLOCATION_COLUMNS,
    "olist_orders_dataset.csv": ORDERS_COLUMNS,
    "olist_order_items_dataset.csv": ORDER_ITEMS_COLUMNS,
    "olist_order_payments_dataset.csv": ORDER_PAYMENTS_COLUMNS,
    "olist_order_reviews_dataset.csv": ORDER_REVIEWS_COLUMNS,
    "olist_products_dataset.csv": PRODUCTS_COLUMNS,
    "olist_sellers_dataset.csv": SELLERS_COLUMNS,
    "product_category_name_translation.csv": PRODUCT_CATEGORY_NAME_TRANSLATION_COLUMNS
}

CUSTOMERS_REQUIRED_COLUMNS = {
    "customer_id",
    "customer_unique_id",
    "customer_zip_code_prefix",
    "customer_city",
    "customer_state"
}

GEOLOCATION_REQUIRED_COLUMNS = {
    "geolocation_zip_code_prefix",
    "geolocation_lat",
    "geolocation_lng",
    "geolocation_city",
    "geolocation_state"
}

ORDERS_REQUIRED_COLUMNS = {
    "order_id",
    "customer_id",
    "order_status",
    "order_purchase_timestamp",
    "order_estimated_delivery_date"    
}

ORDER_ITEMS_REQUIRED_COLUMNS = {
    "order_id",
    "order_item_id",
    "product_id",
    "seller_id",
    "shipping_limit_date",
    "price",
    "freight_value"
}

ORDER_PAYMENTS_REQUIRED_COLUMNS = {
    "order_id",
    "payment_sequential",
    "payment_type",
    "payment_installments",
    "payment_value"
}

ORDER_REVIEWS_REQUIRED_COLUMNS = {
    "review_id",
    "order_id",
    "review_score",
    "review_creation_date",
    "review_answer_timestamp"
}

PRODUCTS_REQUIRED_COLUMNS = {
    "product_id"
}

SELLERS_REQUIRED_COLUMNS = {
    "seller_id",
    "seller_zip_code_prefix",
    "seller_city",
    "seller_state"
}

PRODUCT_CATEGORY_NAME_TRANSLATION_REQUIRED_COLUMNS = {
    "product_category_name",
    "product_category_name_english"
}

REQUIRED_COLUMNS = {
    "olist_customers_dataset.csv": CUSTOMERS_REQUIRED_COLUMNS,
    "olist_geolocation_dataset.csv": GEOLOCATION_REQUIRED_COLUMNS,
    "olist_orders_dataset.csv": ORDERS_REQUIRED_COLUMNS,
    "olist_order_items_dataset.csv": ORDER_ITEMS_REQUIRED_COLUMNS,
    "olist_order_payments_dataset.csv": ORDER_PAYMENTS_REQUIRED_COLUMNS,
    "olist_order_reviews_dataset.csv": ORDER_REVIEWS_REQUIRED_COLUMNS,
    "olist_products_dataset.csv": PRODUCTS_REQUIRED_COLUMNS,
    "olist_sellers_dataset.csv": SELLERS_REQUIRED_COLUMNS,
    "product_category_name_translation.csv": PRODUCT_CATEGORY_NAME_TRANSLATION_REQUIRED_COLUMNS
}

CUSTOMERS_UNIQUE_KEYS = ["customer_id"]

ORDERS_UNIQUE_KEYS = ["order_id"]

ORDER_ITEMS_UNIQUE_KEYS = [
    "order_id",
    "order_item_id"
]

ORDER_PAYMENTS_UNIQUE_KEYS = [
    "order_id",
    "payment_sequential"
]

PRODUCTS_UNIQUE_KEYS = ["product_id"]

SELLERS_UNIQUE_KEYS = ["seller_id"]

PRODUCT_CATEGORY_NAME_TRANSLATION_UNIQUE_KEYS = [
    "product_category_name"
]

UNIQUE_KEYS = {
    "olist_customers_dataset.csv": CUSTOMERS_UNIQUE_KEYS,
    "olist_orders_dataset.csv": ORDERS_UNIQUE_KEYS,
    "olist_order_items_dataset.csv": ORDER_ITEMS_UNIQUE_KEYS,
    "olist_order_payments_dataset.csv": ORDER_PAYMENTS_UNIQUE_KEYS,
    "olist_products_dataset.csv": PRODUCTS_UNIQUE_KEYS,
    "olist_sellers_dataset.csv": SELLERS_UNIQUE_KEYS,
    "product_category_name_translation.csv": PRODUCT_CATEGORY_NAME_TRANSLATION_UNIQUE_KEYS
}

ALLOWED_VALUES ={
    "olist_orders_dataset.csv":{
        'order_status':{
            'delivered',
            'invoiced',
            'shipped',
            'processing',
            'unavailable',
            'canceled',
            'created',
            'approved'
        }
    },
    "olist_order_payments_dataset.csv":{
        'payment_type':{
            'credit_card',
            'boleto',
            'voucher',
            'debit_card',
            'not_defined'
        }
    }
}

NUMERIC_RANGE = {
    "olist_order_items_dataset.csv":{
        'price':{
            'minimum' : 0,
            'maximum' : None
        },
        'freight_value':{
            'minimum' : 0,
            'maximum' : None 
        }
    },
    "olist_order_reviews_dataset.csv":{
        'review_score' : {
            'minimum' : 1,
            'maximum' : 5
        }
    },
    "olist_order_payments_dataset.csv":{
        'payment_value' : {
            'minimum' : 0,
            'maximum' : None
        }
    }
}

REFERENTIAL_INTEGRITY = {
    "olist_orders_dataset.csv": {
        "child_column": "customer_id",
        "parent_dataset": "olist_customers_dataset.csv",
        "parent_column": "customer_id"
    },
    "olist_order_items_dataset.csv" : {
        "child_column": "order_id",
        "parent_dataset": "olist_orders_dataset.csv",
        "parent_column": "order_id"
    }
}

PRODUCTS_WHOLE_NUMBER_COLUMNS=[
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
]

WHOLE_NUMBER = {
    "olist_products_dataset.csv": PRODUCTS_WHOLE_NUMBER_COLUMNS
}