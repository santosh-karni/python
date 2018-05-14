#! /usr/bin.python3
""" Write a program to prints the pattern. """


def print_pattern_05(n_pattern):
    """function to demonstrate to printing pattern"""
    k = 2 * n_pattern - 2
    for i in range(0, n_pattern):
        for j in range(0, k):
            print(end=" ")

        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


if __name__ == '__main__':
    print_pattern_05(5)
