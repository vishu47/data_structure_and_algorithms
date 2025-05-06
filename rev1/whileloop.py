def whileloop():
    count = 0
    while count < 5:
        print("number : " , count)
        count+=1       
        
# The while loop is used to execute a block of code repeatedly as long as a given condition is true.

def inputWhile(n:int = 5):
    count = 0
    while count <= n:
        print("number : ",  count , end = " ")
        count+=1

def stratEndEnd(start : int = 12, end : int = 7):
    if start > end:
        start , end = end , start
        
    while start <= end:
        print("number : ", start, end = " ")
        start+=1 


def printEvenNumber(start :int = 2 , end :int = 32):
    if start > end:
        start ,end = end, start
        
    while start <= end:
        if start % 2 ==0 :
            print("even number : ", start, end = " ")
        start+=1


def printSumOfEvenNumberFromito(i : int = 10, j : int = 1):
    if i > j :
        i , j = j , i 
    sum = 0
    while i<= j:
        if i % 2 == 0:
            sum +=i
        i+=1
    
    print("total :" , sum)    
        
        
def numberofevennumberinrange(i : int = 5674, j : int = 10983):
    c = 0
    
    if i > j:
        i , j = j , i         

    while i <= j:
        if i % 2 == 0 and i % 3 == 0:
            c += 1
        i+=1
        
    print("count : ", c)
    
    
    
def factorial(n : int = 4):
    fact = 1
    while n > 0:
        fact += n*fact
        n -=1    
    print("factorial : ", fact)
    
factorial()
# numberofevennumberinrange()    
# printSumOfEvenNumberFromito()
# printEvenNumber()
# stratEndEnd()
# whileloop()
# inputWhile()