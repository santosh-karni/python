#! /user/bin/python3
""" Write a program to  take marks as input and return a number based on the grade obtained.

Grade can be calculated as follows
Grade 1 - above 80
Grade 2 - above 60 less than equal to 80
Grade 3 - above 40 less than equal to 60
Grade 4 - above 20 less than equal to 40
Grade 5 - above 00 less than equal to 20
If the marks is more than 100 or is invalid, return -1 """


def find_grade(marks):
    """Function to check marks"""
    if 80 < marks <= 100:
        return "grade 1"
    elif 60 < marks <= 80:
        return "Grade 2"
    elif 40 < marks <= 60:
        return "Grade 3"
    elif 20 < marks <= 40:
        return "Grade 4"
    elif 0 < marks <= 20:
        return "Grade 5"
    else:
        return -1


def main():
    """Main Function"""
    try:
        marks = int(input("Enter obtained marks : "))
        print(find_grade(marks))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
