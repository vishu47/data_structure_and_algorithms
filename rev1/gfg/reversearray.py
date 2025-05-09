def reversearray():
    arr = [4, 5, 2]
    l = len(arr) - 1
    for i in range(0 , len(arr)//2):
        arr[i] , arr[l] = arr[l] , arr[i]
        l-=1        
    return arr
    
print(reversearray())