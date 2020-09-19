#!/usr/bin/env python3

# default arguments, assume a default value if one is not provided

def display_info(name, age='42'):
    print('Name: ', name, 'Age', age)

display_info(age='56', name='Marc Wilson')
display_info(name='Marc Wilson')
