#Methods in Python
class Method:
    def __init__(self,roll,course):
        self.roll=roll
        self.course=course
    def display(self):
        print(self.roll," : ",self.course)
obj1=Method(11,"Python")
obj2=Method(12,"C")
obj3=Method(13,"Java")
obj1.display()
obj2.display()
obj3.display()

#Output
# 11  :  Python
# 12  :  C
# 13  :  Java