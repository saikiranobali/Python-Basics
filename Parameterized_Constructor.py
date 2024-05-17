#Parameterized Constructor in Python
class ParameterizedConstructor:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
obj1=ParameterizedConstructor("Saikiran","AIML")
obj2=ParameterizedConstructor("Abhilash","CSE")
print(obj1.name)
print(obj2.name)

#Output
#Saikiran
#Abhilash