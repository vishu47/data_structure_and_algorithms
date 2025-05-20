def majorityElement():
    arr = [4,4,2,4,3,4,4,3,2,4]
    # arr = [2,2,1,1,1,2,2]
    # mp = {}
    # for i in arr:
    #     if i in mp:
    #        mp[i] = mp[i] + 1
    #     else:
    #         mp[i] = 1
    # n = len(arr)//2
    # f = -1
    # for [key , val] in mp.items():
    #     if val > n:
    #         return key
    
    
    # moore voting algo
    # suppose 1st as mejotity and if arr[i] wquals to mejority counte + 1 else count - 1 and at last you will get mejority element 
    # you have mejority element and chekc is it is greater than m//2 
    m = 0
    c = 0
    for i in range(0 , len(arr)):
        if c == 0:
            m = arr[i]
            
        if m == arr[i]:
            c+=1
        else:
            c-=1
    n = len(arr)//2 
    
    count = 0
    for i in arr:
        if i == m:
            count+=1 
                   
    if count > n:
        return m 
    return -1       
    
    print(m, count)
    
print(majorityElement())