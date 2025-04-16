def minValue(arr1, arr2):
    arr1.sort()
    arr2.sort()
    res = []
    sum = 0
    for i in range(len(arr2) - 1, -1, -1):
        res.append(arr2[i])
    for i in range(len(arr1)):
        sum = sum + (arr1[i] * res[i])
    return sum


a = [3, 1, 1]
b = [6, 5, 4]
minValue(a, b)
