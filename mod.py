def greetings(name):
    print(f"Hello, {name}")


def sum(x, y):
    return x + y


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        print(f"This a {self.brand}, {self.model}")
