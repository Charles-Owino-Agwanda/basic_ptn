class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))


class Coordinate:
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

    def distance(self, other):
        x_diff_squared = (self.x - other.x) ** 2
        y_diff_squared = (self.y - other.y) ** 2
        return (x_diff_squared + y_diff_squared) ** 0.5


origin = Coordinate(0, 0)
point = Coordinate(3, 4)

print(origin.distance(point))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} : {self.age}"


p1 = Person("Charles", 36)
print(p1)
