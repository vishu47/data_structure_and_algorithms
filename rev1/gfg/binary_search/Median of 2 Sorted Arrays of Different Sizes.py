def Medianof2SortedArraysofDifferentSizes():
    # a = [2, 3, 5, 8]
    # b = [10, 12, 14, 16, 18, 20]
    a = [-5, 3, 6, 12, 15]
    b = [-12, -10, -6, -3, 4, 10]
    
    # optimal solutions
    elem1 = -1 
    elem2 = -1
    n = len(a) + len(b)
    ind2 = n//2
    ind1 = n//2 - 1
    i, j = 0, 0
    n1 , n2 = len(a) , len(b)
    count = 0
    
    while i < n1 and j < n2:
        if a[i] <= b[j]:
            if count == ind1: elem1 = a[i] 
            if count == ind2: elem2 = a[i]
            count+=1
            i+=1
        else:
            if count == ind1: elem1 = b[j] 
            if count == ind2: elem2 = b[j]
            count+=1
            j+=1
   
    while i < len(a):
        if count == ind1: elem1 = a[i] 
        if count == ind2: elem2 = a[i]
        count+=1
        i+=1
        
    while j < len(b):
        if count == ind1: elem1 = b[j] 
        if count == ind2: elem2 = b[j]
        count+=1
        j+=1
        
    print(elem1 , elem2)
    if n % 2 == 0:
        return (elem1 + elem2)/2
    else:
        return elem2
    
    
    
    
    
    # c = []
    # i , j = 0 , 0
    
    # while i < len(a) and j < len(b):
    #     if a[i] <= b[j]:
    #         c.append(a[i])
    #         i+=1
    #     else:
    #         c.append(b[j])
    #         j+=1
        
    # while i < len(a):
    #     c.append(a[i])
    #     i+=1
        
    # while j < len(b):
    #     c.append(b[j])
    #     j+=1
       
    # # print(len(c) % 2 , len(c) / 2 , len(c)//2, c)
    # clen = len(c)//2
    # # print(c[clen], c[clen - 1] , clen)
    # if len(c) % 2 == 0:
    #     return (c[clen]+ c[clen - 1])/2
    # else:
    #     return c[clen]
        
    
    
print(Medianof2SortedArraysofDifferentSizes())
