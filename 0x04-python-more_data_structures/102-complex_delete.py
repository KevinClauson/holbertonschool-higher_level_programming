#!/usr/bin/python3
def complex_delete(my_dict, value):
    my = {k:v for k,v in my_dict.items() if v == value}
    for key in my:
        del my_dict[key]
    return my_dict
