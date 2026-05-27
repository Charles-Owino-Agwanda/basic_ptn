class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, new_age):
        if new_age >= 18:
            self.__age = new_age
        else:
            print(f"You must be an adult")

    def get_age(self):
        return self.__age


p1 = Person("Charles", 32)
print(p1.name)
p1.set_age(18)
print(p1.get_age())
