def get_circumference(radius):
    circumference = 2*3.14*radius
    if radius < 1:
        circumference = 0
        print("enter a  positive value")
    else:
        return circumference
#r = int(input("Enter the radius of a circle :"))
a= get_circumference(20)
b= get_circumference(20.3)
c= get_circumference(-20)

print(a)
print(b)
print(c)
