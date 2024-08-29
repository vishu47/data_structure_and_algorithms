def findUnion(arr1, arr2, n, m):

    # paased = set()
    # res = []
    # i, j = 0, 0
    # while i < len(arr1) and j < len(arr2):
    #     if arr1[i] <= arr2[j]:
    #         if arr1[i] not in paased:
    #             res.append(arr1[i])
    #         paased.add(arr1[i])
    #         i += 1
    #     else:
    #         if arr2[j] not in paased:
    #             res.append(arr1[i])
    #         paased.add(arr2[j])
    #         j += 1
    # while i < len(arr1):
    #     if arr1[i] not in paased:
    #         res.append(arr1[i])
    #     paased.add(arr1[i])
    #     i += 1
    # while j < len(arr2):
    #     if arr2[j] not in paased:
    #         res.append(arr2[j])
    #     paased.add(arr2[j])
    #     j += 1

    # a = set(arr1)
    # b = set(arr2)
    # uu = a.union(b)
    # res = []
    # for i in uu:
    #     res.append(i)
    # res.sort()
    # return res

    i, j = 0, 0
    res = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
        else:
            if len(res) == 0 or res[-1] != arr2[j]:
                res.append(arr2[j])
            j += 1
    while i < n:
        if len(res) == 0 or res[-1] != arr1[i]:
            res.append(arr1[i])
        i += 1
    while j < m:
        if len(res) == 0 or res[-1] != arr2[j]:
            res.append(arr2[j])
        j += 1
    return res


a = [-7, 8]
b = [-8, -3, 8]
l = 2
m = 3
cc = findUnion(a, b, len(a), len(b))
print(cc)
