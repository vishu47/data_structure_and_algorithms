def searchinsertposition():
    arr = [1,3,5,6]
    k = 5
    mid = 0
    low , high = 0 , len(arr)
    ans = len(arr)
    
    while low <= high:
        
        mid = (low + high)//2
        
        if arr[mid] >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
    
    
    
    

print(searchinsertposition())