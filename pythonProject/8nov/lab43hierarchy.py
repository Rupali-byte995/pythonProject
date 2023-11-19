# hierarchial inheritance
class Vehicle:
    def info(self):
        print("I am parking class")


class Car(Vehicle):
    def info(self):
        return "I am car"

    def strt(self):
        print("I am starting")


class Bike(Vehicle):
    def info(self):
        print("I am bike")


c = Car()
print(c.info())
b = Bike()
b.info()
