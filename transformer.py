import pandas as pd
from get_data import get_data
from save_data import save_data
from notification import send_notification


def change_format(df: pd.DataFrame)-> pd.DataFrame:
    # convert data to a new format
    df['start'] = pd.to_datetime(df['start'])
    df['end'] = pd.to_datetime(df['end'])
    df['today'] = pd.to_datetime(df['today'])
    df = df.astype({'water_point:geo:Latitude': float,'water_point:geo:Longitude':float,
    'water_point:geo:Altitude': float, 'water_point:geo:Accuracy': float, 'water_point:photo': str, 
    'water_point:supervisor_name': str, 'water_point:enumerator_name': str, 'water_point:lga':str, 'water_point:ward':str,
    'water_point:community': str, 'water_point:respondent':str, 'water_point:respondent_position': str,
    'water_point:nearest_locality': str, 'water_point:nearest_school_or_locality': str, 'water_point:water_source_type': str,
    'water_point:distribution_type': str, 'water_point:lift_mechanism': str, 'water_point:source_developed_by': str,
    'water_point:Source_Managed_by': str, 'water_point:Source_managed_identity': str, 'water_point:source_functional': str,
    'water_point:water_source_used': str, 'water_point:reasons_not_used': str, 'water_point:water_source_physical_state': str,
    'water_point:quality_water': str, 'water_point:close_water_source': str, 'meta:instanceID': str})
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
    df.groupby('water_point:water_source_type')
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
