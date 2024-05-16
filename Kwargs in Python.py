#** kwargs=Keyword Arbitary Arguments in Python
def info(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
info(name="Rohit",team="India",age=37)
info(name="Joe Root",team="England",role="Batsman")

#Output
# name Rohit
# team India
# age 37
# name Joe Root
# team England
# role Batsman