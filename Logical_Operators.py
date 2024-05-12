#Logical operators in Python
#Logical AND Operator,it returns True if both conditions satisfies, else it returns False,Similar to Logica AND in Boolean Algebra
print("Logical AND Operator")
a=10
b=7
c=False
print(a<19 and b>3)
print(a<19 and b<3)
print(a>19 and b>3)
print(a>19 and b<3)
#Logical OR Operator it returns False if both conditions fails, else it returns True,Similar to Logica OR in Boolean Algebra
print("Logical OR Operator")
print(a<19 or b>3)
print(a<19 or b<3)
print(a>19 or b>3)
print(a>19 or b<3)
#It inverts boolean values,Similar to Logical NOT
print("Logical NOT Operator")
print(not(c))

#Output
# Logical AND Operator
# True
# False
# False
# False
# Logical OR Operator
# True
# True
# True
# False
# Logical NOT Operator
# True
