import pandas as pd
from notification import send_notification

# do data cleaning
def clean_data(df: pd.DataFrame = None)-> pd.DataFrame:
    # check for missing values
    # check for duplicate values
    # check for invalid values
    # check for out of range values
    # validate data types
    # fill or drop missing values
    if not 1:
        send_notification('Data Cleaning', 'Data is clean!', 'slack')
    else:
        send_notification('Data Cleaning', 'Data is not clean!', 'slack')



clean_data()