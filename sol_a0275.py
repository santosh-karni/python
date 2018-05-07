#! /usr/bin/python3
"""" Program to print pattern """


def print_pattern_02(n):
    """Function to demonstrate printing pattern"""
    for i in range(0, n):
        for j in range(n, i, -1):
            print("* ", end="")
        print()


print_pattern_02(5)
