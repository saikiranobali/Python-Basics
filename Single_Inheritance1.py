# # Single Inheritance In Python
class BaseClass:
    def __init__(self):
        self.name = "Saikiran"
        self.roll = 11

    def display1(self):
        print("Name: ", self.name)
        print("Roll: ", self.roll)

# Define the DerivedClass inheriting from BaseClass
class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()  # Initialize attributes of BaseClass
        self.branch = "AIML"
        self.marks = 9.33

    def display2(self):
        print("Branch: ", self.branch)
        print("Marks: ", self.marks)

# Create an object of DerivedClass and test the methods
obj1 = DerivedClass()
obj1.display1()
obj1.display2()

#Output
# Name:  Saikiran
# Roll:  11
# Branch:  AIML
# Marks:  9.33