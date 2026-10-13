from pathlib import Path
import pandas as pd

root = Path(__file__).parents[1]
raw_data_dir = root / "data" / "raw"

def load_datasets():
    if raw_data_dir.exists():
        csv_files = list(raw_data_dir.glob("*.csv"))

        if csv_files :

            dataframes = {}

            for csv_file in csv_files:
                try:
                    df = pd.read_csv(csv_file)
                    dataframes[csv_file.name] = df
                except (ValueError, OSError, pd.errors.ParserError) as error:
                    raise ValueError(f"Could not read the {csv_file}") from {error}


            return dataframes

        else:
            raise FileNotFoundError(f"No csv file exists")

    else:
        raise FileNotFoundError(f"Raw data directory {raw_data_dir} does not exists.")

if __name__ == "__main__":
    dataframes = load_datasets()
    print(f"Length of dataframe: {len(dataframes)}")
    print(f"Dataframes are: {dataframes.keys()}")

    for name, df in dataframes.items():
        print(f"Shape of {name} is: {df.shape}")
