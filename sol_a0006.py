def get_si_amount(principle, rate, years):
    si = float((principle*rate*years)//100)
    return (si+principle)

principle = input("Enter principle amount : ")
rate = input("Enter interest rate : ")
years = input("enter time in years : ")

print(get_si_amount(principle, rate, years))
