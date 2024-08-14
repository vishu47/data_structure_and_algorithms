def findExtra(n, a, b):
    bs = set(b)
    for i in range(n):
        if a[i] not in bs:
            return i


aa = [2, 4, 6, 8, 9, 10, 12]
bb = [2, 4, 6, 8, 10, 12]
cc = findExtra(len(aa), aa, bb)
print(cc)
