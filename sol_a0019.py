#! /usr/bin/python3
"""Write a Program when passed the radius returns the circumference. """


def get_circumference(radius):
    """Function to find the circumference"""
    circumference = 2*3.14*radius
    if radius < 1:
        circumference = 0
        print("enter a  positive value")
    else:
        return circumference


# r = int(input("Enter the radius of a circle :"))
A = get_circumference(20)

print(A)
