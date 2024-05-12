#Dictionaries in Python
d1={18:"Virat",7:"Dhoni",9:"Manish",45:"Rohit",93:"Bumrah"}#basic Creation
d2=dict({1:1234,2:2345,3:3456,4:4567,5:5678,6:6789,7:7890})##Using dict()
print(type(d2))
print(len(d1))
print(len(d2))
#Method Implemetation of Dictionaries
d1[18]="Smriti Mandanna"#Updation of elements
print(d1)
d1[17]="Rishabh"#Adding Elements
print(d1)#Deletion of Elements
d1.pop(9)
print(d1)
d1.popitem()
print(d1)
#Basic Built_in Functions
print(d1.keys())
print(d1.items())
print(d1.values())

#Output
# <class 'dict'>
# 5
# 7
# {18: 'Smriti Mandanna', 7: 'Dhoni', 9: 'Manish', 45: 'Rohit', 93: 'Bumrah'}
# {18: 'Smriti Mandanna', 7: 'Dhoni', 9: 'Manish', 45: 'Rohit', 93: 'Bumrah', 17: 'Rishabh'}
# {18: 'Smriti Mandanna', 7: 'Dhoni', 45: 'Rohit', 93: 'Bumrah', 17: 'Rishabh'}
# {18: 'Smriti Mandanna', 7: 'Dhoni', 45: 'Rohit', 93: 'Bumrah'}
# dict_keys([18, 7, 45, 93])
# dict_items([(18, 'Smriti Mandanna'), (7, 'Dhoni'), (45, 'Rohit'), (93, 'Bumrah')])
# dict_values(['Smriti Mandanna', 'Dhoni', 'Rohit', 'Bumrah'])
