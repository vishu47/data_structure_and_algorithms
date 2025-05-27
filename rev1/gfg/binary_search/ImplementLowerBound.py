def ImplementLowerBound():
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 11
    # target = 9
    # lower bound will be 1
    mid = 0
    low = 0 
    high = len(arr) -1
    ans = len(arr)
    # arr[mid] >= target ley point
    
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] >= target:
            ans = mid
            # wee need minimu so will search in left space
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
                 
       
print(ImplementLowerBound())