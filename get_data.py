import pandas as pd

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
