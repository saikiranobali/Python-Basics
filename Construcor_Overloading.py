#Constructor Overloading in Python
#It is not supported in Python,but explicitly useing assigning default values we can implement.
class Person:
    def __init__(self,name,age=None):
        self.name=name
        self.age=age
person1=Person("Alice")
person2=Person("Bob",25)
print(person1.name,person1.age)
print(person2.name,person2.age)

#Output
#Alice None
#Bob 25