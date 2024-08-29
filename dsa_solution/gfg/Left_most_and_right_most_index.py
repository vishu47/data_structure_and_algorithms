def indexes(v, x):
    i = 0
    j = len(v) - 1
    res = [-1, -1]
    while i < len(v):
        if v[i] == x:
            res[0] = i
            break
        i += 1
    while j >= 0:
        if v[j] == x:
            res[1] = j
            break
        j -= 1

    return res


a = [1, 3, 5, 67, 123, 125]
X = 5
cc = indexes(a, X)
print(cc)
