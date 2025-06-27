def canWePlace(arr , mid , k):
    count = 1
    last = arr[0]
    
    for i in range(1 , len(arr)):
        
        # maintaine minimum diff mid
        
        if arr[i] - last  >= mid:
            count += 1
            last = arr[i]
    
    if count >= k:
        return True
    else:
        return False    
    


def aggresivecows():
    arr = [6,4,3,16,20,7,18,10]
    k = 3
    arr = sorted(arr)
    maxi = max(arr)
    mini = min(arr)
    ans = -1
    
    # for i in range(1 , maxi - mini):
    #     if canWePlace(arr , i , k):
    #         continue
    #     else:
    #         return i - 1
    
    start , end = 1 , max(arr) - min(arr)
    mid = 0
    ans = -1
    
    while start <= end:
        
        mid = (start + end )//2
        
        if canWePlace(arr ,mid , k):
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
            
    return ans 
                
    
    
    
print(aggresivecows())