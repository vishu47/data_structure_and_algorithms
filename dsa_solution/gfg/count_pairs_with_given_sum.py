def getPairsCount(arr, sum):
    #     l = len(arr)
    #     count = 0
    #     for i in range(l):
    #         for j in range(i + 1, l):
    #             x = arr[i] + arr[j]
    #             if x == sum:
    #                 count += 1
    #     print(count)

    # hashing methods
    l = len(arr)
    hs = {}
    count = 0
    for i in arr:
        print(hs, count)
        if sum - i in hs:
            count += hs[sum - i]
        if i in hs:
            hs[i] += 1
        else:
            hs[i] = 1

    return count


ar = [1, 1, 1, 1]
getPairsCount(ar, 2)
