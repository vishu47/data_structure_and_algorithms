def minimuminsoertedarray():
    
    arr = [5, 6, 1, 2, 3, 4]
    
    mid = 0
    mini = float("inf")
    start , end  = 0 , len(arr) - 1
    
    while start <= end:
        mid = (start+end)//2
        
        if arr[mid] >= arr[start]:
            mini = min(mini,arr[start])
            start = mid + 1
        else:
            mini = min(mini,arr[mid])
            end = mid - 1


    return mini            
                 
        


print(minimuminsoertedarray())
