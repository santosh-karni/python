#! /usr/bin/python3
""" Program to get the simple interest when principle amount, rate and years are
specified."""


def get_si_amount(principle, rate, years):
    """Function to calculate simple interest."""

    simple_int = float((principle*rate*years)/100.0)
    return simple_int+principle


def main():
    """ Main function."""
    try:
        principle = float(input("Enter principle amount : "))
        rate = float(input("Enter interest rate : "))
        years = float(input("enter time in years : "))
        print(get_si_amount(principle, rate, years))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you \
                    are inserting digits only")


if __name__ == '__main__':
    main()
