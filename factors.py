import sys
from math import isqrt

def factorize(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def factorize_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line) for line in file.readlines()]

    for number in numbers:
        factors = factorize(number)
        print(f"{number}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)

    filename = sys.argv[1]
    factorize_file(filename)

