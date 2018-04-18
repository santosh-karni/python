#! /user/bin/python3
""" Write a Program to convert KMs to Feet when passed values in KMs"""


def convert_kms_to_feet(kms):
    """Function to convert kms to feet"""
    converter = int(3280.8399*kms)
    return converter


def main():
    """Main Function"""
    try:
        kms = int(input("Enter kilometers :"))
        result= convert_kms_to_feet(kms)
    except ValueError:
        print(print("Could not parse the input correctly. Please ensure that you \
                are inserting digits only"))
    finally:
        print(kms, "KMs = ", result, "feet")


if __name__ == '__main__':
    main()
