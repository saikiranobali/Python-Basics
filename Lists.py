#List and List methods in Python
list1=["Virat",18,45,"Dhoni",7,"Sunrisers","Arjun",10.8]
list2=["Sai","Dhoni","Yellow","Black","Orange","White"]
list3=[32,35,54,76,98798,6,5]
print(list1)
print(type(list1))
#len()
print(len(list1))
print(list1[-3])
print(list1[1:5])
print(list1[:])
print(list1[1:5:2])
#Append() method
list1.append('R')
print(list1)
#insert()
list1.insert(2,22)
print(list1)
#extend()
list1.extend([17,"Rishabh"])
print(list1)
list1.remove(22)
print(list1)
#pop()
list1.pop()
print(list1)
print(list1.pop(3))#returns element of index 3 (Dhoni)
print(list1)
#index()
print(list1.index(45))
#count()
print(list1.count(70))
print(list1.count(7))
#sort()
list2.sort()
print(list2)
#min() & max()
print(min(list2))
print(max(list2))
print(min(list3))
print(max(list3))
#reverse()
print(list1.reverse())
list1.reverse()
list2.reverse()
list3.reverse()
print(list1)
print(list2)
print(list3)
#clear()
list3.clear()
print(list3)

#Output
# ['Virat', 18, 45, 'Dhoni', 7, 'Sunrisers', 'Arjun', 10.8]
# <class 'list'>
# 8
# Sunrisers
# [18, 45, 'Dhoni', 7]
# ['Virat', 18, 45, 'Dhoni', 7, 'Sunrisers', 'Arjun', 10.8]
# [18, 'Dhoni']
# ['Virat', 18, 45, 'Dhoni', 7, 'Sunrisers', 'Arjun', 10.8, 'R']
# ['Virat', 18, 22, 45, 'Dhoni', 7, 'Sunrisers', 'Arjun', 10.8, 'R']
# ['Virat', 18, 22, 45, 'Dhoni', 7, 'Sunrisers', 'Arjun', 10.8, 'R', 17, 'Rishabh']
# ['Virat', 18, 45, 'Dhoni', 7, 'Sunrisers', 'Arjun', 10.8, 'R', 17, 'Rishabh']
# ['Virat', 18, 45, 'Dhoni', 7, 'Sunrisers', 'Arjun', 10.8, 'R', 17]
# Dhoni
# ['Virat', 18, 45, 7, 'Sunrisers', 'Arjun', 10.8, 'R', 17]
# 2
# 0
# 1
# ['Black', 'Dhoni', 'Orange', 'Sai', 'White', 'Yellow']
# Black
# Yellow
# 5
# 98798
# None
# ['Virat', 18, 45, 7, 'Sunrisers', 'Arjun', 10.8, 'R', 17]
# ['Yellow', 'White', 'Sai', 'Orange', 'Dhoni', 'Black']
# [5, 6, 98798, 76, 54, 35, 32]
# []