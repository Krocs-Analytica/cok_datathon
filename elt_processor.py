import pandas as pd


from get_data import get_data
from save_data import save_data
from notification import send_notification
from transformer import transform_data
from data_validator import clean_data



pd.set_option(

        'display.max_columns', None,

        'display.max_colwidth', None,

        'display.expand_frame_repr', False

    )

source_file = 'cok_datathon\input\water_point1_results.csv'


data = get_data(path=source_file, source='csv')


file_path = save_data(data, filename='water_point1_results_downloaded', path='lakehouse', file_type='csv', allow_index=False)


data = get_data(path=file_path, source='csv')


data = clean_data(data)


cleaned_data = save_data(data, filename='water_point1_results_cleaned', path='lakehouse', file_type='csv', allow_index=False)


data = get_data(path=cleaned_data, source='csv')


data = transform_data(data)


transformed_data = save_data(data, filename='water_point1_results_transformed', path='lakehouse', file_type='csv', allow_index=False)

transformed_data_location = transformed_data.replace('\\', '/')
title = 'ELT Job Status: '

message = f'''

    The ETL job has finished successfully.<br/>

    The transformed data is available at http://fakeurl.com/{transformed_data_location}<br/>

    '''
medium = 'email'

send_notification(title, message, medium)
