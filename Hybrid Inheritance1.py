# Single Inheritance
class BaseClass1:
    def __init__(self):
        self.name = "Dhoni"

    def display1(self):
        print("Name:", self.name)


class DerivedClass1(BaseClass1):
    def __init__(self):
        super().__init__()
        self.age = 42

    def display2(self):
        print("Age:", self.age)


# Multilevel Inheritance
class BaseClass2:
    def __init__(self):
        self.team = "India"

    def display3(self):
        print("Team:", self.team)


class DerivedClass2(BaseClass2):
    def __init__(self):
        super().__init__()
        self.id = 7

    def display4(self):
        print("Jersey Number:", self.id)


class DerivedClass3(BaseClass2):
    def __init__(self):
        super().__init__()
        self.role = "Captain"

    def display5(self):
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