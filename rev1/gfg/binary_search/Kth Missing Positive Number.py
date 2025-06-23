def function():
    
    arr = [2,3,4,7,11]
    k = 5
    
    # brute force
    # for i in arr:
    #     if i < k:
    #         k+=1
    #     else:
    #         break
        
    # return k

    # optimal BS
    
    start , end = 0 , len(arr) - 1
    missingNumber = 0
    ans = 0
    while start <= end:
        
        mid = (start+end)//2
        
        missingNumber = arr[mid] - (mid + 1)
        
        if missingNumber <= k:
            start = mid + 1
        else:
            end = end - 1
    
    return end + 1 + k
    
    


print(function())