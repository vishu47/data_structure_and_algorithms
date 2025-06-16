def totalHrs(arr , mid):
    print(mid)
    total = 0
    
    for i in arr:
        # simulate ceil value of i // mid   
        total += (i + mid - 1) // mid 
    
    return total
    

def kokoeatingbanan():
    h = 8
    # arr = [3,6,7,11]
    # h = 4
    # arr = [5,10,3]
    h = 10
    arr = [3, 4]
    maxi = 0
    ans = 0
    for i in arr:
        maxi = max(maxi , i)
    # note start will laways 1 because it should be one hours minimum
    start , end = 1 , maxi
    
    while start <= end:
        mid = (start + end)//2 
        
        totalhours = totalHrs(arr, mid)
        
        if totalhours <= h:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return ans           
        
    


print(kokoeatingbanan())