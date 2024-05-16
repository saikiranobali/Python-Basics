#Print vs Return in Python
print("\"Print Usage\"")
def function_1(a,b):
    c=a+b
    print(c)
output=function_1(10,2)
print(output)

print("\"Return Usage\"")
def function_2(x,y):
    z=x+y
    return x
output2=function_2(10,22)
print(output2)

#Output
# "Print Usage"
# 12
# None
# "Return Usage"
# 10