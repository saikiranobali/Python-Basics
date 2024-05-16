#Loop Control Statements
#These are used to control flow of execution
print("\"Break Statement\"")
numbers=[1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)
    if number==5:
        break
print("\"Continue Statement\"")
numbers=[1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if number==5:
        continue
    print(number)
print("\"Pass Statement\"")
for i in range(5):
    pass
#Returns nothing

#Output
# "Break Statement"
# 1
# 2
# 3
# 4
# 5
# "Continue Statement"
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# "Pass Statement"