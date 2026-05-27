class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print(f"{self.name} is a {self.breed} that loves to whoof whoof")


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number


owner1 = Owner("Danny", 10268, 1223)
dog1 = Dog("Bosco", "Njaaman Shepherd", owner1)

owner2 = Owner("Charles", 10356, 1443)
dog2 = Dog("Simba", "Boerbel", owner2)


print(dog1.owner.name)
print(dog1.bark())
