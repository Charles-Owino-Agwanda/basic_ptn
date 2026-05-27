class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


Car1 = Car("Honda", "Fit")
Boat1 = Boat("Ibiza", "Touring 20")
Plane1 = Plane("Boeing", "777")


for x in (Car1, Boat1, Plane1):
    x.move()
