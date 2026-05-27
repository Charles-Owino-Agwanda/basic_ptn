def bubble_sort(items):
    """
    implementation of bubble sort.

    """
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


# print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account = BankAccount(100)
account.deposit(50)
# print(account.balance)


def r(s):
    if len(s) == 0:
        return s
    else:
        return r[s[1:] + s[0]]


# print(r(r("programming")))


numbers = [-2, 5, -9, 8, -1, 10]

result = filter(lambda x: x >= 0, numbers)
# print(list(result))


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius


# print(Circle(3).circumference())


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect = Rectangle(3, 4)
# print("Area:", rect.area(), "Perimeter:", rect.perimeter())

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x**2, numbers)
print(list(result))


class ExampleClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Shape:
    def __init__(self, name):
        self.name = name


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side


circle = Circle(3)
square = Square(4)
total_area = circle.area() + square.area()
print("Total Area:", total_area)
