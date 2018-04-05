#number - Number whose digits are to be added
def sum_of_digits(number):
    num = str(number)
    total = 0
    for i in num:
         total += int(i)
    return total

print(sum_of_digits(1244))
