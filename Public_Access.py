#Public members are accessible with  in class and outside the class also.
#Members which are not defined with underscopre as prefix is termed as Public accesss modifiers
class Person:
    def show(self):
        self.name="Saikiran"
        self.roll=11
        print("Name: ",self.name)
        print("Roll: ",self.roll)
obj1=Person()
obj1.show()

#Output
# Name:  Saikiran
# Roll:  11