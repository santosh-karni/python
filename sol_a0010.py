#! user/bin/python3
""""Program to reverse a number when a 5 digit number is specified. """


def reverse_5_digit_int(number):
    """Function to reverse a number """
    reminder = 0
    reverse = 0
    while number > 0:
        reminder = number%10
        number = number//10
        reverse = (reverse*10) + reminder
    return reverse


print(reverse_5_digit_int(12345))
