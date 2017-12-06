#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print('{:s}'.format(chr(ord(i) - 32) if ord(i) >= ord('a') and
                            ord(i) <= ord('z') else i), end="")
    print("".format(), end="\n")
