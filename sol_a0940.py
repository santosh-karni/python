#! /user/bin/python3
"""Write a Program check if a number is odd or not. Return -1 if even, else return 0 """


def check_if_odd(num):
    """Function to check"""
    if num <= 0:
        print(num, "is not valid. Retry with positive value")
    elif num % 2 == 0:
        return -1
    else:
        return 0


def main():
    """Main Function"""
    try:
        num = int(input("Enter a Number : "))
        print(check_if_odd(num))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()

