#!/usr/bin/python3
"""finds peak"""

def find_peak(nums):
    """
    finds peak
    """
    size = len(nums)
    if not nums or size == 0:
        return None
    elif num == 1:
        return nums[0]
    elif num == 2:
        return max(nums[0], nums[1])
    for i in range(len(list_of_integers)):
        if i == 0 and list_of_integers[i] >= list_of_integers[i+1]:
            return list_of_integers[i]
        elif i == len(list_of_integers) - 1 and list_of_integers[i] > list_of_integers[i-1]:
            return list_of_integers[i]
        elif i != 0 and i != len(list_of_integers) - 1 and list_of_integers[i] > list_of_integers[i-1] and list_of_integers[i] > list_of_integers[i+1]:
            return list_of_integers[i]
    return None
