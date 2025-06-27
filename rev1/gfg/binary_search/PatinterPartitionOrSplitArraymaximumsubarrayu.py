def check(arr , mid , k):
    count = 1
    sum = 0
    
    for i in range(0, len(arr)):
        if sum + arr[i] <= mid:
            sum += arr[i]
        else:
            sum = arr[i]
            count += 1

    return count
    
def PainterParttition():
    
    arr = [10,20,30,40,50]
    k = 2
    ans = float("inf")
    start, end = min(arr), sum(arr)
    
    while start <= end:
        mid = (start + end)//2

        if check(arr, mid , k) <= k:
            # if painter s are less as we required then mid should be less then more number of painter 
            ans = min(ans, mid) 
            end = mid - 1
        else:
            start = mid + 1
            
    return ans
        

print(PainterParttition())