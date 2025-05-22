def SetMatrixZero():
    # arr=[[1,1,1],[1,0,1],[1,1,1]]
    # arr=[
    #         [0,1,2,0],
    #         [3,4,5,2],
    #         [1,3,1,5]
    #     ]
    # arr=[[1, -1, 1],
    #     [-1, 0, 1],
    #     [1, -1, 1]]
    
    arr  =[[1, 1 ,5],
           [0,-1,-1]]
    
    
    
    # optimal
    # row = ["0"]*n  ===> matrix[...][j]
    # col = ["0"]*m  ===> matrix[i][...]
        
    #  marking
    n , m = len(arr), len(arr[0])
    col0 = -1
    for i in range(0 , n):
        for j in range(0 , m):
            if arr[i][j] == 0:
                # take 1st row and upadte the element
                arr[i][0] = 0
                # take 1st col expet 0th and upadte the element
                if j != 0 : 
                    arr[0][j] = 0
                else:
                    col0 = 0
                    
    print("step one",arr)
    
    # check for matrix element with saved element n-1*m-1 and                 
    for i in range(1 , n):
        for j in range(1 , m):
            if arr[i][0] == 0 or arr[0][j] == 0:
                    arr[i][j] = 0
        
    print("step one",arr)
    
    # now check for saved col
    for j in range(1 , m):
        if arr[0][0] == 0:
            arr[0][j] = 0    
    
    # now check for saved row
    for i in range(0 , n):
        if col0 == 0:
            arr[i][0] = 0    

    return arr
    
    
    # better
    
    # n , m = len(arr), len(arr[0])
    # row = ["0"]*n
    # col = ["0"]*m
    
    # for i in range(0 , n):
    #     for j in range(0 , m):
    #         if arr[i][j] == 0 :
    #             row[i] = 1
    #             col[j] = 1
    
    # for i in range(0 , n):
    #     for j in range(0 , m):
    #         if row[i] == 1 or col[j] == 1 :
    #             arr[i][j] = 0
                
                
    # print(row,col ,n , m , arr)
    # return arr
    
                
        
print(SetMatrixZero())