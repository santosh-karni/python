#cp - The cost price of the product.
#profit - The profit percentage of the product.


def get_profit(cp,profit_percent):
    profit = int(cp*profit_percent)
    return profit

#input from user
cp = int(input("Enter cost price :"))
profit_percent = input("specify the percentage of profit :")

print(get_profit(cp,profit_percent))
  
