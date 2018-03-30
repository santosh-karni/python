#number - Number to be reversed
def reverse_5_digit_int(number):
    reminder = 0
    reverse = 0
    while number > 0:
        reminder = number%10
        number = number//10
        reverse = (reverse*10) + reminder
    return reverse


print(reverse_5_digit_int(12345))