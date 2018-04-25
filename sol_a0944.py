#! /user/bin/python3
""" Program to return number of odd digits in a number """


def count_odd_digits(number):
    """Function to check the number"""
    cnt = 0
    for i in str(number):
        if int(i) % 2 == 1:
#            print(i)
            cnt += 1
    return cnt


def main():
    """ Main Function"""
    try:
        number = int(input("Enter a number : "))
        print(count_odd_digits(number))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you"
              " are inserting digits only")


if __name__ == '__main__':
    main()
