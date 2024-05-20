#Abstact Class using ABC module
from abc import ABC,abstractmethod
class One(ABC):
    @abstractmethod
    def display1(self):
        pass
class Two(One):
    def display1(self):
        print("Inside Class Two")
class Three(One):
    def display1(self):
        print("Inside Class Three")
obj1=Two()
obj2=Three()
obj1.display1()
obj2.display1()
#Output
# Inside Class Two
# Inside Class Three