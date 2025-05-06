def greet():
    print("Hello, World!")
    

def getName():
    name = input("Enter your name : ") 
    print(name)


def login():
    username = input("Enter your username : ") 
    password = input("Enter your password : ")
    while password.isnumeric() == False:
        print("Enter again...")
        password = input("Enter your password : ")

    while username == "vishnu" and int(password) == 1111:
        print("Logged in successfully")
        break
    else:
        print("Somethimh went wrong please try again...")
        login()
        
        
def keyWordArguments(name , age , course, location):
    # you can send argument with name in the end not before the only value
    print(name , age , course, location)
    
        
        
'''
*args: This is used to pass a variable number of non-keyworded arguments to a function. It collects these arguments into a tuple. 
**kwargs: This is used to pass a variable number of keyword arguments to a function. It collects these arguments into a dictionary. 
'''
def keyWordArgumentsWithargsAndKwargs(*args, **kwargs):
    # you can send argument with name in the end not before the only value
    print(args , kwargs)
    
        
# greet()
# getName()
# login()
# keyWordArguments("Vishnu", 20, location = "BCA", course = "India")
keyWordArgumentsWithargsAndKwargs("Vishnu", 20, location = "BCA", course = "India")