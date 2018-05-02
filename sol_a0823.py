#! /user/bin/python3
""" Write a program for calculating the factorial of a number"""


def calculate_factorial(num):
    """Function to calculate factorial"""
    factorial = 1
    if num < 0:
        return None
    elif num == 0:
        return 1
    else:
        for i in range(1, num+1):
            factorial *= i
        return factorial


def main():
    """Main Function"""
    try:
        num = int(input("Enter a number : "))
        print(calculate_factorial(num))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
