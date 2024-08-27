def hasArrayTwoCandidates(arr, x):
    hs = {}
    # for i in range(len(arr)):
    #     s = x - arr[i]
    #     if s in hs:
    #         print([hs[s], i])
    #         break
    #     hs[arr[i]] = i
    arr[:] = [0] * 3 + [1] * 3 + [2] * 3
    print(arr)


a = [1, 4, 45, 6, 10, 8]
n = 16
hasArrayTwoCandidates(a, n)
