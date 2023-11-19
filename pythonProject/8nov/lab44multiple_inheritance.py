#multiple inheritance
class A:
    def A_money(self):
        print("A money")
class B:
    def B_money(self):
        print("B money")
class Son(A,B):
    pass
s=Son()
s.A_money()
s.B_money()