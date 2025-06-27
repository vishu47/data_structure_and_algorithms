def noOfStudent(arr , mid , k):
    
    stud = 1
    pages = 0
    
    for i in range(0 , len(arr)):
        if pages + arr[i] <= mid:
            pages += arr[i]
        else:
            stud += 1
            pages = arr[i]
            
    return stud
    

def BookAllocationProblem():
    
    arr = [12, 34, 67, 90]
    k = 2
    
    start , end = max(arr) , sum(arr)

    if len(arr) < k:
        return -1

    while start <= end:
        
        mid = (start + end)//2
        # foir increasing the number of student we less the mid value by decreasing the end = mid - 1
        if noOfStudent(arr , mid , k ) <= k:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1


    return ans

print(BookAllocationProblem())