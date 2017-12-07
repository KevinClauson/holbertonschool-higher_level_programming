#!/usr/bin/python3
from sys import argv
def main():
    n_args = len(argv) - 1
    print("{:d} arguments{}".format(n_args, '.' if n_args < 1 else ":"))
    t = 0
    for i in argv:
        if t > 0:
            print("{:d}: {:s}".format(t, i))
        t += 1
if __name__ == "__main__":
    main()
