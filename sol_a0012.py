#number - Number whose digits are to be multiplied.

def product_of_5_digits(number):
    num = str(number)
    product = 1
    ls = list(num)
    for i in num:
        product = product*i
        print(product)
product_of_5_digits(12345)
