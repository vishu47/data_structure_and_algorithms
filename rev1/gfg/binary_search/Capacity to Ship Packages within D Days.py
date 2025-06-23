def requiredDays(arr , cap):
    
    load = 0
    days = 1
    
    for wt in arr:
        if wt + load > cap:
            days += 1
            load = wt
        else:
            load += wt
            
    return days
        

def capacityFind():
    
    arr = [1,2,3,4,5,6,7,8,9,10]
    d = 1
    # arr = [5,4,5,2,3,4,5,6]
    # d = 5
    
    start =  float("-inf") 
    end =  0
    
    for i in arr:
        start = max(start , i)
        end += i
        
        
    while start <= end:
        mid = (start + end)//2
        
        if requiredDays(arr , mid) <= d:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return ans
        
    print(start , end)
    
    
    
    
print(capacityFind())