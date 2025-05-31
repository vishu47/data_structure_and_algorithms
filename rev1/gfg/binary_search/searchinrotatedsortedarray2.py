def searchinrotatedsortedarray():
    # arr = [2, 5, 6, 0, 0, 1, 2]
    # k = 3
    arr = [3,1,2,3,3,3,3]
    k = 3
    
    mid = 0
    start , end = 0 , len(arr)-1
    
    while start <= end:
        mid = (start + end)//2
        
        if arr[mid] == k:
            ans = mid
            return True
        
        if arr[mid] > arr[start]:
            if k >= arr[start] and k < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
        else:
            if k > arr[mid] and k <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
                
    return False
                
print(searchinrotatedsortedarray())