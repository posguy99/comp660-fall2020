'''
This module contains functions for converting
temperatures between degrees Fahrenheit
and degrees Celsius
'''
def to_celsius(fahrenheit):
    '''
    Accepts degrees Fahrenheit
    Returns degrees Celsius
    '''
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def to_fahrenheit(celsius):
    '''
    Accepts degrees Celsius
    Returns degrees Fahrenheit
    '''
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def main():
    for temp in range(0, 212, 40):
        print(temp, 'Fahrenheit: ', round(to_celsius(temp)), 'Celsius')

    for temp in range(0, 100, 20):
        print(temp, 'Celsius: ', round(to_fahrenheit(temp)), 'Fahrenheit')


if __name__ == '__main__':
    main()
