#! /usr/bin/python3
"""Write a program which print the pattern"""


def print_pattern_03(n):
    """Function to demonstrate printing pattern """
    for i in range(0, n):
        # outer loop to handle number of rows
        for j in range(0, i+1):
            # outer loop to handle number of columns
            print("* ",end="")
        print()


print_pattern_03(5)
