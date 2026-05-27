class Cat:
    def __init__(self):
        pass

    def sound(self):
        print(f"Meow")


class Fox:
    def __init__(self):
        pass

    def sound(self):
        print(f"Wa-pa-pa-pa-pa-pow!")


c1 = Cat()
f1 = Fox()

for a in (c1, f1):
    a.sound()
