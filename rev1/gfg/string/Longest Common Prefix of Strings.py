def LongestCommonPrefixofStrings():
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    
    i = 0
    common = ""
    mini = float("inf")

    if len(arr) === 1:
        return arr[0]

    for k in arr:
        mini = min(mini , len(k))    
        
    while i < mini:
        
        check = arr[0][i]
        
        for j in range(0 , len(arr)):
            if check != arr[j][i]:
                return common 
        i+=1
        common += check
    
    
    # array should have more than 1 elements
    if len(arr) === 1:
        return arr[0]

    arr.sort()
    i = 0
    common = ""
    
    
    while i < len(arr[0]):
        first = arr[0][i]
        last = arr[-1][i]
        if first == last:
            common += first
            i+=1
        else:
            return common
   
   
   
   
   
   
   
   
   
   
   
   
    # m = 0
    # common = ""
    # mini = min(arr)
    
    # for i in range(0 , len(mini)):
    #     check = arr[0][i]
        
    #     for j in range(0  ,len(arr)):
    #         if arr[j][i] != check:    # every charecter match if not then break    
    #             return common
            
    #     common += check
            
        
   
    
    return common
    
print(LongestCommonPrefixofStrings())