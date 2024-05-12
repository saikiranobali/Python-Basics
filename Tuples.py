#Tuples in python
t=(45,43,54,67,"Patrick",18.45,"James")
t1=(63,43,324,53,5,82,8,564,423)
print(type(t))
print(t)
#Accessing Tuple Elements
print(t[1])#Indexing
print(t[-3])#Negative Indexing
print(t[1:4])#Slicing
#Tuple Method Implementation
print(t.count(45))
print(t.count(9876))
print(t.index((43)))
print(len(t))
print(sorted(t1))
print(max(t1))
print(min(t1))
print(sum(t1))

#Output
# <class 'tuple'>
# (45, 43, 54, 67, 'Patrick', 18.45, 'James')
# 43
# Patrick
# (43, 54, 67)
# 1
# 0
# 1
# 7
# [5, 8, 43, 53, 63, 82, 324, 423, 564]
# 564
# 5
# 1565