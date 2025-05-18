def RearrangeArrayElementsbySign():
    # arr = [1,2,-4,-5]
    arr = [1,2,-3,-1,-2, 3]
    # arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    
    i , j = 0 , 0
    neg = []
    pos = []
    for i in range(0 , len(arr)):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    
    
    for i in range(0 , len(arr) // 2):
        arr[i*2] = pos[i]
        arr[i*2+1] = neg[i]
    
    return arr
    
    
    # res = [""]*len(arr)
    # # 
    # i = 0
    # p , n = 0 , 1
    
    # while i < len(arr):
    #     if arr[i] > 0:
    #         res[p] = arr[i]
    #         p+=2
    #     else:
    #         res[n] = arr[i]
    #         n+=2
    #     i+=1
    
    # return res

print(RearrangeArrayElementsbySign())