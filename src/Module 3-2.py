#!/usr/bin/env python3

letter = "Hizthere,zThisziszhowzazpasszstatementzworks!"
for i in letter:
    if i == "mn":   # this is whack and will never work
        pass
    elif i == "z":
        print(" ",end="")
    else:
        print(i, end="")
print()

