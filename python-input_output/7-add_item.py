#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys

if _name_ == "_main_":
    load_from_json_file = \
        _import_('6-load_from_json_file').load_from_json_file
    save_to_json_file = _import_('5-save_to_json_file').save_to_json_file

    try:
        tab = load_from_json_file("add_item.json")
    except FileNotFoundError:
        tab = []
    tab.extend(sys.argv[1:])
    save_to_json_file(tab, "add_item.json")
