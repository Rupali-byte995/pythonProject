#private protected and public
class myClass:
    def __init__(self):
        self.public_var=10
        self._proc_var=20
        self.__private_var=40


obj=myClass()
print(obj.public_var)
# print(obj.__private_var)