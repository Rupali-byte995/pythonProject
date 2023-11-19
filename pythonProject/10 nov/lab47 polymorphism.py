#polymorphism
#parent class method can be called from child class method
class Animal :
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bow bow")
d=Dog()
d.sound()