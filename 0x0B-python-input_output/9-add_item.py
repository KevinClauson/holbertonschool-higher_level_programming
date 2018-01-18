#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def add_args_list():
    """adds ags to a list and saves in file"""
    file = './add_item.json'
    try:
        new_l = load_from_json_file(file)
    except:
        new_l = []
    for i in range(1, len(argv)):
        new_l.append(argv[i])
    save_to_json_file(new_l, file)


if __name__ == '__main__':
    add_args_list()
