#! /usr/bin/python3
"""" Write a program to print pattern"""


def print_pattern(pattern):
    """ function to demonstrate to printing pattern """
    for i in range(pattern):
        print(" "*(pattern-i-1) + "* "*(i+1))
    for j in range(pattern-1, 0, -1):
        print(" "*(pattern-j) + "* "*j)


if __name__ == '__main__':
    print_pattern(5)
