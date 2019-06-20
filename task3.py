#!/usr/bin/env python
def factcount():
    "Calculate factorial"
    x = int(input("Intput the number: "))
    factorial = 1
    for i in range(2, x+1):
        factorial *= i
    return factorial

print ("N! =",factcount())
