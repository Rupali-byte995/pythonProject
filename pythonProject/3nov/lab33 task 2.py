# Create a Class Person , Two Objects by taking (name, age, address) Input from users and print details in the end.
class Person:
    name = None
    age = None
    gender = None

    def person_details(self):
        print("Person details", self.name, self.age, self.gender)


p1_obj = Person()
p2_obj = Person()
person_name = input("Eneter person name")
person_age = int(input("Eneter person age"))
person_gender = input("Eneter person gender")
p1_obj.name = person_name
p1_obj.age = person_age
p1_obj.name = person_gender
p1_obj.person_details()
person_name = input("Eneter person name")
person_age = int(input("Eneter person age"))
person_gender = input("Eneter person gender")
p2_obj.name = person_name
p2_obj.age = person_age
p2_obj.gender = person_gender
p2_obj.person_details()
