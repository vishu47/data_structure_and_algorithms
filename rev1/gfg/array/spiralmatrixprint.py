def spiralmatrixprint():
    arr = [
        [1, 2, 3],
        [4 ,5 ,6],
        [7, 8, 9]
    ]
    # arr = [
    #         [1, 2, 3, 4]
    #     ]
    
    n, m = len(arr) , len(arr[0])
    res = []
    # right bottom left top
    
    top , left = 0 , 0 
    right = m
    bottom = n
    
    while left < right and top < bottom:
    # right
        for i in range(left , right):
            res.append(arr[top][i])
        top+=1
        # bottom
        for i in range(top , bottom):
            # right = 3
            res.append(arr[i][right - 1])
        right-=1
        
        # # left
        # 2 to 0
        
        # top added and then top == bottom as bottom was 1 and top was 0 + 1 top+=1
        if top < bottom : 
            for i in range(right - 1 , left - 1, -1):
                # bottom = 3
                res.append(arr[bottom - 1][i])
            bottom-=1
        
        # bottom
        # right reduced and then left == right
        if left < right: 
            for i in range(bottom - 1, top - 1, -1):
                res.append(arr[i][left])
                
            left+=1
        
    
    
    print(res)
print(spiralmatrixprint())
    