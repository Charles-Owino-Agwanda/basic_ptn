def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(4))


def factorial(n):
    if n == 1:
        return n
    else:
        print(f"n = {n} : now calling factorial (n-1)")
        lower_fact = factorial(n - 1)
        current_fact = n * lower_fact
        print(
            f"n = {n} : factorial(n-1) returned {lower_fact} multiplied by n to get {current_fact}"
        )
        return current_fact


print(factorial(4))
