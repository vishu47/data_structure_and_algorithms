def arraysearch():
    arr = [1, 2, 3, 4]
    x = 3
    for i in range(0 , len(arr)):   
        print(arr[i] ,x)
        if arr[i] == x:
            return i
        
    return -1
    
print(arraysearch())