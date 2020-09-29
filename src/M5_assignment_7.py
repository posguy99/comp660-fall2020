
# 6. Write a lambda function (area_circle_lambda) that returns the area
# of a circle of a given radius.


area_circle_lambda = lambda r : 3.1415926536 * (r ** 2)


def main():
    print('Test case')
    print('area_circle_lambda(5) is', area_circle_lambda(5))


if __name__ == "__main__":
    main()
