# find breakpoint 
# find swap with lowest number but greater than breakpoint number
# remaining part would be always in decending order then reverse that array and done 
def nextpermutation():
    arr = [3,2,1]
    
    bindex = -1
    # edge case
    
    
    for i in range(len(arr) - 2 , -1 , -1):
        if arr[i] < arr[i+1]:
            bindex = i
            break
    
       
    if bindex == -1:
        arr.reverse()
        return arr 
    
    for i in range(len(arr) -1 , -1 , -1):
        if arr[i] > arr[bindex]:
            arr[bindex] , arr[i] =  arr[i] , arr[bindex]
            break
        
    
    rez = arr[bindex+1:]
    rez.reverse()
    arr[bindex+1:] = rez
    
    return arr
    
print(nextpermutation())