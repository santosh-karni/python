#! /user/bin/python
""" Write a program when passed a 5 digit number returns the average of the digits"""


def avg_of_5_digits(number):
    """Function to get average"""
    num = str(number)
    total = 0
    for i in num:
        total += float(i)
    return float(total/len(num))


def main():
    """main Function"""
    try:
        number = input("Enter 5 digit number : ")
        print(avg_of_5_digits(number))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you"
              " are inserting digits only")


if __name__ == '__main__':
    main()
