def exponential(a, n):
    if n == 0:
        return 1
    else:
        return a * pow(a, n - 1)


print(exponential(2, 3))
print(exponential(5, 0))
