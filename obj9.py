class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


Person1 = Person("John", 36)
print(Person1.greet())


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")


d1 = Dog("Buddy", 3)

print(d1.bark())


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")


p1 = Person("Tobias")
print(p1.greet())
p1.welcome()


class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(f"{self.brand}")


c1 = Car("Ford")
# del c1.brand
c1.show()


class Person:
    species = "Human"

    def __init__(self, name):
        self.name = name


p1 = Person("Charles")
p2 = Person("Kevin")

print(p1.name, ":", p1.species)
print(p2.name, ":", p2.species)

Person.species = "Ape"

print(p1.name, ":", p1.species)
print(p2.name, ":", p2.species)

p1.age = 32
p1.city = "Nairobi"

print(p1.name, ":", p1.species, ":", p1.age, ":", p1.city)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


s1 = Student("Anna", "A")
print(s1.grade)

s1.grade = "B"
print(s1.grade)
