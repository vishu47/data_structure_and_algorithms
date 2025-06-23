def Function():
    
    # arr = [4, 7, 9, 10]
    # k = 3
    arr = [6,7]
    k =  7
    
    
    start = arr[0]
    i = 0
    ans = 0
    
    while i <= len(arr) - 1:
        if start == arr[i]:
            i += 1
        else:
            ans += 1
            if ans == k:
                return start
                
        start += 1
            

    # if missing number beyond array then 
    # k - found missing number  = 
    # arr[-1] + (k - found missing number)
    if ans < k:
        return arr[-1] + (k - ans)
    
            
    return -1

            

    
    
print(Function())