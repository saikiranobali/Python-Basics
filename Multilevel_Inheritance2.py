#Multilevel Inheritance in Python
class BaseClass:
    def show(self):
        self.name = "Saikiran"
        self.age = 18
        print("Name: ",self.name)
        print("Äge: ",self.age)
class DerviedClass1(BaseClass):
    def display(self):
        self.roll = 11
        self.branch = "AIML"
        print("Roll: ",self.roll)
        print("Branch: ",self.branch)
class FinalDerviedClass(DerviedClass1):
    def print(self):
        self.marks = 9.33
        self.college = "GRIET"
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