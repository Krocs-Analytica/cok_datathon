import pandas as pd
from get_data import get_data
from save_data import save_data
from notification import send_notification


def change_format(df: pd.DataFrame)-> pd.DataFrame:
    # convert data to a new format
    print('Data format changed successfully!\n')
    return df


def apply_function_to_column(df: pd.DataFrame)-> pd.DataFrame:
    # apply a function to each column
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
    # TODO: read data transformation configurations from a file e.g yaml file
    data = df.copy()
    try:
        # convert data to a new format
        data = change_format(data)
        # apply a function to each column
        data = apply_function_to_column(data)
        # apply a function to each row
        data = apply_function_to_row(data)
        # aggregate data
        data = aggregate_data(data)
        # group data
        data = group_data(data)
        # sort data
        data = sort_data(data)
        # filter data
        data = filter_data(data)

        message = "Data transformations finished successfully!"
    except Exception as e:
        message = "Data transformations failed!"
        print(e)

    title = 'Data Transformation'
    medium = "slack"
    send_notification(title, message, medium)
    return data