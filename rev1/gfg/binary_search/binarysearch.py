def SearchXinsortedarray():
    arr = [1,1,1,2,2,3,3,3,3,3,3,4,4,4,5,5,5]
    target = 3
    # arr = [ 2, 3, 4, 10, 40 ]
    # target = 10
    # arr =  [-1,0,3,5,9,12]
    # target = 9
    mid = 0
    result = -1
    start , end = 0 , len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] > target:
            end = mid - 1
        
        elif arr[mid] < target:
            start = mid +1
        
        else:
            result = mid
            end = mid - 1
            
    return result

print(SearchXinsortedarray())