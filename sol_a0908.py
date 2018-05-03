#! /user/bin/python3
"""" program to check whether a given number is a multiple of 3"""


def is_multiple_of_3(num):
    """ check the number is multiples of 3 or not"""
    if num % 3 == 0:
        return 0
    else:
        return -1


def main():
    """ Main function"""
    try:
        num = float(input("Enter a number : "))
        print(is_multiple_of_3(num))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
