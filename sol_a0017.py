def get_profit(cp,profit_percent):
    profit = int(cp*profit_percent)
    return profit

cp = int(input("Enter cost price :"))
profit_percent = input("specify the percentage of profit :")

print(get_profit(cp,profit_percent))
  
