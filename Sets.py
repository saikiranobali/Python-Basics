#Sets in Python
s1={"Saikiran",18,45,"Ammu",18.45}#Basic Creation
s2=set([12,23,45,6,7])# By set()
print(s2)
print(s1)
print(type(s1))
print(len(s2))
#Method Implementation of sets
s1.add(8)
print(s1)
s1.remove(8)
print(s1)
print(s1.union(s2)) #print(s1|s2)
print(s1.intersection(s2))#print(s1&s2)
print(s1.difference(s2))#print(s1-s2)
print(s1.symmetric_difference(s2))#print((s1^s2))

#Output
# {6, 7, 12, 45, 23}
# {18, 18.45, 'Saikiran', 'Ammu', 45}
# <class 'set'>
# 5
# {18, 18.45, 'Saikiran', 'Ammu', 8, 45}
# {18, 18.45, 'Saikiran', 'Ammu', 45}
# {6, 7, 12, 45, 18, 18.45, 'Saikiran', 23, 'Ammu'}
# {45}
# {'Ammu', 18, 18.45, 'Saikiran'}
# {6, 7, 12, 18, 18.45, 23, 'Saikiran', 'Ammu'}