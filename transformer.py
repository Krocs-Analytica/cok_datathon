import pandas as pd
from get_data import get_data
from save_data import save_data
from notification import send_notification
from config.config_loader import read_config_file


config = read_config_file()

def change_format(df: pd.DataFrame)-> pd.DataFrame:
    # convert data to a new format
    cols_to_change = config.get('transform').get('change_column_to_datetime')
    if len(cols_to_change) > 0:
        for col in cols_to_change:
            df[col] = pd.to_datetime(df[col])
        print('Data format changed successfully!\n')
    return df


def apply_function_to_column(df: pd.DataFrame)-> pd.DataFrame:
    # apply a function to each column
    if config.get('transform').get('map_yes_no_to_1_0'):
        cols = config.get('transform').get('columns_to_map')
        for col in cols:
            df[col] = df[col].map({'Yes': 1, 'No': 0, 'yes': 1, 'no': 0})
        print('Applying function to each column finished successfully!\n')
    return df


def apply_function_to_row(df: pd.DataFrame)-> pd.DataFrame:
    # apply a function to each row
    print('Applying function to each row finished successfully!\n')
    return df


def aggregate_data(df: pd.DataFrame)-> pd.DataFrame:
    # aggregate data
    print('Aggregating data finished successfully!\n')
    return df


def group_data(df: pd.DataFrame)-> pd.DataFrame:
    # group data
    print('Grouping data finished successfully!\n')
    return df


def sort_data(df: pd.DataFrame)-> pd.DataFrame:
    # sort data
    print('Sorting data finished successfully!\n')
    return df


def filter_data(df: pd.DataFrame)-> pd.DataFrame:
    # filter data
    print('Filtering data finished successfully!\n')
    return df


def transform_data(df: pd.DataFrame)-> pd.DataFrame:
    data = df.copy()
    try:
        # convert data to a new format
        if config.get('transform').get('change_column_to_datetime'):
            data = change_format(data)
        # apply a function to each column
        if config.get('transform').get('apply_function_to_column'):
            data = apply_function_to_column(data)
        # apply a function to each row
        if config.get('transform').get('apply_function_to_row'):
            data = apply_function_to_row(data)
        # aggregate data
        if config.get('transform').get('aggregate_data'):
            data = aggregate_data(data)
        # group data
        if config.get('transform').get('group_data'):
            data = group_data(data)
        # sort data
        if config.get('transform').get('sort_data'):
            data = sort_data(data)
        # filter data
        if config.get('transform').get('filter_data'):
            data = filter_data(data)

        message = "Data transformations finished successfully!"
    except Exception as e:
        message = f"Data transformations failed!\n{e}"

    print(message)
    return data
