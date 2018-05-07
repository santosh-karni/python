#! /usr/bin/python3
"""" Program to count the number of even digits in a 5 digit number. """


def count_even_digits(num):
    """Function to check even digits of a number """
    cnt = 0
    for i in str(num):
        if int(i) % 2 == 0:
            cnt += 1
    return cnt


def main():
    """Main Function"""
    try:
        num = int(input("Enter number : "))
        print(count_even_digits(num))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
