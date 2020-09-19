#!/usr/bin/env python3

vehicle = ['Honda', 'Civic']
def display_car(car):
    print('You own a ' + car[0] + ' ' + car[1])
    car[0] = 'Chevy'
    car[1] = 'Camaro'
display_car(vehicle)
print(vehicle[0] + ' ' + vehicle[1])
