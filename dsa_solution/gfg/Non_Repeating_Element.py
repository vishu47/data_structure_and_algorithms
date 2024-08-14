def firstNonRepeating(arr):
    ls = {}
    for elm in arr:
        ls[elm] = ls.get(elm, 0) + 1
    print(ls)
    for elm in arr:
        if ls[elm] == 1:
            return elm
    return 0


a = [4, -8, 1, -4, -3, -8, -3, -10, 3, -3, 10]
cc = firstNonRepeating(a)
print(cc)
