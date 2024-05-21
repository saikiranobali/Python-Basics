#A+ Mode in Python File Handling
f1=open("file.txt","a+")
print(f1.tell())
print(f1.seek(0))
print(f1.read())
f1.write(" A+ Mode")
print(f1.tell())
print(f1.seek(0))
print(f1.read())

#Output
# 81
# 0
# Hello,Welcome to Python File Handling Appended Part of File Appended Part of File
# 89
# 0
# Hello,Welcome to Python File Handling Appended Part of File Appended Part of File A+ Mode
