def findfloorinarray():
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 5
    
    mid = 0
    low , high = 0 , len(arr) - 1
    ans = -1
    
    while low <= high:
        
        mid = (low+high)//2
        
        if arr[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
            
    
    
    
print(findfloorinarray())