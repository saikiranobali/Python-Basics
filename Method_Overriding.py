#Method Overriding in Python
class Super:
    def display(self):
        print("Method in Super Class")
class Sub(Super):
    def display(self):
        super().display()
        print("Method in Sub Class")
obj=Sub()
obj.display()

#Output
# Method in Super Class
# Method in Sub Class