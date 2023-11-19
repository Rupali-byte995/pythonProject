#multilevel inheritance
class gp:
    def gp_method(self):
        print("Grandfather method")
class Father(gp):
    def f_method(self):
        print("father method")
class Child(Father):
    def c_method(self):
        print("Child method")
child=Child()
child.gp_method()
child.f_method()
child.c_method()