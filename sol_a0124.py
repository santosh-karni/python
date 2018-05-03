#! /user/bin/python3
""" Program to find the Minimum out of the 3 numbers passed to Function."""


def my_minimum(num1, num2, num3):
    """ Function to pass numbers and check"""
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num3 and num2 < num1:
        return num2
    else:
        return num3


def main():
    """" Main Function"""
    try:
        num1 = float(input("Enter 1st number : "))
        num2 = float(input("Enter 2nd number : "))
        num3 = float(input("Enter 3rd number : "))
        print(my_minimum(num1, num2, num3))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
