#! /user/bin/python3
""" Write a program to Convert Fahrenheit to Celsius when Fahrenheit temperature is
 specified"""


def convert_fahrenheit_to_celsius(fth_temp):
    """Function to convert F to C"""
    converter = float(5/9.0*(fth_temp-32))
    return converter

def main():
    """Main Function"""
    try:
        fth_temp = float(input("Temperature in Fahrenheit :"))
        result = convert_fahrenheit_to_celsius(fth_temp)
    except ValueError:
        print(print("Could not parse the input correctly. Please ensure that you \
                are inserting digits only"))
    finally:
        print(fth_temp, "F =", result, "C")


if __name__ == '__main__':
    main()

