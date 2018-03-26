def get_circumference(r):
    circumference = 2*3.14*r
    return circumference
r = int(input("Enter the radius of a circle :"))
if r < 1:
    circumference = 0
    print(circumference)
    print("enter a positive value")
a= get_circumference(r)

print(a)