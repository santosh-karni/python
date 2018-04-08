#! /usr/bin/python3
""" Program to get the profit when cost price and profit percentage is
specified."""

def get_profit(cost_price, profit_percent):
    """Function to calculate the profit."""
    profit = int(cost_price * profit_percent)
    return profit


def main():
    """ Main function."""
    try:
        cost_price = float(input("Enter cost price :"))
        profit_percent = float("specify the percentage of profit :")
        print("Profit is : {0}".format(get_profit(cost_price, profit_percent)))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you \
                are inserting digits only")

if __name__ == '__main__':
    main()
