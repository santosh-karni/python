#! /usr/bin/python3
""" Write a program to print nth prime number """


def find_nth_prime(n):
    """initial prime number list """
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        for i in prime_list:
            if num % i == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list[-1]


if __name__ == '__main__':
    print(find_nth_prime(5))
