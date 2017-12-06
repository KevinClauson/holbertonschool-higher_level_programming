#!/usr/bin/python3
def remove_char_at(str, n):
    num = 0
    arr = ""
    for i in str:
        if num != n:
            arr += i
        num += 1
    return arr
