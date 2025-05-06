def pushZerosToEnd():
    arr = [3,5,0,4,0]
    nz = 0
    for i in range(0 , len(arr)):
        if(arr[i] != 0):
            arr[nz] = arr[i]
            nz+=1
    
    while nz < len(arr):
        arr[nz] = 0
        nz += 1
    
    return arr

print(pushZerosToEnd())