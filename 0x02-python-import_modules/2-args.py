#!/usr/bin/python3
import sys
def main(argv):
    if len(argv) - 1 == 0:
        print("0 arguments")
    elif len(argv) - 1 == 1:
        print("{} arguments: ".format(len(argv) - 1)
    else:
        print("{}: {}".format(len(argv) - 1, argv[])
        for i, x in enumerate(argv[1:], 1):
              print("{:d}: {}".format(i, x))

if __name__ == "__main__":
    import sys
