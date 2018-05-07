#! /usr/bin/python3
"""which takes a number and the power to be calculated and
returns the result of x to the power n"""


def find_pow(int_x, int_n):
    """Function to find the power of a number"""
    power = int_x**int_n
    return power


def main():
    """Main Function"""
    try:
        int_x = float(input("Enter a value of x :"))
        int_n = float(input("Enter n value : "))
        print(find_pow(int_x, int_n))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
