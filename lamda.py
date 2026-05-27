def double(x):
    return x * 2


print(double(2))


double = lambda x: x * 2
print(double(6))

print((lambda x: x**2)(3))

numbers = [2, 3, 4, 5]

print(list(map(lambda x: x * 2, numbers)))


def root(x, y):
    return x ** (1 / y)


print(root(4, 2))

root = lambda x, y: x ** (1 / y)

print(root(25, 2))
print(root(8, 3))

sort = lambda s: sorted(s)

print(sort([6, 2, 3, 9, 1, 5]))


list1 = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

filtered_list = list(filter(lambda x: x > 9, list1))

print(filtered_list)

list2 = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

mapped_list = list(map(lambda x: x % 2, list2))

print(mapped_list)
