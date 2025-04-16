def findElement(arr):
    l = len(arr)
    lmax = [0] * l
    lmax[0] = arr[0]

    rmin = [float("inf")] * len(arr)
    rmin[l - 1] = arr[l - 1]

    for i in range(l):
        lmax[i] = max(lmax[i - 1], arr[i])

    for j in range(l - 2, -1, -1):
        print(j, rmin[j], arr[j - 1])
        rmin[j] = min(rmin[j + 1], arr[j + 1])

    for k in range(1, l - 1):
        print(lmax[k], arr[k], rmin[k])
        if arr[k] >= lmax[k] and arr[k] <= rmin[k]:
            return arr[k]
    return -1


# a = [4, 2, 5, 7]
a = [98, 40, 65, 59, 27, 20, 45, 87, 34, 99]
cc = findElement(a)
print(cc)
