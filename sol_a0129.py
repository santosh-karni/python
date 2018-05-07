#! /usr/bin/python3
""" Program to find the maximum out of the 4 numbers passed to it."""


def find_maximum_in_4(num1, num2, num3, num4):
    """ Function to compare numbers """
    if num1 > num2 and num1 > num3 and num1 > num4:
        return num1
    elif num2 > num3 and num2 > num4 and num2 > num1:
        return num2
    elif num3 > num4 and num3 > num1 and num3 > num2:
        return num3
    else:
        return num4


def main():
    """ Main Function"""
    try:
        num1 = float(input("Enter first value : "))
        num2 = float(input("Enter 2nd value : "))
        num3 = float(input("Enter 3rd value : "))
        num4 = float(input("Enter 4th value : "))
        print(find_maximum_in_4(num1, num2, num3, num4))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
