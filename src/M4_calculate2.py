#!/usr/bin/env python3

# required arguments (throws error if not passed in)
def calculate(x, y):
    ''' This returns the sum of x and y '''
    return x + y

print(calculate(10))

# TypeError: "calculate() missing 1 required positional argument: 'y'"
#
# module body in M4_calculate2.py at line 8
# print(calculate(10))
