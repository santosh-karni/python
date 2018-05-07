#! /usr/bin/python3
"""" Program to passe the Selling Price and Cost Price, returns
if there is a profit made in the sale."""


def is_profit(selling_price, cost_price):
    """" Function to find the profit"""
    profit = (selling_price-cost_price)/cost_price
    return profit


def main():
    """" Main Function"""
    try:
        cost_price = float(input("Enter cost price : "))
        selling_price = float(input("Enter the selling price : "))
        print(is_profit(selling_price, cost_price))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you "
              "are inserting digits only")


if __name__ == '__main__':
    main()
