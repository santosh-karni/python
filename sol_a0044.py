#! /user/bin/python3
""" Write a Program when passed a number checks if
the number is palindrome or not and returns 0 or -1."""


def is_palindrome_number(num):
    """Function to check number  """
    var = str(num)
    rev = var[::-1]
    if rev == var:
        print(0)
    else:
        print(-1)


is_palindrome_number(12345)
