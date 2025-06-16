def giveSum(arr , mid):
    sum = 0
    
    for i in arr:
        sum += (i+mid-1)//mid

    return sum


def findDivisorMinimum():
    # arr = [1,2,3,4,5]
    # l = 8
    arr = [8,4,2,3]
    # l = 10
    arr = [1,2,5,9]
    l = 6
    start = 1
    end = float("-inf")  # maxi
    ans = 0
    
    for i in arr:
        end = max(end , i)
        
    while start <= end:
        
        mid = (start + end)//2 
        
        if giveSum(arr , mid) <= l:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return ans

print(findDivisorMinimum())
        
        

    
    
    