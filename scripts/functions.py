import os
import pandas as pd
import numpy as np
import matplotlib.pylab as pl


def read_csv_files(directory_path) -> pd.DataFrame:
    """
    Function to read csv files and create DataFrame

    Args:
        directory_path (str): The path to the folder containing csv files.
    Returns:
        pandas.DataFrame: A DataFrame that contains all the data from the csv files,
                          with an extra column 'bron_datum'.
    """
    dataframes = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            full_path = os.path.join(directory_path, filename)
            df = pd.read_csv(full_path)
            df['bron_datum'] = filename[:-4]
            dataframes.append(df)
    
    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    return combined_df


def to_percentage(number):
    return str(np.round(number * 100, 2)) + "%"

def compute_num_unique(df, n_births):
    return len(np.unique(df['naam'].sample(n_births)))

def plot_geboortedagen_per_jaar(bron, horizontale_lijn):
    pl.figure(figsize=(20, 5))
    bron.plot(kind="line", color="blue", title="Aantal geboortes per dag van het jaar", label='Aantal geboortes')
    pl.axhline(horizontale_lijn, color='red', linestyle='dashed', linewidth=1, label='gemiddelde')
    pl.xlabel("Dag van het jaar")
    pl.ylabel("Aantal geboortes")
    pl.grid(axis="y")
    pl.legend()
    pl.show()

def plot_runnnig_average(df, horizontale_lijn):
    pl.figure(figsize=(20, 5))
    pl.plot(df['bron_datum'], df['running_average'], color="blue", label='Aantal geboortes')
    pl.axhline(horizontale_lijn, color='red', linestyle='dashed', linewidth=1, label='gemiddelde')
    pl.xlabel("Dag van het jaar")
    pl.ylabel("Aantal geboortes")
    pl.grid(axis="y")
    pl.legend()
    pl.show()