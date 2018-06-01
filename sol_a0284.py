#! /usr/bin/python3
""" Write a program to print pattern"""


def print_pattern(n_rows):
    """ Function to demonstrate pattern"""
    for i in range(n_rows):
        print(" "*(n_rows-i-1) + "* " * n_rows)


if __name__ == '__main__':
    print(print_pattern(5))
