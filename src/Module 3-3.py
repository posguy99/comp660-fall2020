#!/usr/bin/env python3

# Module 3 Assignment Pt 3
# recommend clothing based on temperature

print('What shall I wear today?\n')

first_name = input('Please Enter Your First Name: ')
temp       = float(input("What is Today's Temperature: "))

print()

if temp < 70.0:
    print('Hi', first_name, ', You should probably bring a sweater')
else:
    print('Hi', first_name, ', It will be a warm day, T-shirt time!')

