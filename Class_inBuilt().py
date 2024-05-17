#Built in Functions of Class in Python
class Constructor:
    def __init__(self,name,role,id):
        self.name=name
        self.role=role
        self.id=id
obj1=Constructor("Bumrah","Bowler",93)
obj2=Constructor("Rahul","Keerper Batsman",1)
print(obj2.role)
print(obj1.role)
#Inbuilt Functions of Class
print(getattr(obj1,"id"))
setattr(obj2,"role","Vice Captain")
print(getattr(obj2,"role"))
print(hasattr(obj1,"jersey"))

#Output
# Keerper Batsman
# Bowler
# 93
# Vice Captain
# False