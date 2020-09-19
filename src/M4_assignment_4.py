#!/usr/bin/env python3

from math import sqrt

# 4a - Using the equation above, build a function called (velocityFinal) which returns
#      the final velocity of the object rounded to one decimal place.
def velocityFinal(vo, a, d):
    ''' vo = initial velocity
        a  = uniform acceleration
        d  = distance traveled '''

    return round(sqrt((vo**2) + (2*a*d)),1)

# 4b - A ball is gently dropped from a height of 51m (167 ft), the acceleration
#      due to gravity is a constant 9.8 m/s2. Using the arguments described and function
#      you built above, what is the calling expression to determine the final velocity
#      before impact?
final = velocityFinal(0, 9.8, 51)

#4c - Based on the function you created , calculate the speed of the ball before
#     it strikes the ground ? Answer should be in m/s
print(final, 'm/s') # 31.6 m/s

