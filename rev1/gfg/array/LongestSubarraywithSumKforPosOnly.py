def LongestSubarraywithSumKforPosOnly():
    '''
    2 pointer approch if sum is greater then remove previous element and update j if equal then posible subarray
    '''
    arr = [1,2,3,1,1,1,1,3,3]
    k = 6
    sum = 0
    l = 0
    j = 0
    
    for i in range(0 , len(arr)):
        sum += arr[i]
        
        if sum == k:
            l = max(l , i - j + 1)
        
        if sum > k:
            sum = sum - arr[j]
            j+=1
            
    return l


print(LongestSubarraywithSumKforPosOnly())        