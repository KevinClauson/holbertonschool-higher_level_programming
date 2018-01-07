#!/usr/bin/python3
"""
module with one function that rints a text with 2 new lines 
after each of those characters: ., ? and :
"""


def text_indentation(text):
    """ function tht prints two lines after certain chars """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if i == '?' or i == '.' or i == ':':
            print(i)
            print()
            flag = 1
        else:
            if flag == 1:
                if i == ' ':
                    pass
                else:
                    print(i, end='')
                flag = 0
            else:
                print(i, end='')
