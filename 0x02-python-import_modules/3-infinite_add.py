#!/usr/bin/python3
"""
DocString Goes Here
"""
if __name__ == "__main__":
    from sys import argv
    result = 0

    for i, x in enumerate(argv[1:]):
        result += int(x)

        print("{:d}".format(result))
