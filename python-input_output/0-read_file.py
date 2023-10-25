#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, mode='r', encoding="utf-8") as file:
        for line in file:
            print(line, end='')
