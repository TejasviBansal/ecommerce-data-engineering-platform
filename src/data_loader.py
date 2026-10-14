from pathlib import Path
import pandas as pd

root = Path(__file__).parents[1]
raw_data_dir = root / "data" / "raw"

def load_datasets(filename = None):
    if raw_data_dir.exists():
        csv_files = list(raw_data_dir.glob("*.csv"))

        if csv_files :

            if filename is not None:
                if (raw_data_dir/filename) in csv_files:
                    try:
                        df = pd.read_csv(raw_data_dir / filename)
                    except (ValueError, OSError, pd.errors.ParserError) as error:
                        raise ValueError(f"Could not read the {filename}") from {error}
                    return df
                else:
                    raise FileNotFoundError(f"The file {filename} does not exist.")

            else:
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
    result = load_datasets()
    if isinstance(result, dict):
        print(f"Length of dataframe: {len(result)}")
        print(f"Dataframes are: {result.keys()}")

        for name, df in result.items():
            print(f"Shape of {name} is: {df.shape}")

    else:
        print(f"Shape of dataframe is {result.shape}")
