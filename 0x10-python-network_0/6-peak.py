#!/usr/bin/python3
"""finds peak"""


ç∂çdef find_peak(nums):
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
