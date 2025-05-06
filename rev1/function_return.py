def ReturnSome(num :int) -> bool:
    if(num % 2 == 0):
        return True
    else:
        return False


def ReturnSome(*num :int) -> bool:
    for i in num:
        if(i % 2 == 0):
            print(True)
        else:
            print(False)
 

x = input("Enter the number = ")

if type(x) == int:
    print("int")
if type(x) == str:
    print('str')
else:
    print(False)


if isinstance(x, int):
    print("int")
if isinstance(x, str):
    print("str")
else:
    print(False)
    
    
    
# x = int(input("Enter the number = "))
# print(ReturnSome(x))

# print(ReturnSome(2,34,45,56))