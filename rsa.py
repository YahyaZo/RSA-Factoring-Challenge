# rsa.py

import sys
from math import isqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def rsa_factorize(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i
    return n, 1

def rsa_factorize_file(filename):
    with open(filename, 'r') as file:
        rsa_numbers = [int(line) for line in file.readlines()]

    for rsa_number in rsa_numbers:
        factors = rsa_factorize(rsa_number)
        print(f"{rsa_number}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rsa.py <file>")
        sys.exit(1)

    filename = sys.argv[1]
    rsa_factorize_file(filename)

