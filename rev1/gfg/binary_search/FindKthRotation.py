def FindKthRotation():
    arr = [5, 1, 2, 3, 4]
    
    start , end = 0 , len(arr) - 1
    index = -1
    mini = float('inf')
    
    while start <= end:
        mid = (start + end)//2
        
        if arr[mid] >= arr[start]:
            # mini = min(mini,arr[start])
            if arr[start] <= mini:
                mini = arr[start]
                index = start
            start = mid + 1
        else:
            # mini = min(arr[mid] , mini)
            if arr[mid] <= mini:
                mini = arr[mid]
                index = mid
            end = mid - 1

    return index


print(FindKthRotation())
            
    