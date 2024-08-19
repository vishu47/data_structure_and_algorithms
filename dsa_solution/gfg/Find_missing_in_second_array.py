def findMissing(a, b, n, m):
    hsb = {}
    res = []
    for it in b:
        hsb[it] = it
    for item in a:
        if item not in hsb:
            res.append(item)
    return res


x = {1, 2, 3, 4, 5, 10}
y = {2, 3, 1, 0, 5}
cc = findMissing(x, y, len(x), len(y))
print(cc)
