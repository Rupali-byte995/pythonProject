#hybrid inheritance
class A:
    def A_method(self):
        print("A method")
class B(A):
    def B_method(self):
        print("B method")
class C(A):
    def C_method(self):
        print("C method")
class D(B,C):
    def D_method(self):
        print("D method")
d=D()
d.A_method()
d.B_method()
d.C_method()
d.D_method()