#! /usr/bin/python3
"""Write a program which print the pattern"""


def print_pattern_01(n_pattern):
    """Function to demonstrate printing pattern """
    for i in range(0, n_pattern):
        for j in range(0, n_pattern):
            print("*", end=" ")
        print()


if __name__ == '__main__':
    print_pattern_01(5)
