def ceilinsortedarray():
    arr = [1, 2, 8, 10, 11, 12, 19]
    x = 5
    mid = 0
    start, end = 0 , len(arr) - 1
    ans = -1
    while start <= end:
        mid = (start+end)//2
        
        if arr[mid] >= x:
            ans = mid
            end = mid - 1
            
        else:
            start = mid + 1
            
    return ans
    
    



print(ceilinsortedarray())