#x = input("entera number :")
#conversion = 1000
#mm = x*conversion
#print(mm)

def convert_kms_to_mms(km):
    converter = km *1000000
    return converter

km = int(input("enter a value : "))
a = convert_kms_to_mms(km)

print km,"kms =", a,"mms"
