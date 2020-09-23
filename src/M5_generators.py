# basic generator function


# def myGen(n):
#     yield n
#     yield n+1


# g = myGen(1)
# print(next(g))
# print(next(g))
# print(next(g))


def myGen():
    yield "These"
    yield "words"
    yield "come"
    yield "one"
    yield "at"
    yield "a"
    yield "time"


gen = myGen()
for i in range(1, 9):
    print(next(gen))
