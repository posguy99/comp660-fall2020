#!/usr/bin/env python3

print('The Invoice Program\n')

customer_type = input('Enter customer type (r/w):\t')
invoice_total = float(input('Enter your invoice total:\t'))

if customer_type == 'r':
    if invoice_total > 0 and invoice_total < 100:
        discount_percent = 0
    elif invoice_total >= 100 and invoice_total < 250:
        discount_percent = .1
    elif invoice_total >= 250 and invoice_total < 500:
        discount_percent = .2
    elif invoice_total >= 500:
        discount_percent = .25
elif customer_type == 'w':
    if invoice_total > 0 and invoice_total < 500:
        discount_percent = .5
    elif invoice_total >= 500:
        discount_percent = .35
else:
    discount_percent = 0

discount_amount = invoice_total * discount_percent
new_invoice_total = invoice_total - discount_amount

print('Invoice total:\t\t\t'+str(invoice_total))
print('Discount percent:\t\t'+str(discount_percent))
print('Discount amount:\t\t'+str(discount_amount))
print('New invoice total:\t\t'+str(new_invoice_total))
