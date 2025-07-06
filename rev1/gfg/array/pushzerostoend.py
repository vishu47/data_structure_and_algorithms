def pushZerosToEnd():
    arr = [3,5,0 ,9 ,0,4,8]
    # nz = 0
    # for i in range(0 , len(arr)):
    #     if(arr[i] != 0):
    #         arr[nz] = arr[i]
    #         nz+=1
    
    # while nz < len(arr):
    #     arr[nz] = 0
    #     nz += 1
    
    # return arr
    j = -1
    
    for i in range(0 , len(arr)):
        if arr[i] == 0:
            j = i
            break
        
    if j == -1:
        return arr
    
    for i in range(j+1 , len(arr)):
        if arr[i] != 0:
            print(i , j)
            arr[i] ,arr[j] = arr[j], arr[i]
            j+=1
            
    print(arr)
                    
print(pushZerosToEnd())