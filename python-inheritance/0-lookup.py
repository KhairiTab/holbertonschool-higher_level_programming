#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of attributes and methods of the given object.
    """
    if obj is None:
        return []
    return [attribute for attribute in dir(obj)]
