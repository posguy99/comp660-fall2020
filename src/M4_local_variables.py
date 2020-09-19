#!/usr/bin/env python3

# local variables

def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate         # tax is a local variable
    return tax                      # return statement is necessary

def main():
    tax = calculate_tax(85.0, .05)  # tax is a local variable
    print('Tax: ', tax)

if __name__ == '__main__':
    main()
