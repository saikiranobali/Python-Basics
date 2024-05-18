#Multiple Inheritance in Python
class BaseClass1:
    def __init__(self):
        self.name="Virat"
        self.jersey_no=18
    def display1(self):
        print("Name: ",self.name)
        print("Jersey No: ",self.jersey_no)
class BaseClass2:
    def __init__(self):
        self.team="India"
        self.skill="Right Handed Batsman"
    def display2(self):
        print("Team: ",self.team)
        print("Skill: ",self.skill)
class Derived(BaseClass1,BaseClass2):
    def __init__(self):
        BaseClass1.__init__(self)
        BaseClass2.__init__(self)
        self.franchise_team="Royal Challengers Bangalore"
        self.nickname="Chiku"
    def show(self):
        print("Franchise Team: ",self.franchise_team)
        print("Nick Name: ",self.nickname)
obj1=Derived()
obj1.display1()
obj1.display2()
obj1.show()

#Output
# Name:  Virat
# Jersey No:  18
# Team:  India
# Skill:  Right Handed Batsman
# Franchise Team:  Royal Challengers Bangalore
# Nick Name:  Chiku
