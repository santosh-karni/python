#! /usr/bin/python3
"""" Write a program to print pattern"""


def print_pattern(pattern):
    """ function to demonstrate to printing pattern """
    for i in range(pattern):
        print("*"*(pattern-i) + "  "*i + "*"*(pattern-i))
    for j in range(pattern-1, 0, -1):
        print("*"*(pattern-j+1) + "  "*(j-1) + "*"*(pattern-j+1))


if __name__ == '__main__':
    print_pattern(5)
