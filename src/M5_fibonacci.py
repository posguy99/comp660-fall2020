# a Fibonacci series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...

# # an iterative function that computes a Fibonacci sequence
# def fib(num):
#     if num == 0:
#         print(0)
#     elif num == 1:
#         print(1)
#     else:
#         n1 = 0
#         n2 = 1
#         n3 = 0
#     while n2 <= num:
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#         # or do it this way: n1, n2 = n2, n1 + n2
#         print(n1)


# fib(100)


# # a recursive function that computes a Fibonacci sequence
# def fib(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fib(num - 1) + fib(num - 2)


# for i in range(12):
#     print(fib(i), sep=', ')


# a generator function that computes a Fibonacci sequence
def fib():
    n1, n2 = 0, 1
    for i in range(12):
        yield n1
        n1, n2 = n2, n1 + n2


print(list(fib()))
