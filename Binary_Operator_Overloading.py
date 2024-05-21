#Binary Operator Overloading in Python
class Binary:
    def __init__(self,a):
        self.a=a
    def __add__(self, other):
        return self.a+other.a
obj1=Binary(10)
obj2=Binary(11)
obj3=Binary("Rohit")
obj4=Binary(" Sharma")
print(obj1+obj2)
print(obj3+obj4)

#Output
# 21
# Rohit Sharma