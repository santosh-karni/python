#! /user/bin/python3
"""Write a program that takes input an integer and finds sum till that number. """


def find_sum_till_n(num):
    """Function to find the sum of numbers"""
    sum_n = (num*(num+1)/2)
    return sum_n


def main():
    """Main Function"""
    try:
        num = int(input("Enter a number : "))
        print(find_sum_till_n(num))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
