#! /usr/bin/python3
""" Write a program to find the Product of two numbers"""


def product(num_a, num_b):
    """Function to find product of 2 numbers"""
    return num_a*num_b


def main():
    """Main Function"""
    try:
        num_a = float(input("Enter A value : "))
        num_b = float(input("Enter B value : "))
        print(product(num_a, num_b))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()

