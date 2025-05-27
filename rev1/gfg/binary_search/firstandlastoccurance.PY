def FirstSearch(arr, k):
    mid = 0
    ans = -1
    start, end = 0 , len(arr) - 1
    
    while start <= end:
        
        mid = (start + end)//2
        
        if arr[mid] == k:
            ans = mid
            end = mid - 1 
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
            
    return ans
    
    
def LastSearch(arr, k):
    mid = 0
    start , end = 0 , len(arr)
    ans = -1
    while start <= end:
        mid = (start + end)//2
        
        if arr[mid] == k:
            ans = mid
            start = mid + 1
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
            
            
    return ans


def firstandlastoccurance():
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    x = 5
    
    
    fist = FirstSearch(arr , x)
    last = LastSearch(arr , x)
    
    return [fist , last]
    
    
print(firstandlastoccurance())