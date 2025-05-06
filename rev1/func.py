def passFunc():
    pass

# scoping variable can not exccess ouside the function

def scoping():
    name = "vishnu "
    surname = "maurya"
    print(name + surname)

def addage():
    age = 90
    print("age : {age}")


def avg(a :int,b:int,c:int):
    print((a+b+c))

# keyword arguments
def subMarks(phy:int,eng:int,hindi:int):
    print(phy,eng,hindi , end = " ")



subMarks(90,hindi = 80,eng = 88)
subMarks(eng=90,hindi = 80,phy = 88)
# avg(1,2,4)
# avg('vishnu ',"kumar ","maurya")
# scoping()
# addage()
# passFunc()