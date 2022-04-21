#!/usr/bin/env python
"""Gendiff main script."""
import argparse


def gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument(
        '-f',
        '--format',
        metavar='FORMAT',
        help='set format of output')
    parser.add_argument('first_file', type=open)
    parser.add_argument('second_file', type=open)

    parser.parse_args()


def main():
    """Gendiff main function."""
    gendiff()


if __name__ == '__main__':
    main()
