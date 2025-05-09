from typing import Union, Dict, List, Any
import pandas as pd
from pathlib import Path

from pytextable.utils.parse_csv import parse_csv
from pytextable.utils.parse_dict import parse_dict
from pytextable.utils.parse_dataframe import parse_dataframe


def generate(data: Union[str, Dict[str, List[Any]], pd.DataFrame], caption: str = "", label: str = "", **kwargs) -> str: 
    """
    Generates a LaTeX table from the given data.

    Returns:
        str: A string containing the LaTeX code for the generated table.
    
    :param data: A 2D dictionary. 
    :param caption: The caption for the table.
    :param label: The label for the table.
    :param kwargs: Additional arguments for table generation.
    """
    table = ""

    # Check if the data is a CSV file using Path
    if isinstance(data, str) and Path(data).suffix == ".csv":
        data = parse_csv(data)
    # Check if the data is a dictionary
    elif isinstance(data, dict):
        data = parse_dict(data)
    # Check if the data is a DataFrame
    elif isinstance(data, pd.DataFrame):
        data = parse_dataframe(data)

    return ""
