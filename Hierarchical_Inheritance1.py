#Hierarchical Inheritance in Python
class BaseClass1:
    def __init__(self):
        self.name="Rohit"
        self.role="Captain"
    def display1(self):
        print("Name: ",self.name)
        print("Role: ",self.role)
class Derivedclass1(BaseClass1):
    def __init__(self):
        super().__init__()
        self.team="India"
        self.jersey_no=45
    def display2(self):
        print("Name: ",self.team)
        print("Role: ",self.jersey_no)
class DerivedClass2(BaseClass1):
    def __init__(self):
        super().__init__()
        self.age=37
        self.skill="Right Handed Batsman"
    def display3(self):
        print("Age: ",self.age)
        print("Skill: ",self.skill)
obj2=DerivedClass2()
obj1=Derivedclass1()
obj1.display1()
obj1.display2()
obj2.display1()
obj2.display3()

#Output
# Name:  Rohit
# Role:  Captain
# Name:  India
# Role:  45
# Name:  Rohit
# Role:  Captain
# Age:  37
# Skill:  Right Handed Batsman