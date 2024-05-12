#Fstrings in Python,They allow you to embed expressions inside string literals, which are then evaluated at runtime. F-strings are prefixed with an 'f' or 'F' and curly braces {} are used to evaluate expressions.
name = "Saikiran"
branch="Computer Science & Machine Learning"
clg="Gokaraju Rangaraju Institute of Engineering & Technology"
# Using f-string to format a string
message = f"Hello, my name is {name} I'm pursuing Btech in {branch} at {clg}."
print(message)

#Output
#Hello, my name is Saikiran I'm pursuing Btech in Computer Science & Machine Learning at Gokaraju Rangaraju Institute of Engineering & Technology.