#!/usr/bin/env python3

names = ["Zak", "Joe", "Sally", "Mary", "Fred"]

name  = input("Enter a name to find: ")

found = False

for i in range(5):
    if (names[i] == name):
        print('I found that name!')
        found = True
        break
    else:
        continue
if not(found): print('I could not find that name!')



# names = ["Zak", "Joe", "Sally", "Mary", "Fred"]
#
# name  = input("Enter a name to find: ")
#
# found = False
#
# if name in names:
#     print('I found that name!')
#     found = True
#
# if not(found): print('I could not find that name!')

