#basic_salary - Basic Salary in Rupees
#dearness_allowance - Dearness Allowance in percentage of Basic
#house_rent - House Rent Allowance in Rupees

def calculate_gross_salary(basic_salary, dearness_allowance, house_rent):
    gross_sal = basic_salary+(basic_salary*dearness_allowance)+house_rent
    return gross_sal

basic_salary = input("Enter basic salary : ")
dearness_allowance = input("Enter dearness_allowance : ")
house_rent = input("Enter house_rent  : ")

print(calculate_gross_salary(basic_salary,dearness_allowance, house_rent))
