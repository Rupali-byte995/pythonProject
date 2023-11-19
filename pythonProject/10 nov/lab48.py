#default method
class Mathutil:
    def add(self,a,b=0,c=0):
        return a+b+c


obj1=Mathutil()
print(obj1.add(1))
print(obj1.add(2,3))
