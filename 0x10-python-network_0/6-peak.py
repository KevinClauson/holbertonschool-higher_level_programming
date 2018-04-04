#!/usr/bin/python3
"""finds peak"""


def find_peak(list_of_integers):
    """
    finds peak
    """
    nums = list_of_integers
    size = len(nums)
    if not nums or size == 0:
        return None
    elif num == 1:
        return nums[0]
    peak = None
    for i in range(size):
        if i == 0 and nums[i] >= nums[i+1]:
            peak = nums[i]
        elif i == size - 1 and nums[i] > nums[i-1]:
            return list_of_integers[i]
        elif i != 0 and i != size - 1:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return nums[i]
    return peak
