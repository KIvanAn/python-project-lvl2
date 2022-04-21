#!/usr/bin/env python
"""Gendiff main script."""
import argparse


def gendiff():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=open)
    parser.add_argument('second_file', type=open)

    parser.parse_args()


def main():
    """Gendiff main function."""
    gendiff()


if __name__ == '__main__':
    main()
