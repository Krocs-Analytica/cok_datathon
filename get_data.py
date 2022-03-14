
import pandas as pd

from pathlib import Path

 

def get_data(source: str, path: str) -> pd.DataFrame:

    """Get data from a file.

    Args:

        source (str): _description_

        path (str): _description_

    Raises:

        ValueError: _description_

    Returns:

        pd.DataFrame: _description_

    """

    path_to_file = 'readme.csv'

    path = Path(path_to_file)

 

    if path.is_file():

        print(f'The file {path_to_file} exists')

    else:

        print(f'The file {path_to_file} does not exist')

 

 

try:

    if source == 'csv':

        return pd.read_csv(path)

    elif source == 'excel':

        return pd.read_excel(path)

    elif source == 'json':

        return pd.read_json(path)

    elif source == 'pickle':

        return pd.read_pickle(path)

    elif source == 'sql':

        return pd.read_sql(path)

    elif source == 'html':

        return pd.read_html(path)

    else:

        raise ValueError('Source not supported.')

except Exception as e:

print(e)