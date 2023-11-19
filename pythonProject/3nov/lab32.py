"""
Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods
Create a Class Person , Two Objects by taking (name, age, address) Input from users and print details in the end.

"""

class car:
    name=None
    model=None
    number=None
    def start_Car(self):
        print("I am starting",self.model)
    def stop_Car(self):
        print("I am starting")
    def driving_Car(self):
        print("I am starting")
tesla_obj=car()
tesla_obj.name='Tesla'
tesla_obj.model='b4'
tesla_obj.number='88888'
tesla_obj.start_Car()
maruti_obj=car()
maruti_obj.name='Maruti'
maruti_obj.model='M3'
maruti_obj.number='M3'
maruti_obj.start_Car()


