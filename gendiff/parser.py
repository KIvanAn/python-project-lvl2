"""Parser files module."""
import json
from pathlib import Path

import yaml


def parser(file_path):
    """
    Get data function.

    Args:
        file_path: path to file

    Returns:
        dact
    """
    get_path = Path('gendiff/fixtures', Path(file_path).name).resolve()
    with open(get_path) as data_file1:
        if get_path.suffix == '.json':
            file_data = json.load(data_file1)
        elif get_path.suffix in {'.yaml', '.yml'}:
            file_data = yaml.safe_load(data_file1)

    return file_data
