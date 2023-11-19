#abstract class(ABC) and abstract base method
from abc import ABC,abstractmethod
class Animal(ABC):
  @abstractmethod
  def sound(self):
   pass
class Dog(Animal):
 def sound(self):
  print("bow bow")
d=Dog()
d.sound()