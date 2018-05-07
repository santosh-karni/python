#! /usr/bn/python3
""" Write a program when passed the side of a cube, returns the volume of the cube. """


def cub_volume(side):
    """ Function to find Cube Volume"""
    return float(side)**3


def main():
    """Main Function"""
    try:
        side = float(input("Enter side of cube : "))
        print(cub_volume(side))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you \
                are inserting digits only")


if __name__ == '__main__':
    main()
