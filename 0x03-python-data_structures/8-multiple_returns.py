#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence:
        t = (len(sentence), sentence[0],)
    else:
        t = (None,)
    return t
