#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    digit = [1, 5, 10, 50, 100, 500, 1000]
    num = []
    k = 0
    for i in roman_string:
        k = 0
        for j in roman:
            if i == j:
                num.append(digit[k])
            k += 1
    length = len(num)
    k = length - 1
    result = 0
    while k >= 0:
        if k > 0 and num[k] > num[k-1]:
            result = num[k] - num[k-1]
            k -= 1
        else:
            result = result + num[k]
        k -= 1
    return result
