#Check if the number is even
#num = number to be checked

def is_even(num):
    if num % 2 == 0:
        return int(True)
    else:
        return int(False)

num = int(input("Enter a number : "))
print(is_even(num))
