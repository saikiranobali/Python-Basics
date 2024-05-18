# Single Inheritance
class BaseClass1:
    def display1(self):
        self.name = "Dhoni"
        print("Name:", self.name)
class DerivedClass1(BaseClass1):
    def display2(self):
        self.age = 42
        print("Age:", self.age)
# Multilevel Inheritance
class BaseClass2:
    def display3(self):
        self.team = "India"
        print("Team:", self.team)
class DerivedClass2(BaseClass2):
    def display4(self):
        self.id = 7
        print("Jersey Number:", self.id)
class DerivedClass3(BaseClass2):
    def display5(self):
        self.role = "Captain"
        print("Role:", self.role)
# Creating an object of DerivedClass1 (Single Inheritance)
obj1 = DerivedClass1()
obj1.display1()
obj1.display2()
# Creating an object of DerivedClass3 (Multilevel Inheritance)
obj2 = DerivedClass3()
obj2.display3()
obj2.display5()
# Creating an object of DerivedClass2 (Multilevel Inheritance)
obj3 = DerivedClass2()
obj3.display3()
obj3.display4()

#Output
# Name: Dhoni
# Age: 42
# Team: India
# Role: Captain
# Team: India
# Jersey Number: 7