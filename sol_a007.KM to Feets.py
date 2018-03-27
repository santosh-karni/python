def convert_kms_to_feet(kms):
    converter = int(3280.8399*kms)
    return converter

kms = int(input("Enter kilo meters :"))
print(convert_kms_to_feet(kms))