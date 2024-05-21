#Accessing Public members in Python
class Person:
    def __display(self):
        self.name = "Ramu"
        print("Name:", self.name)

obj = Person()
obj._Person__display()  # Accessing the private method using name mangling

#Output
# Name: Ramu