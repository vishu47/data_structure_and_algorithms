def LongestSubarraywithSumK():
    
    arr = [94,-33,-13,40,-82,94,-33,-13,40,-82]
    k = 52
    # arr = [10,5,2,7,1,-10]
    # k = 15
    # l = 0
    
    # for i in range(0 ,len(arr)):
    #     sum = 0
    #     for j in range(i , len(arr)):
    #         sum += arr[j] 
    #         if sum == k:
    #             l = max(l,j - i + 1) 
    # return l
    
    
    '''
    using hashed map will add in sum and look for x-k in map if exist then check for maxlenth and update
    '''
    pre_sum = {}
    l = 0
    sum = 0
    
    for i in range(0 , len(arr)):
        sum += arr[i]
        
        if sum == k:
            l = i + 1  
        
        if sum - k in pre_sum:
            l  = max(l ,i - pre_sum[sum - k])
            
        if sum not in pre_sum:
            pre_sum[sum] = i 
            
    return l

    
    
    
    

print(LongestSubarraywithSumK())