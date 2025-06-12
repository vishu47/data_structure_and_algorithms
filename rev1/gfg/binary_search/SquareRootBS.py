def floorSqrt(): 
    n = 5
    #Your code here
    start , end = 0 , n 
    ans  = -1
    
    while start <= end :
        
        mid = (start + end)//2
        
        if mid*mid == n:
            return mid
            
        elif mid*mid > n:
            end = mid - 1
            
        else:
            ans = mid
            start = mid + 1
            
    return ans 
    
    
print(floorSqrt())