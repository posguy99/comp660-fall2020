
# Check if a string contains alpha, numeric, or alphanumeric characters

title = 'Monty Python and the Holy Grail'
year = '1975'

print(title.isalpha())      # False
print(title.isspace())      # False
print(year.isalnum())       # True
print(year.isdigit())       # True
print(year.isnumeric())     # True
