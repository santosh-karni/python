#! /user/bin/python3
""" Write a program to Add 2 numbers"""


def add_two_numbers(num1, num2):
    """Function to add two numbers"""
    add = num2+num1
    return add


def main():
    """Main Function"""
    try:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number : "))
        sum_2 = add_two_numbers(num1, num2)
        print(sum_2)
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
