#parameterised constructor
class Car:
    def __init__(self,model,make):
        self.model=model
        self.make=make

    def start_Car(self):
        print("I own the car ",self.model,self.make)

car1=Car("Toyo","Maruti")
car2=Car("lambo","9000")
car1.start_Car()
car2.start_Car()