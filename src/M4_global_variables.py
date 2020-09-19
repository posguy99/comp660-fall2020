#!/usr/bin/env python3

# global variables

tax = 0.0                           # tax is a global variable

def calculate_tax(amount, tax_rate):
    global tax                      # access global variable
    tax = amount * tax_rate         # change global variable

def main():
    calculate_tax(85.0, .05)
    print('Tax: ', tax)             # Tax is 4.25 (the global variable)

if __name__ == '__main__':
    main()
