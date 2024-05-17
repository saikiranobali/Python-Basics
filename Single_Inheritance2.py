#Single Inheritance in Python without super
class BaseClass:
    def display(self):
        self.name="Saikiran"
        self.roll=11
        print("Name: ",self.name)
        print("Roll: ",self.roll)
class DerivedClass(BaseClass):
    def show(self):
        self.gpa=9.44
        self.branch="AIML"
        print("Branch: ",self.branch)
        print("GPA: ",self.gpa)
obj1=DerivedClass()
obj1.display()
obj1.show()