class Person:
    def __init__(self, name):
        self.name = name

    def print_my_name(self):
        print("My name is", self.name*3)


amit = Person("amit")
anubhav = Person("anubhav")
amit.print_my_name()
