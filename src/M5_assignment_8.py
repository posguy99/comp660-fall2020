
from math import log, log10

# doubling_time for 5/8a
def doubling_time(r):
    '''
    Return the time it takes to double your investment
    r = rate of investment return
    '''
    return round( log(2) / log(1 + r), 1)


# lambda function for doubling_time for 5/8b
doubling_time_yrs = lambda x: round( log10(2) / log10(1 + x) , 1)


def main():
    apr = 1.85

    print('5/8a - 1.85 APR compounded yearly')
    print('\ttime (y): ', doubling_time(apr/100))
    print('5/8a - 1.85 APR compounded monthly')
    print('\ttime (m): ', doubling_time((apr/12)/100))

    print()

    print('5/8b - 1.85 APR compounded monthly, in years, lambda')
    print('\ttime (y): ', doubling_time_yrs((apr/12)/100))

    print()

    apr = 10.0

    print('5/8c - 10.0 APR compounded yearly')
    print('\ttime: ', doubling_time(apr/100))


if __name__ == "__main__":
    main()
