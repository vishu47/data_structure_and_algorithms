def binarysearch(arr, k):
    # for i in range(len(arr)):
    #     if arr[i] == k:
    #         return i
    # return -1

    # binary search
    n = len(arr)
    left = 0
    right = n
    mid = left + (right - left) // 2
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1


a = [1, 2, 3, 4, 5]
m = 4
cc = binarysearch(a, m)
print(cc)
