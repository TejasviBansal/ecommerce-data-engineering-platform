from pathlib import Path
import pandas as pd
import json

# Path of the root
root = Path(__file__).parents[1]

# Path of the raw data
raw_data_dir = root / "data" / "raw"

#Extracting csv files
csv_files = list(raw_data_dir.glob("*.csv"))

#Path of the report
profile_report_path = root / "reports"/ "data_profile.json"

profiles = []
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    rows, columns = df.shape
    profile = {}
    profile["file_name"]=csv_file.name
    profile["rows"]=rows
    profile["columns"]=columns
    profile['column_names']=list(df.columns)
    profile['data_types']={column: str(dtype) for column, dtype in df.dtypes.items()}
    profile['missing_values_count']={column: int(val) for column, val in df.isna().sum().items()}
    profile['duplicate_rows_count']=int(df.duplicated().sum())
    profile['unique_value_counts']={column: int(val) for column, val in df.nunique().items()}

    numeric_df = df.select_dtypes(include="number")
    profile['numeric_statistics'] = {} if numeric_df.shape[1] == 0 else {
        column: {
            key: int(value) if key == 'count' else float(value)
            for key, value in stats.items()
        }
        for column, stats in numeric_df.describe().to_dict(orient='dict').items()
    }

    profiles.append(profile)


with open(profile_report_path, "w") as file:
    json.dump(profiles, file, indent=4)