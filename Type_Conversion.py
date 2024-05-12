#Type Conversion:Type Conevrsioin can be defined as the changing nature of data,i.e, converting one type of data to another type of data
print("float to int type conversion")
a=19.65
print(a)
print(type(a))
print(type(int(a)))
print("float to str type conversion")
#float to str type conversion
print(type(a))
print(type(str(a)))
print("int to float type conversion")
a=18
print(a)# It will print 18,it does not generate an error due to same var names,In py varable vales can be changed based on assignment of values
print(type(a))
print(type(float(a)))
print("int to str type conversion")
print(a)
print(type(a))
print(type(str(a)))

#Output
#float to int type conversion
# 19.65
# <class 'float'>
# <class 'int'>
# float to str type conversion
# <class 'float'>
# <class 'str'>
# int to float type conversion
# 18
# <class 'int'>
# <class 'float'>
# int to str type conversion
# 18
# <class 'int'>
# <class 'str'>