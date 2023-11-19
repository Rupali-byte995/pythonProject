#take input from user  and print the car details

class Car:
    name=None
    model=None
    def my_car_details(self):
        print ("My car etails are ",self.name,self.model)
car_name=input("Enter car name")
car_model=input("Enter car model")
my_car=Car()

my_car.name=car_name
my_car.model=car_model
my_car.my_car_details()

