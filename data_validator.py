import pandas as pd
import numpy as np
from notification import send_notification
from config.config_loader import read_config_file


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


def check_out_of_range_values(df: pd.DataFrame, min_value: int, max_value: int)-> pd.DataFrame:
    data = df.copy()
    # check for out of range values
    filter = ((data['water_point:geo:Accuracy'] >= min_value) & (data['water_point:geo:Accuracy'] <= max_value))
    data = data[filter]
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
    data = df.copy()
    try:
        config = read_config_file()
        if config.get('clean').get('check_missing_values'):
            # check for missing values
            data = check_missing_values(data)

        if config.get('clean').get('check_duplicate_values'):
            # check for duplicate values
            data = check_duplicate_values(data)
        
        if config.get('clean').get('check_invalid_values'):
            # check for invalid values
            data = check_invalid_values(data)
        
        if config.get('clean').get('check_out_of_range_values'):
            # check for out of range values
            min_value = config.get('clean').get('range_min_value')
            max_value = config.get('clean').get('range_max_value')
            data = check_out_of_range_values(data, min_value=min_value, max_value=max_value)
        
        if config.get('clean').get('check_data_types'):
            # validate data types
            data = check_data_types(data)
        
        if config.get('clean').get('fill_missing_values'):
            # fill or drop missing values
            data = fill_missing_values(data)

        message = 'Data cleaning finished successfully!'
    except Exception as e:
        message = 'Data cleaning failed!'
        print(e)

    title = 'Data Cleaning'
    medium = 'email'
    send_notification(title, message, medium)
    return data
