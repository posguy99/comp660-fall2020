# do not assign a lambda expression, use a def flake8(E731)
double = lambda x: x * 2
print(double(5))

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2) == 0, my_list))
print(new_list)
