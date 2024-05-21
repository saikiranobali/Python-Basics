#Method Overloading in Python 
from multipledispatch import dispatch

@dispatch(int, int, int)
def add(a, b, c):
    print(a + b + c)

@dispatch(int, float)
def add(a, b):
    print(a + b)

@dispatch(str, str)
def add(a, b):
    print(a + b)

# Testing the overloaded functions
add(10, 18.99)                  # Should print 28.99
add(10, 20, 33)                 # Should print 63
add("Sunrisers ", "Hyderabad")  # Should print "Sunrisers Hyderabad"

#Output
#8.99
#63
#Sunrisers Hyderabad
