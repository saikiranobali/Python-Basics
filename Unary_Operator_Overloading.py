#Unary Operator Overloading in Python
class Unary:
    def __init__(self,x):
        self.x=x
    def __pos__(self):
        return Unary(+self.x)
    def __invert__(self):
        return ~self.x
    def __neg__(self):
        return Unary(-self.x)
    def __abs__(self):
        return Unary(abs(self.x))
    def __int__(self):
        return Unary(int(self.x))
    def __complex__(self):
        return complex(self.x)
obj=Unary(18)
print(+obj.x)
print(-obj.x)
print(~obj.x)
print(abs(obj.x))
print((int(obj.x)))
print((complex(obj.x)))

# #Output
# 18
# -18
# -19
# 18
# 18
# (18+0j)