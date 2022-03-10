from wsgiref.handlers import format_date_time
import pandas as pd
from get_data import get_data
from save_data import save_data

def transform_data(df: pd.DataFrame)-> pd.DataFrame:
    # convert data to a new format
    # apply a function to each column
    # apply a function to each row
    # aggregate data
    # group data
    # sort data
    # filter data
    pass
def remove_special_characters(text):
    """ Remove special characters from a string.
    Args:
        text (str): Source text to remove special characters.
    Raises:
        Exception: Any other error message
    Returns:
        [str]: Text with special characters removed.
    """
    txt = ""
    try:
        txt = text.translate({ord(c): "_" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        txt = txt.replace(' ', '_')
    except Exception as e:
        print('remove_special_characters: ' + repr(e))
    return txt
