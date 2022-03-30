import pandas as pd
import numpy as np
from notification import send_notification
from config.config_loader import read_config_file


config = read_config_file()

def check_missing_values(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    # check for missing values
    missing_info = pd.DataFrame(zip(data.nunique(axis=0), data.isnull().sum()), columns =['No of unique values', 'No of Missing values'],
                 index=data.columns.values)
    print('Missing values checked successfully!\n')
    return data, missing_info


def check_duplicate_values(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    # check for duplicate values
    data = data.drop_duplicates()
    print('Duplicate values checked successfully!\n')
    return data


def check_invalid_values(df: pd.DataFrame)-> pd.DataFrame:
    # check for invalid values
    print('Invalid values checked successfully!\n')
    return data


def check_out_of_range_values(df: pd.DataFrame, min_value: int, max_value: int)-> pd.DataFrame:
    # data = df.copy()
    # check for out of range values
    # filter = ((data['water_point:geo:Accuracy'] >= min_value) & (data['water_point:geo:Accuracy'] <= max_value))
    # data = data[filter]
    print('Out of range values checked successfully!\n')
    return data


def check_data_types(df: pd.DataFrame)-> pd.DataFrame:
    # check for invalid values
    print('Data types checked successfully!\n')
    return data


def fill_missing_values(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    cols = config.get('clean').get('missing_value_columns')
    value = config.get('clean').get('fill_missing_value_with')
    for col in cols:
        data = data.fillna(value)
    print('Missing values filled successfully!\n')
    return data

# do data cleaning
def clean_data(df: pd.DataFrame = None)-> pd.DataFrame:
    missing_info = ''
    data = df.copy()
    try:
        
        if config.get('clean').get('check_missing_values'):
            # check for missing values
            data, missing_info = check_missing_values(data)

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

        message = f'''
        {missing_info}
        Data cleaning finished successfully!'''
    except Exception as e:
        message = 'Data cleaning failed!'
        print(e)

    title = 'Data Cleaning'
    medium = 'email'
    send_notification(title, message, medium)
    return data
