#R+ in File Handling
f1=open("file3","r+")
print(f1.read())
f1.write("R+ Mode in File Handling in Python ")
print(f1.read())
print(f1.tell())

#Output
#File3:R+ Mode in File Handling in Python
#34