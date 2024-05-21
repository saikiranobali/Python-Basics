#Get() and Set() to Access Private Members without Name Mangling
class Person:
    def __init__(self,age):
        self.__age=age
    def get_age(self):
        print("Age of Person is: ",self.__age)
    def set_age(self,age):
        if age<18:
            print("Person is Minor")
        else:
            self.__age=age
            print("The Age is: ",self.__age," He is Major")
obj=Person(17)
obj.get_age()
obj.set_age(14)
obj.set_age(87)
#Output
# Age of Person is:  17
# Person is Minor
# The Age is:  87  He is Major