#Method Resolution Order in Python
# In python, method resolution order defines the order in which the base classes are searched when executing a method. First, the method or attribute is searched within a class and then it follows the order we specified while inheriting. This order is also called Linearization of a class and set of rules are called MRO(Method Resolution Order).
class BaseClass1:
    def show(self):
        print("Inside First Base Class")
class BaseClass2:
    def show(self):
        print("Inisde Second Base Class")
class DerivdeClass(BaseClass2,BaseClass1):
    def display(self):
        print("Inside Derived Class")
obj1=DerivdeClass()
obj1.show()
obj1.display()

#Output
# Inisde Second Base Class
# Inside Derived Class