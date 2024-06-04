import pandas as pd
import os
import json


def read_csv_files(directory_path):
    """
    Function to read JSON files and create DataFrame

    Args:
        directory_path (str): The path to the folder containing csv files.
    Returns:
        pandas.DataFrame: A DataFrame that contains all the data from the csv files,
                          with an extra column 'bron_datum'.
    """
    dataframes = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            full_path = os.path.join(directory_path, filename)
            with open(full_path, 'r') as f:
                json_data = json.load(f)
                df = pd.DataFrame([json_data])
                df['bron_datum'] = filename
                dataframes.append(df)
    return pd.DataFrame(dataframes, ignore_index=True)
