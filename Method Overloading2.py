#Method Overloading Using Default Arguments in Python
class Addition:
    def add(self,x,y):
        print(x+y)

    def add(self, x,y,z=0):
        print(x + y+z)
obj=Addition()
obj.add(10,22)
obj.add(10,82,33)

#Output
# 32
# 125