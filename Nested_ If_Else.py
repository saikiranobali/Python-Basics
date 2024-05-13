#Nested If Else and Elif in Python
height=int(input("Enter Your Height in Feets:"))
if height>=3:
    print("It Sounds Good..You Can Ride ")
    age=int(input("What is Your Age:"))
    if age<10:
        print("Really Nice.. You Have To Pay $20")
    elif age>18 and age==30:
        print("My Friend... You have to pay $35 ")
    else:
        print("Dear... You have to pay $45 ")
else:
    print("Sorry Mate.. You Can't Ride!!!")

#Output
# Enter Your Height in Feets:5
# It Sounds Good..You Can Ride
# What is Your Age:27
# Dear... You have to pay $45