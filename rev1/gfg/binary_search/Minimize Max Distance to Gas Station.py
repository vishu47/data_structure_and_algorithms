def check(arr , mid , k) :
    count = 0 
    
    for i in range(0 , len(arr) - 1):
        
        diff = arr[i+1] - arr[i]
        
        if diff > mid:
            count += diff // mid
        
    if count > k:
        return False
    else:
        return True
             
        

def  MinimizeMaxDistancetoGasStation():
    
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 9
    
    start , end = 0 , max(arr) - min(arr)
    mid = 0
    ans = -1    
    while end - start <= 0.000001:
        
        mid = (start + end)/2
        
        if (check(arr,mid,k)):
            ans = mid
            end = mid - 0.000001
            
        else:
            start = mid + 0.000001
            
    return round(ans , 6) 

print(MinimizeMaxDistancetoGasStation())