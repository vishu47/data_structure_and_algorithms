def allPairs(x, arr1, arr2):
    res = []
    st = set(arr2)

    for j in range(len(arr1)):
        m = x - arr1[j]
        if m in st:
            res.append([arr1[j], m])
    return res


k = 9
a = [1, 2, 4, 5, 7]
b = [5, 6, 3, 4, 8]
allPairs(k, a, b)
# 1 8
# 4 5
# 5 4
