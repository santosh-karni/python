#! /user/bin/python3
"""" Write a program to find the Nth element in a geometric progression """


def find_nth_element_in_gp(int_a, int_r, int_n):
    """ Function to check the nth element"""
    nth_element = int_a*(int_r**int_n)
    return nth_element


def main():
    """Main Function"""
    try:
        int_a = int(input("Enter First term : "))
        int_r = int(input("Enter Scalar Factor : "))
        int_n = int(input("Enter nth term : "))
        print(find_nth_element_in_gp(int_a, int_r, int_n))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
