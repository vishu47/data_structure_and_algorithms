def unionof2sortedarr():
    a = [-7, 8]
    b = [-8,-3, 8]
    # a = [1, 2, 3, 4, 5] 
    # b = [1, 2, 3, 6, 7]
    # a = [-5,-4,-1,1,7]
    # b = [-3,0,1,8]
    # c = set(a)
    # for i in b:
    #     if i not in c:
    #         c.add(i)
            
    # return list(c)

    i , j = 0, 0
    
    n = len(a)
    m = len(b)
    res = []
    '''
    2 pointer approch check which is smaller and pushed to res and check for 1st time or check for if last element is not same then only push otherwise next condition
    '''
    while i < n and j < m:
        if a[i] < b[j]:
            if len(res) == 0 or res[-1] != a[i]:
                res.append(a[i])
            i+=1
        else:
            if len(res) == 0 or res[-1] != b[j]:
                res.append(b[j])
            j+=1
        
    while i < n:
        if len(res) == 0 or res[-1] != a[i]:
            res.append(a[i])
        i+=1
        
    while j < m:
        if len(res) == 0 or res[-1] != b[j]:
            res.append(b[j])
        j+=1
        
    return res
print(unionof2sortedarr())