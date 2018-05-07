#! /usr/bin/python3
""" Write a program takes two numbers as arguments and returns the largest of them."""


def max_of_three(num_a, num_b, num_c):
    """Function to find largest number """
    if num_a > num_b and num_a > num_c:
        return num_a
    elif num_b > num_c and num_b > num_a:
        return num_b
    elif num_c > num_a and num_c > num_b:
        return num_c
    else:
        print("all are equal")


def main():
    """Main Function"""
    try:
        num_a = float(input("Enter values of a : "))
        num_b = float(input("Enter value of b : "))
        num_c = float(input("Enter value of c : "))
        print(max_of_three(num_a, num_b, num_c))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()

