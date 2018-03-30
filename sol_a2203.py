def max_of_three(a,b,c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    elif c > a and c > b:
        return c
    else:
        print("all are equal")

a = int(input("Enter values of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))
print(max_of_three(a,b,c))