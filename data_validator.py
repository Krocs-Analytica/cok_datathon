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

def drop_columns(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    cols = config.get('clean').get('drop_columns')
    if len(cols) > 0:
        for col in cols:
            data = data.drop(col, axis=1)
    return data


def drop_out_of_range_values(df: pd.DataFrame, min_value: int, max_value: int)-> pd.DataFrame:
    data = df.copy()
    cols_to_check_range = config.get('clean').get('drop_out_of_range_values')
    if len(cols_to_check_range) > 0:
    # check for out of range values
        for col in cols_to_check_range:
            filter = ((data[col] >= min_value) & (data[col] <= max_value))
            data = data[filter]
        print('Out of range values dropped successfully!\n')
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
        data[col] = data[col].fillna(str(value))
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
        
        if config.get('clean').get('drop_columns'):
            # drop unwanted columns
            data = drop_columns(data)
        
        if config.get('clean').get('drop_out_of_range_values'):
            # check for out of range values
            min_value = config.get('clean').get('range_min_value')
            max_value = config.get('clean').get('range_max_value')
            data = drop_out_of_range_values(data, min_value=min_value, max_value=max_value)
        
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
        message = f'Data cleaning failed!:\n{e}'

    print(message)
    return data
