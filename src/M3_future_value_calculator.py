#!/usr/bin/env python3

print('Welcome to the Future Value Calculator\n')

# potted choice to make the first pass through the loop work
# _while_ evaluates at the *top* of the loop
choice = 'y'
while choice == 'y':
    monthly_investment = float(input('enter your monthly investment:\t'))
    yearly_interest_rate = float(input('Enter yearly interest rate:\t'))
    years = int(input('Enter number of years:\t\t'))

    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    print('Future value:\t\t\t' + str(round(future_value,2)))
    # chose to continue at the bottom of the loop...
    choice = input('Continue? (y or n)\t\t')
print('Thank you for using the Future Value Calculator')
