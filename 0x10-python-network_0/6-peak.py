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
    elif size == 1:
        return nums[0]
    elif size == 2:
        return max(nums[0], nums[1])
    mid = size // 2
    start = 0
    end = size - 1
    while start < end:
        if mid == start or mid ==  end:
            return nums[mid]
        elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return nums[mid]
        elif nums[mid] < nums[mid+1]:
            start = mid + 1
            mid = (start + end) // 2
        elif nums[mid] < nums[mid-1]:
            end = mid - 1
            mid = (start + end) // 2
        else:
            return nums[mid]
    return nums[mid]
