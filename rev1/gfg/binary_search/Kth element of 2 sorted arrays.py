def Kthelementof2sortedarrays():
    # a = [2, 3, 6, 7, 9]
    # b = [1, 4, 8, 10]
    # k = 5
    a = [100, 112, 256, 349, 770]
    b = [72, 86, 113, 119, 265, 445, 892]
    k = 7
    n1 , n2 = len(a) , len(b)
    count = 0
    i , j = 0 , 0 
    ans = -1
            
    while i < n1 and j < n2:
        if a[i] < b[j]: 
            if count == k-1:
                ans = a[i]
            count += 1
            i+=1
        else:
            if count == k-1:
                ans = b[j]
            count += 1    
            j+=1
    while i < n1:
        if count == k-1:
            ans = a[i]
        count += 1
        i+=1
    while j < n2:
        if count == k-1:
            ans = b[j]
        count += 1
        j+=1
            
    return ans
    
print(Kthelementof2sortedarrays())