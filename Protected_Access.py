#Protected members are accessible with  in class and outside the class but using inheritance only.
#Members which are defined with single underscopre as prefix is termed as Protected accesss modifiers
class Person:
    def _show(self):
        self.name="Saikiran"
        self.roll=11
        print("Name: ",self.name)
        print("Roll: ",self.roll)
class Sub(Person):
    def display(self):
        self._show()
        self.branch="AIML"
        self.clg="GRIET"
        print("Branch: ",self.branch)
        print("College: ",self.clg)
obj1=Sub()
obj1.display()

#Output
# Name:  Saikiran
# Roll:  11
# Branch:  AIML
# College:  GRIET