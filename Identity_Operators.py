#Identity Operators in Python
#Identity Operator Checks The Memory Locations,is returns True if locations are same else it returns False. is not returns True if locations are different else it returns False
a=5
b=6
c=5
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)
print(a is not b)
print(a is not c)

#Output
# 140712350835656
# 140712350835624
# False
# True
# True
# False
