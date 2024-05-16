#While Else Loop in Python
count=1
while count<=5:
    print(count)
    count+=1
else:
    print("Else Block In While Else Loop")

#Working of Else When Loop Terminated
print("\"While Else When Loop Termination Occurs\"")
count=1
while count<=5:
    print(count)
    count+=1
    if count==3:
        break
else:
    print("Else Block In While Else Loop")

#Output
# 1
# 2
# 3
# 4
# 5
# Else Block In While Else Loop
# "While Else When Loop Termination Occurs"
# 1
# 2