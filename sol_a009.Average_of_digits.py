def avg_of_digits(number):
    num = str(number)
    total = 0
    for i in num:
         total += float(i)
    return float(total/len(num))

print(avg_of_digits(56565656))