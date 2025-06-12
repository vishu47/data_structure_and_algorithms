def nthRoot() -> int:
    # Code here
    # n , m = 4 , 69
    # n , m = 2 , 9
    n , m = 3 , 9
    
    start , end = 0 , m
    ans = -1
    
    while start <= end:
        
        mid = (start + end)//2
        
        if mid**n == m:
            return mid
        
        if mid**n <= m:
            start = mid + 1
        else:
            end = mid - 1
        

    return ans	

print(nthRoot())