# basic module import
# use as, since I named the temperature.py differently to indicate the module
# its from

import M5_temperature as temperature

print('The current temperature is: ', temperature.to_fahrenheit(0))
print('The current temperature is: ', temperature.to_celsius(32))
