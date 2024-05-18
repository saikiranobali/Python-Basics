#Supe() is used to refer super class methods from sub class
class Super:
    def __init__(self):
        self.name="Saikiran"
    def display(self):
        print("Name: ",self.name)
class Sub(Super):
    def __init__(self):
        super().__init__()
        self.id=11
    def show(self):
        print("Roll: ",self.id)
obj1=Sub()
obj1.display()
obj1.show()

#Output
# Name:  Saikiran
# Roll:  11