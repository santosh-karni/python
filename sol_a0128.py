#! /user/bin/python
""" Write a program to check the given number is Zero orr not when number is specified """


def is_zero(number):
    """ Function to check the number"""
    if number == 0:
        print(True)
    else:
        print(False)


def main():
    """Main function"""
    try:
        number = int(input("Enter a number : "))
        is_zero(number)
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
