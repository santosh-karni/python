#! /user/bin/python3
""" Write a program takes two numbers as arguments and returns the largest of them.
 Use the if-then-else construct available in your language. """


def mymax(num1, num2):
    """Function to check max. of numbers"""
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        print("both are equal")


def main():
    """Main Function"""
    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        print(mymax(num1, num2))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
