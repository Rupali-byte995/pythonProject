# # single level inheritance
# class Animal:
#     def speak(self):
#         print("Animal can speak")
#
#     def drive(self):
#         print("I can drive")
#
#
# class Dog(Animal):
#     def speak(self):
#         print("Bow bow")
#         Animal().drive()
#
#
# d = Dog()
# d.speak()
# d.drive()
# another example
class Father:
    def one_bhk(self):
        print("You own it ")


class Son(Father):
   def inherit(self):
       Father().one_bhk()


s = Son()
s.inherit()
s.one_bhk()