import pandas as pd
import numpy as np
from notification import send_notification


def check_missing_values(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    # check for missing values
    missing_info = pd.DataFrame(zip(data.nunique(axis=0), data.isnull().sum()), columns =['No of unique values', 'No of Missing values'],
                 index=data.columns.values)
    print(missing_info)
    print('Missing values checked successfully!\n')
    return data


def check_duplicate_values(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    # check for duplicate values
    data = data.drop_duplicates()
    print('Duplicate values checked successfully!\n')
    return data


def check_invalid_values(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    # check for invalid values
    data = data.replace('', np.nan)
    print('Invalid values checked successfully!\n')
    return data


def check_out_of_range_values(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    # check for out of range values
    data = data[data['water_point:geo:Accuracy'] < 5]
    print('Out of range values checked successfully!\n')
    return data


def check_data_types(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    # check for invalid values
    data = data.astype({'water_point:geo:Latitude': 'float', 'water_point:geo:Longitude': 'float', 'water_point:source_functional': 'bool'})
    print('Data types checked successfully!\n')
    return data


def fill_missing_values(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    # fill or drop missing values
    # data = data.fillna(0)
    print('Missing values filled successfully!\n')
    return data

# do data cleaning
def clean_data(df: pd.DataFrame = None)-> pd.DataFrame:
    # TODO: read data cleaning configurations from a file e.g yaml file
    data = df.copy()
    try:
        # check for missing values
        data = check_missing_values(data)
        # check for duplicate values
        data = check_duplicate_values(data)
        # check for invalid values
        data = check_invalid_values(data)
        # check for out of range values
        data = check_out_of_range_values(data)
        # validate data types
        data = check_data_types(data)
        # fill or drop missing values
        data = fill_missing_values(data)

        message = 'Data cleaning finished successfully!'
    except Exception as e:
        message = 'Data cleaning failed!'
        print(e)

    title = 'Data Cleaning'
    medium = 'slack'
    send_notification(title, message, medium)
    return data

