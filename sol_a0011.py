#! usr/bin/python3
""" Program to find the Sum of 5 digit number"""


def sum_of_digits(number):
    """ Function to calculate sum """
    num = str(number)
    total = 0
    for i in num:
        total += int(i)
    return total


#print(sum_of_digits(12))
