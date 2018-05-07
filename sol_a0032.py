#! /usr/bin/python3
"""Program to convert kms to mms when passed value in KMs returns values in Millimeters.
Your function will not be tested for negative values."""


def convert_kms_to_mms(kms):
    """Function to convert kms to mms"""
    converter = kms * 1000000
    return converter


def main():
    """Main Function"""
    try:
        kms = int(input("enter a value : "))
        result = convert_kms_to_mms(kms)
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you \
                    are inserting digits only")
    finally:
        print(kms, "kms =", result, "mms")


if __name__ == '__main__':
    main()

