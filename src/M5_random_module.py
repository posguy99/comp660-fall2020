import random

# use of the random module
print(random.random())          # a float value >= 0.0 and < 1.0
print(random.random()*100)      # a float value >= 0.0 and < 100.0

# use of the randint method
print(random.randint(1, 100))       # an int from 1 to 100
print(random.randint(101, 200))     # an int from 101 to 200
print(random.randint(0, 7))         # an int from 0 7

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print("Your roll: ", die1, die2)

print(random.randrange(1, 100))             # an int from 1 to 99
print(random.randrange(100, 200, 2))        # an even int from 100 to 198
print(random.randrange(11, 250, 2))         # an odd int from 11 to 249
