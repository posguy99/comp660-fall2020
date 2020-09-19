#!/usr/bin/env python3

from math import sqrt

# 4a - Using the equation above, build a function called (velocityFinal) which returns
#      the final velocity of the object rounded to one decimal place.
def velocityFinal(vo, a, d):
    ''' vo = initial velocity
        a  = uniform acceleration
        d  = distance traveled '''

    return round(sqrt((vo**2) + (2*a*d)),1)

# 5 - finalVelocity isn't really needed, but you have to solve for t to get what
#     is going to be used in elapsedTime()
def finalVelocity(u, a, t):
    ''' u = initial velocity
        a = acceleration
        t = elapsed time from u to v '''

    return round(u+(a*t),1)

# 5a - Create a function which returns the elapsed time using the arguments v, u, and a.
# Calculate the elapsed  time from when the ball is dropped till it hits the ground
# (1 decimal place)? Use standard gravity as 9.8 m/s2
def elapsedTime(v, u, a):
    ''' v = final velocity
        u = initial velocity
        a = acceleration '''

    return round(((v-u)/a), 1)

# use the velocityFinal() function from 4a
time = elapsedTime(velocityFinal(0, 9.8, 51), 0, 9.8)

print(time, "sec")      # 3.2 sec
