def LongestConsecutiveSubsequence():
    # arr = [2, 6, 1, 9, 4, 5, 3]
    # arr = [15, 13, 12, 14, 11, 10, 9]
    arr = [1, 9, 3, 10, 4, 20, 2]
    mp = set()
    
    count = 0
    maxi = float("-inf")
    
    for i in range(0 , len(arr)):
        mp.add(arr[i])
        
    for i in mp:
        if i - 1 not in mp:
            count = 1
            
            while i+1 in mp:
                count+=1
                maxi = max(maxi , count)
                i+=1
                
            
    return maxi        
    
print(LongestConsecutiveSubsequence())