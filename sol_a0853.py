#! /usr/bin/python3
"""
to check if the valid year passed to the function is a leap year or not.
Leap year is a year which has 366 days instead of 365 days in a year.
The function should return True if the year is a leap year, else it should return False.
In case of invalid input, it should return False.
"""


def is_leap_year(year):
    """Function to check year"""
    if year <= 0:
        print(False)
    elif year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return True
    else:
        return False


def main():
    """Main Function"""
    try:
        year = int(input("year : "))
        print(is_leap_year(year))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
