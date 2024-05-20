#Abstraction oin Python
from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Polygon):
    def sides(self,length,breadth):
        self.length=length
        self.breadth = breadth
    def area(self):
        print("Area of Rectangle is: ",self.length*self.breadth)
    def perimeter(self):
        print("Perimeter of Rectangle is: ",(self.length+self.breadth)*2)
class Triangle(Polygon):
    def sides(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        print("Area of Triangle is: ",(self.b*self.c)*1//2)
    def perimeter(self):
        print("Perimeter of Triangle is: ",self.a+self.b+self.c)
obj1=Triangle()
obj1.sides(10,20,3)
obj1.area()
obj1.perimeter()
obj2=Rectangle()
obj2.sides(12,3)
obj2.area()
obj2.perimeter()

#Output
# Area of Triangle is:  30
# Perimeter of Triangle is:  33
# Area of Rectangle is:  36
# Perimeter of Rectangle is:  30