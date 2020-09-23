# basic generator function


def myGen(n):
    yield n
    yield n+1

g = myGen(1)
print(next(g))
print(next(g))
print(next(g))
