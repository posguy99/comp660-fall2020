
# 6. Write a simple function (area_circle) that returns the area
# of a circle of a given radius.


def area_circle(r):
    ''' Calculate the area of a circle given the radius
        r = radius (in some unstated unit of measurement)
    '''
    return 3.1415926536 * (r ** 2)


def main():
    print('Test case')
    print('area_circle(5) is', area_circle(5))


if __name__ == "__main__":
    main()
