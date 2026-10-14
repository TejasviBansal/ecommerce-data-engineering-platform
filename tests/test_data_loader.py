import pandas as pd
import src.data_loader as data_loader
import pytest

def test_load_datasets(tmp_path, monkeypatch):
    # create a temporary files
    csv_path = tmp_path / "sample.csv"

    data = {
        "customer_id": ["C001", "C004"],
        "customer_city": ["London", "Paris"]
    }

    df = pd.DataFrame(data)

    # write the data to a csv file
    df.to_csv(csv_path, index = False)

    # direct raw_data_dir to tmp_path
    monkeypatch.setattr(data_loader, "raw_data_dir", tmp_path)

    #Test the function
    dataframes = data_loader.load_datasets()

    # verification
    assert type(dataframes) == dict
    assert 'sample.csv' in dataframes
    assert type(dataframes['sample.csv']) == pd.DataFrame
    assert dataframes['sample.csv'].shape == (2,2)

def test_data_loader_with_no_directory(tmp_path, monkeypatch):
    missing_dir = tmp_path / "missing_data"
    monkeypatch.setattr(data_loader, "raw_data_dir", missing_dir)

    with pytest.raises(FileNotFoundError):
        data_loader.load_datasets()

def test_data_loader_with_no_csvfiles(tmp_path, monkeypatch):

    monkeypatch.setattr(data_loader, "raw_data_dir", tmp_path)

    with pytest.raises(FileNotFoundError):
        data_loader.load_datasets()

def test_load_single_dataset(tmp_path, monkeypatch):
    # create a temporary files
    csv_path = tmp_path / "sample.csv"

    data = {
        "customer_id": ["C001", "C004"],
        "customer_city": ["London", "Paris"]
    }

    df = pd.DataFrame(data)

    # write the data to a csv file
    df.to_csv(csv_path, index = False)

    # direct raw_data_dir to tmp_path
    monkeypatch.setattr(data_loader, "raw_data_dir", tmp_path)

    #Test the function
    dataframe = data_loader.load_datasets("sample.csv")

    # verification
    assert isinstance(dataframe, pd.DataFrame)
    assert dataframe.shape == (2,2)


def test_load_dataset_with_missing_filename(tmp_path, monkeypatch):
    monkeypatch.setattr(data_loader, "raw_data_dir", tmp_path)

    with pytest.raises(FileNotFoundError):
        data_loader.load_datasets("missing_file.csv")