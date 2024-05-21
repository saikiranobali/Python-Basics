#Comparision Operator Overloading in Python
class Comparision:
    def __init__(self,x):
        self.x=x
    def __gt__(self, other):
        if self.x>other.x:
            return  True
        else:
            return False
obj1=Comparision(100)
obj2=Comparision(190)
if obj1>obj2:
    print(obj1.x,"is Greater Than ",obj2.x)
else:
    print(obj2.x, "is Greater Than ", obj1.x)

#Output
# 190 is Greater Than  100