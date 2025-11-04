def searchinrotatedsortedarray():
    arr = [4,5,6,7,0,1,2,3]
    k = 0
    
    # ans = -1
    # mid = 0
    # start , end = 0 , len(arr) - 1
    
    # while start <= end:
        
    #     mid = (start+end)//2\
            
    #     if arr[mid] == k:
    #         ans = mid
        
    #     if  arr[mid] > arr[start]:
    #         if k >= arr[start] and k < arr[mid]:
    #             end = mid - 1
    #         else:
    #             start = mid + 1
    #     else:
    #         if k > arr[mid] and k <= arr[end]:
    #             start = mid + 1
    #         else:
    #             end = mid - 1
            
    # return ans


    ans = -1
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == k:
            ans = mid
            break  # stop searching when found

        # Left half is sorted
        if arr[start] <= arr[mid]:
            if arr[start] <= k < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # Right half is sorted
        else:
            if arr[mid] < k <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return ans
    

print(searchinrotatedsortedarray())