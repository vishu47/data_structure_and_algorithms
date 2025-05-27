def CountOfSubarraywithsumk():
    # logic based on LongestSubarraywithSumK
    # when we find sum then nat same time add that sub array in res 
    
    
    # arr = [9, 4, 20, 3, 10, 5]
    # k = 33
    # arr =  [1, 3, 5]
    # k = 0

    arr = [10, 2, -2, -20, 10] 
    k = -10
    
    # initiallly add o th count edge case
    mp = {0 : 1}
    count = 0 
    sum = 0 
    for i in range(0,len(arr)):
        sum = sum + arr[i]
        
        if sum - k in mp:
            count += mp[sum - k]
            
        mp[sum] = mp.get(sum , 0) + 1
           
           
    print(mp)
    return count
        
    
  
print(CountOfSubarraywithsumk())