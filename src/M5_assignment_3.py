
# 3. Write a recursive Python function that returns the sum of the first
# n integers. (Hint: The function will be similar to the factorial function!)
# ie sum_nint(3) = 1 + 2 + 3 = 6 , sum_nint(4) = 1 + 2 + 3 + 4 = 10.

def sum_nint(num):
    ''' recursive sum of integers
        num = last integer in range
    '''
    if num == 1:
        return 1
    else:
        return num + sum_nint(num - 1)


def main():
    print('Test cases')
    n = 3
    print('Sum of first', n, 'integers is', sum_nint(n))
    n = 4
    print('Sum of first', n, 'integers is', sum_nint(n))


if __name__ == "__main__":
    main()
