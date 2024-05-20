#Private members are accessible with  in class not outside the class also.
#Members which are  defined with double underscopre as prefix is termed as Public accesss modifiers
class Person:
    def __show(self):
        self.name="Saikiran"
        self.roll=11
        print("Name: ",self.name)
        print("Roll: ",self.roll)
obj1=Person()
obj1.show()

#Output
# obj1.show()
#     ^^^^^^^^^
# AttributeError: 'Person' object has no attribute 'show'