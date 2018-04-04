#!/usr/bin/python3
"""finds peak"""

def find_peak(list_of_integers):
    """
    finds peak
    """
    if not list_of_integers or len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    for i in range(len(list_of_integers)):
        if i == 0 and list_of_integers[i] >= list_of_integers[i+1]:
            return list_of_integers[i]
        elif i == len(list_of_integers) - 1 and list_of_integers[i] > list_of_integers[i-1]:
            return list_of_integers[i]
        elif i != 0 and i != len(list_of_integers) - 1 and list_of_integers[i] > list_of_integers[i-1] and list_of_integers[i] > list_of_integers[i+1]:
            return list_of_integers[i]
    return None
