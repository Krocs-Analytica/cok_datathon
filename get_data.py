
import pandas as pd
import os
import pathlib
 

def get_data( path: str, source: str) -> pd.DataFrame:

    """Get data from a file.

    Args:

        source (str): _description_

        path (str): _description_

    Raises:

        ValueError: _description_

    Returns:

        pd.DataFrame: _description_

    """
    if not pathlib.Path(path).exists():
        raise ValueError('File does not exist')

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
        