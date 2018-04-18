#! /usr/bin/python3
""" Program to make the number from digits when 5 digits are specified."""


def make_number_from_5_digits(num1, num2, num3, num4, num5):
    """Function to make the Number"""
    number = str(num1)+str(num2)+str(num3)+str(num4)+str(num5)
    return int(number)


print(make_number_from_5_digits(1, 2, 3, 4, 5))
