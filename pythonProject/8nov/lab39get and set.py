# getter and setter
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def print_details(self):
        print("Your details", self.__name, self.__age)


p = Person("Amit", 25)
p.print_details()
name = p.get_name()
p.set_name("Pramod")
p.print_details()
