#!/usr/bin/env python
"""Gendiff main script."""
import argparse
import json
from pathlib import Path


def dict_to_str(dictionary):
    """
    Get dictionary to string function.

    Args:
        dictionary: some dict

    Returns:
        str
    """
    return json.dumps(
        dictionary,
        separators=(' ', ': '),
        indent=4,
    ).replace('"', '')


def get_key(key):
    """
    Get key function.

    Args:
        key: tuple

    Returns:
        str
    """
    return key[0]


def get_data(file_path):
    """
    Get data function.

    Args:
        file_path: path to file

    Returns:
        dact
    """
    get_path = Path('gendiff/fixtures', Path(file_path).name).resolve()
    with open(get_path) as data_file1:
        file_data = json.load(data_file1)

    return file_data


def generate_diff(file1, file2):
    """
    Check different function.

    Args:
        file1: path to file one
        file2: path to file two

    Returns:
        str
    """
    file1_data = get_data(file1)
    file2_data = get_data(file2)
    sorted_tuple = sorted((file1_data | file2_data).items(), key=get_key)
    new_data = {}
    for key in dict(sorted_tuple):
        if key in file1_data:
            if key in file2_data:
                if file1_data.get(key) == file2_data.get(key):
                    new_data['  {0}'.format(key)] = file2_data.get(key)
                else:
                    new_data['- {0}'.format(key)] = file1_data.get(key)
                    new_data['+ {0}'.format(key)] = file2_data.get(key)
            else:
                new_data['- {0}'.format(key)] = file1_data.get(key)
        else:
            new_data['+ {0}'.format(key)] = file2_data.get(key)

    return dict_to_str(new_data)


def gendiff():
    """Gendiff function."""
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument(
        '-f',
        '--format',
        metavar='FORMAT',
        help='set format of output',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


def main():
    """Gendiff main function."""
    gendiff()


if __name__ == '__main__':
    main()
