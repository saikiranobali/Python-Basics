#Hierarchical Inheritance in Python
class BaseClass1:
    def display1(self):
        self.name = "Rohit"
        self.role = "Captain"
        print("Name: ",self.name)
        print("Role: ",self.role)
class Derivedclass1(BaseClass1):
    def display2(self):
        self.team = "India"
        self.jersey_no = 45
        print("Name: ",self.team)
        print("Role: ",self.jersey_no)
class DerivedClass2(BaseClass1):
    def display3(self):
        self.age = 37
        self.skill = "Right Handed Batsman"
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