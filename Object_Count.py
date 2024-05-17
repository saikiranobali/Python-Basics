#Counting number of objects of a class
class ObjectCount:
    count=0
    def __init__(self):
        ObjectCount.count=ObjectCount.count+1
obj1=ObjectCount()
obj2=ObjectCount()
obj3=ObjectCount()
print("Objcet Count is :",ObjectCount.count)

#Output
#Objcet Count is : 3