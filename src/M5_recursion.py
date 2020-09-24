# Using an iterative function to find the
# factorial of a number


def factorial(num):
    ''' iterative computation of factorial '''
    result = 1
    for count in range(1, num+1):
        result = count * result
    return result


def factorial_r(num):
    ''' recursive computation of factorial '''
    if num == 1:
        return num
    else:
        return num * factorial_r(num - 1)


n = 6

print('n =', n)
print('Iterative: ', factorial(n))
print('Recursive: ', factorial_r(n))
