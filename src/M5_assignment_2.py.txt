
# recursive computation of factorial

def factorial(num):
    ''' recursive computation of factorial
        num = factorial to return
    '''
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def main():
    print('Test case, print 5 factorial')
    print(factorial(5))


if __name__ == "__main__":
    main()
