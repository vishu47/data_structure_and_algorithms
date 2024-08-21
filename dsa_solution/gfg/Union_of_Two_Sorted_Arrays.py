def findUnion(arr1, arr2, n, m):

    paased = set()
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if arr1[i] not in paased:
                res.append(arr1[i])
            paased.add(arr1[i])
            i += 1
        else:
            if arr2[j] not in paased:
                res.append(arr1[i])
            paased.add(arr2[j])
            j += 1
    while i < len(arr1):
        if arr1[i] not in paased:
            res.append(arr1[i])
        paased.add(arr1[i])
        i += 1
    while j < len(arr2):
        if arr2[j] not in paased:
            res.append(arr2[j])
        paased.add(arr2[j])
        j += 1


a = [1, 2, 3, 4, 5]
b = [1, 2, 3]
l = 5
m = 5
cc = findUnion(a, b, l, m)
print(cc)
