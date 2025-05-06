def ifels():
    age = int(input('Enter the ege = '))
    if age >= 18 and age < 60:
        print("Adult")
    elif age < 18:
        print("child")
    elif age >= 60:
        print("Old")
    else:
        print('no one')
        
        
        
def lengthofarr():
    arr = []
    while len(arr) < 4:
        a = int(input("Push number in arra = "))
        arr.append(a)
    
    if(len(arr) > 0):
        return True
    else:
        return False
    
print(lengthofarr())    
    
    
    
    
# ifels()
