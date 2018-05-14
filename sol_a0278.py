#! /usr/bin/python3
""" Write a program to prints the pattern. """


def print_pattern_05(n_pat):
    """ Function to demonstrate printing pattern """
    k = n_pat-1
    for i in range(0, n_pat):
        for j in range(0, k):
            print("# ", end=" ")

        k = k - 1
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")


if __name__ == '__main__':
    print_pattern_05(5)
