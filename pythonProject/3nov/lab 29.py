# self functiionality
class Car:
    name=None
    color=None
    def who_is_drive(self):
        print("I am driving",self.name)
        

tesla_obj=Car()
lambo_obj=Car()
tesla_obj.name='Tesla'
lambo_obj.name='Lamborghini'
tesla_obj.who_is_drive()
lambo_obj.who_is_drive()
