import pandas as pd
import os


def ensure_directory_exist(directory):

    if not os.path.exists(directory):

        os.makedirs(directory)


def save_data(df: pd.DataFrame, filename: str, path: str, file_type: str, allow_index: bool = False) -> None:

    try:
        if not path:

            path = 'output'


        ensure_directory_exist(path)
        
        if file_type == 'csv':

            if '.csv' not in filename:

                filename = filename.replace(' ', '_') + '.csv'
                

            long_file_name = os.path.join(path, filename)

            df.to_csv(path_or_buf=long_file_name, index=allow_index)
            
        elif file_type == 'excel':
            if '.xls' not in filename:

                filename = filename.replace(' ', '_') + '.xlsx'
                

            long_file_name = os.path.join(path, filename)

            df.to_excel(path_or_buf=long_file_name, index=allow_index)
        else:

            raise ValueError('Source must be either csv or excel')

    except Exception as e:
        print(e)        

    return long_file_name
    