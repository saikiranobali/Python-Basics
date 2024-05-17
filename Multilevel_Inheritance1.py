#Multilevel Inheritance in Python
class BaseClass:
    def __init__(self):
        self.name="Saikiran"
        self.age=18
    def show(self):
        print("Name: ",self.name)
        print("Äge: ",self.age)
class DerviedClass1(BaseClass):
    def __init__(self):
        super().__init__()
        self.roll=11
        self.branch="AIML"
    def display(self):
        print("Roll: ",self.roll)
        print("Branch: ",self.branch)
class FinalDerviedClass(DerviedClass1):
    def __init__(self):
        super().__init__()
        self.marks=9.33
        self.college="GRIET"
    def print(self):
        print("Marks: ",self.marks)
        print("College: ",self.college)
obj1=FinalDerviedClass()
obj1.show()
obj1.display()
obj1.print()

#Output
# Name:  Saikiran
# Äge:  18
# Roll:  11
# Branch:  AIML
# Marks:  9.33
# College:  GRIET