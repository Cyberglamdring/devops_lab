#!/usr/bin/env python
def calc_factorial(x):
    """Calculate factorial"""
    factorial = 1
    for i in range(2, x + 1):
        factorial *= i
    return factorial


if __name__ == "__main__":
    x = int(input("Intput the number: "))
    print(calc_factorial(x))
