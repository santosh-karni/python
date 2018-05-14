#! /user/bin/python3
"""" Program to print pattern """


def print_pattern_02(n_pattern):
    """Function to demonstrate printing pattern"""
    for i in range(0, n_pattern):
        for j in range(n_pattern, i, -1):
            print("* ", end="")
        print()


if __name__ == '__main__':
    print_pattern_02(5)
