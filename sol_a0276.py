#! /user/bin/python3
"""Write a program which print the pattern"""


def print_pattern_03(n_pattern):
    """Function to demonstrate printing pattern """
    for i in range(0, n_pattern):
        # outer loop to handle number of rows
        for j in range(0, i+1):
            # inner loop to handle number of columns
            print("* ", end="")
        print()


if __name__ == '__main__':
    print_pattern_03(5)
