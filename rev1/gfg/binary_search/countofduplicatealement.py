def fisrtOcc(arr , target):
    mid = 0 
    start , end = 0 , len(arr) - 1
    ans = -1
    
    while start <= end:
        
        mid = (start + end ) // 2
        
        if arr[mid] == target:
            ans = mid
            end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return ans
    
def lastOcc(arr , target):
    mid = 0 
    start , end = 0 , len(arr) - 1
    ans = -1
    
    while start <= end:
        
        mid = (start + end ) // 2
        
        if arr[mid] == target:
            ans = mid
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return ans


# def countFreq(arr = [1,1,2,2,2,2,3], target = 4):
def countFreq(arr = [8, 9, 10, 12, 12, 12], target = 12):
    #code here
    fist = fisrtOcc(arr , target)
    last = lastOcc(arr , target)
    print(fist, last)
    
    if fist == -1:
        return 0
    else:
        return last - fist + 1

print(countFreq())