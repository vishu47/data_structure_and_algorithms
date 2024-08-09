def firstElementKTime(n, k, arr):
    hs = {}
    for i in arr:
        hs[i] = hs.get(i, 0) + 1
        if hs[i] == k:
            return i
    return -1


l = 2
a = [1, 7, 4, 3, 4, 8, 7]
cc = firstElementKTime(len(a), l, a)
print(cc)
