#Method Overloading Arbitary Arguments in Python
class Addition:
    def add(self,*args):
        total=0
        for i in args:
            total+=i
        print(total)

obj=Addition()
obj.add(10,22)
obj.add(10,82,33,7654)
obj.add(76,43,34,234,234,213,231,5,7,8)

#Output
# 32
# 7779
# 1085