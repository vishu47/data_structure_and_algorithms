def lenOfLongSubarr(arr, n, k):
    # only works for positive integer
    # maxil = -1
    # l = 0
    # r = 0
    # s = 0
    # while l < len(arr) and r < len(arr):
    #     s += arr[r]
    #     if s <= k:
    #         r += 1
    #         maxil = max(maxil, r - l)
    #     else:
    #         s -= arr[l]
    #         l += 1
    #         r += 1

    # return maxil

    # optimal solu
    s = 0
    hs = {}
    maxi = -1
    for i in range(n):
        s += arr[i]
        if s == k:
            maxi = i + 1
        # will check this remender in hash map
        rem = s - k
        if rem in hs:
            l = i - hs[rem]
            maxi = max(maxi, l)
        if s not in hs:
            hs[s] = i

    print(maxi)


a = [-13, 0, 6, 15, 16, 2, 15, -12, 17, -16, 0, -3, 19, -3, 2, -9, -6]
x = 15
lenOfLongSubarr(a, len(a), x)
