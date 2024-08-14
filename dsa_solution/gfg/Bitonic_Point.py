def findMaximum(arr, n):
    el = 0
    for i in arr:
        el = max(el, i)
    return el


a = [1, 15, 25, 45, 42, 21, 17, 12, 11]
cc = findMaximum(a, len(a))
print(cc)
