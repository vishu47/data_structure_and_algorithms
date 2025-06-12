def peakelement():
    # arr = [-1]
    arr = [1,2,3]
    # arr = [1, 2, 4, 5, 7, 8, 3]
    # arr = [10, 20, 15, 2, 23, 90, 80]
    
    # for i in range(1 , len(arr) - 1):
    #     if arr[i] > arr[i - 1] and arr[i] > arr[i+1]:
    #         return True
    # return False
    n = len(arr)
    start , end = 1 ,len(arr) - 2 
    
    if n == 1: return True
    
    if arr[0] > arr[1] or arr[n - 1] > arr[n - 2]:
        return True
        
    while start <= end:
        mid = (start + end)//2
        
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            # return True
            return arr[mid]
        elif arr[mid] > arr[mid - 1] :
            start = mid + 1
        elif arr[mid] > arr[mid + 1] :
            end = mid - 1
        # fort multiple peaks this else will work
        else:
            start = mid + 1 
            
            
    return False
    
    
    
print(peakelement())