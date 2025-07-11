# Maximum Subarray Sum – Kadane's Algorithm
# loop and sum if sum is less than 0 then sum replace with 0 and move forword 
def KadanesAlgorithm():
    arr = [-2, -4]
    # msum = float("-inf")
    # sum = 0
    # for i in range(0, len(arr)):
    #     for j in range(i, len(arr)):
    #         sum = sum + arr[j]
    #         msum = max(msum , sum)
            
    #     sum = 0
    # print(msum)
    
    msum = float("-inf")
    sum = 0
    start = -1
    st , en = -1, -1
    for i in range(0 , len(arr)):
        # whenever sum 0 it will start from i 
        if sum == 0 : start = i
        
        sum = sum + arr[i]
        
        if sum > msum:
            msum = sum
            st = start 
            en = i + 1
        
        if sum < 0: 
            sum = 0
            
    print(st , en, msum)
    return arr[st:en]
    
    
print(KadanesAlgorithm())
 