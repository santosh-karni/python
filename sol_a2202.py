#Find maximum  of 2 numbers
#num1 - The first number.
#num2 - The second number.

def mymax(num1, num2):
    if num1 > num2:
        print(num1, "is greater")
    elif num2 > num1:
        print(num2, "is greater")
    else:
        print("both are equal")

print(mymax(12,12))
