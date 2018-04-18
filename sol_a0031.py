#! /user/bin/python3
"""Write a program when passed the Basic salary, Dearness Allowance (in percentage of Basic)
 and House Rent Allowance in rupees, calculates and returns the gross salary,
 which is the sum of all three."""


def calculate_gross_salary(basic_salary, dearness_allowance, house_rent):
    """Function to Calculate Gross Salary"""
    gross_sal = basic_salary+(basic_salary*dearness_allowance)+house_rent
    return gross_sal


def main():
    """main Function"""
    try:
        basic_salary = float(input("Enter basic salary : "))
        dearness_allowance = float(input("Enter dearness_allowance : "))
        house_rent = float(input("Enter house_rent  : "))

        print(calculate_gross_salary(basic_salary, dearness_allowance, house_rent))
    except ValueError:
        print("Could not parse the input correctly. Please ensure that you \
                    are inserting digits only")


if __name__ == '__main__':
    main()
