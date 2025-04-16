def hasArrayTwoCandidates(arr, x):
    hs = {}  # unique and take hashable values(immutable data int,string,tuple,boolean)
    for i in arr:
        if x - i in hs:
            return True
        hs[i] = hs.get(i, 0) + 1
    return False


a = [1, 2, 4, 3, 6]
c = 11
p = hasArrayTwoCandidates(a, c)
print(p)
