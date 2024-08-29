def pairWithMaxSum(arr):
    fst = 0
    nd = 0
    for i in arr:
        if i > fst:
            nd = fst
            fst = i
        elif i < fst and i > nd:
            nd = i
    return nd + fst


# a = [4, 3, 1, 5, 6]
a = [228, 394, 463, 227, 388, 757, 782, 238, 967]  # 1539
cc = pairWithMaxSum(a)
print(cc)
