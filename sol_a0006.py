#principle - Principle amount to be used for calculation
#rate - Rate percentage to be used for calculation
#years - Number of years to be used for calculation

def get_si_amount(principle, rate, years):
    si = float((principle*rate*years)//100)
    return (si+principle)

#take input from user
#rate should be interms of decimal
principle = input("Enter principle amount : ")
rate = input("Enter interest rate : ")
years = input("enter time in years : ")

print(get_si_amount(principle, rate, years))
