#W+ Mode in Python File Handling
f1=open("file4.txt","w+")
print(f1.tell())
f1.write("W+ Mode in File Handling")
print(f1.tell())
print(f1.seek(0))
print(f1.read())
print(f1.tell())

#Output
# 0
# 24
# 0
# W+ Mode in File Handling
# 24