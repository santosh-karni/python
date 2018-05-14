#! /usr/bin/python3
""" Write a program to print pattern"""


def print_pattern(pattern):
    """" Function to demonstrate pattern """
    for i in range(pattern):
        print(" "*i + "* "*(pattern-i))
    for j in range(pattern-1, 0, -1):
        print(" "*(j-1) + "* "*(pattern-j+1))


if __name__ == "__main__":
    print_pattern(5)
