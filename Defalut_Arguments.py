#Default Arguments
def addition(a=18,b=2,c=8,d=6):
    #Function Defination
    total=a+b+c+d
    print(total)
addition(10,29,6) # User not provided d value,so default value 6 will be assigned to variable d as function defination
addition(3,4)
addition(11)
#Output
#51
#21
#27