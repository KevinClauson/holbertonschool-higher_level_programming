#!/usr/bin/python3
""" module with one function """


def read_lines(filename="", nb_lines=0):
    line_count = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        if nb_lines <= 0:
            for line in f: 
                print("{}".format(line.rstrip()))
        else:
            for line in f:
                if line_count >= nb_lines:
                    break
                print("{}".format(line.rstrip()))
                line_count += 1
