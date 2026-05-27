class Person:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def printname(self):
        print(f"{self.fname}, {self.lname}")


class Student(Person):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)
        self.graduation_year = year

    def welcome(self):
        print(
            f"Welcome, {self.fname} {self.lname}, to the class of {self.graduation_year}"
        )


person1 = Person("Charles", "Owino")
person1.printname()
student1 = Student("Mike", "Olsen", 2019)
student1.printname()
print(student1.graduation_year)
student1.welcome()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}")


class Dog(Animal):
    pass


d1 = Dog("Rex")
d1.speak()
