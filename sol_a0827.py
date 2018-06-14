#! /usr/bin/python3
""" Program to generate Nth Fibonacci number. """


def gen_fibonacci(num):
    """ Function which generates the Nth Fibonacci number """
    num1 = 0
    num2 = 1
    if num < 0:
        return "incorrect"
    elif num == 1:
        return num1
    elif num == 2:
        return num2
    else:
        for i in range(2, num):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return num2


if __name__ == '__main__':
    print(gen_fibonacci(5))
