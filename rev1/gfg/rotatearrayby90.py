def rotatearrayby90():
    mat=[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    
    # transpose the array row become column
    # tranverse right triangle
    n = len(mat)
    m = len(mat[0])
    
    
    # this is for clock wise 
    
    # transponse of array
    for i in range(0, n):
        for j in range(i+1, m):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    print(mat)
    
    # revrse every array
    for i in range(0, n):
        mat[i].reverse()
    
    
    print(mat)
    
    # for anticlockwise
    
    # transpose of array
    n = len(mat)
    m = len(mat[0])
    for i in range(0 , n):
        for j in range(i+1 , m):
            mat[i][j], mat[j][i] =mat[j][i] , mat[i][j]
            
    # reverse whoole every row
    mat.reverse()
    # for anticlockwise [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    # after transpose reverse whole array
    
    
print(rotatearrayby90())