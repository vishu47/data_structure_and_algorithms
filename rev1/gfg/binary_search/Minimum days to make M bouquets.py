def possible(arr , mid , n , k):
    cnt = 0
    noofb = 0
    
    for a in arr:
        if a <= mid: #it means that is bloomed flower
            cnt += 1 
        else:
            # maxi adjacent / required adjacent
            noofb += cnt // k
            cnt = 0
            
    #at the end make sure for last conjecutive add that also
    noofb += cnt / k
    
    if noofb >= n:
        return True
    else:
        return False
    

def flower():
    # arr = [3, 4, 2, 7, 13, 8, 5]
    # m = 3 # no of bouquet
    # n = 2 # no of flower in it
    # arr = [5, 5, 5, 5, 10, 5, 5]
    # m = 2 # no of bouquet
    # n = 3 # no of flower in it
    arr = [5,21,24,26,26,33,41,52,78,98,100]
    m = 2 # no of bouquet
    n = 5 # no of flower in it
    mini , maxi = float("inf") , 0 
    ans = -1
    
    for i in arr:
        maxi = max(maxi , i)
        mini = min(mini , i)
    
    # edhge case when number of flower are less than required flower to make bouquet total flower = n*k(tyotal required flower)
    start , end = mini , maxi
    
    print(start , end)
    
    if len(arr) < m*n:
        return -1 
    
    
    while start <= end:
        mid = (start + end)//2
        
        print(possible(arr ,mid , m , n), start , end , mid , 'possible')
        
        if possible(arr ,mid , m , n):
            end = mid - 1
            ans = mid
        else:
            start = mid + 1
        
    return ans
    
print(flower())