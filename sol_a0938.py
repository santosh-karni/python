#a - First digit
#b - Second digit
#c - Third digit
#d - Fourth digit
#e - Fifth digit


def make_number_from_5_digits(a,b,c,d,e):
    number = str(a)+str(b)+str(c)+str(d)+str(e)
    print type(number)
    return int(number)


#user input
a = int(input("Enter digit a : "))
b = int(input("Enter digit b : "))
c = int(input("Enter digit c : "))
d = int(input("Enter digit d : "))
e = int(input("Enter digit e : "))
print(make_number_from_5_digits(a,b,c,d,e))
#print type(make_number_from_5_digits(a,b,c,d,e))
