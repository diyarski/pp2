from functools import reduce
my_list = [1, -2, 4, -11]
def multiply(lst):
    return reduce(lambda x, y: x * y, lst)
print(multiply(my_list))
