#! /use/bin/python3
""" Write a program to check if a number is even or no. Return 0 if the number is even,
 else return -1."""


def is_even(num):
    """Function to check the number"""
    if num <= 0:
        print('invalid. Positive numbers are allowed')
    elif num % 2 == 0:
        return 0
    else:
        return -1


def main():
    """Main Function"""
    try:
        num = int(input("Enter a number : "))
        print(is_even(num))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
