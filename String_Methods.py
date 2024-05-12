# Basic String Methods in Pytjhon
s="saikiran"
s1="Rohit"
s2="   Virat      "
print(s.endswith('k'))
print(s.startswith('s'))
print(s.capitalize())
print(s.split()) #Converts into a list of element
print(s.count('a'))
print(s1.casefold()) #Similar to lower() method
print(s2.strip()) # Removes extra spaces
print(s1.index('i'))
print(s1.center(10,'7'))
print(s1.lower())
print(s1.upper())
print(s.encode()) #It encodes str into bytes,if no encoding is specified it uses UTF-8 encoding format
print(s.replace('n','m'))
print(len(s))
print(s.swapcase())
print(s.isalnum())
print(s.isalpha())
print(s.isascii())
print(s.isdigit())
print(s.isdecimal())
print(s.isnumeric())
print(s.title())

#Output
# False
# True
# Saikiran
# ['saikiran']
# 2
# rohit
# Virat
# 3
# 77Rohit777
# rohit
# ROHIT
# b'saikiran'
# saikiram
# 8
# SAIKIRAN
# True
# True
# True
# False
# False
# False
# Saikiran