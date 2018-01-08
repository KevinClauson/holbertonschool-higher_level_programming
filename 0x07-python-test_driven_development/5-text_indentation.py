#!/usr/bin/python3
"""
module with one function that rints a text with 2 new lines 
after each of those characters: ., ? and :
"""


def text_indentation(text):
    """ function tht prints two lines after certain chars """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 1
    i = 0
    while i < len(text):
        if text[i] == '?' or text[i] == '.' or text[i] == ':':
            print(text[i])
            print()
            flag = 1
        else:
            if flag == 1:
                if text[i] == ' ':
                    while(text[i] == ' '):
                        i += 1
                print(text[i], end='')
                flag = 0
            else:
                print(text[i], end='')
        i += 1