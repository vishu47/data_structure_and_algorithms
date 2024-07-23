def print2largest(arr):
    # Code Here
    st = 0
    nd = 0

    if len(arr) < 2:
        return -1

    for i in arr:
        if i > st:
            nd = st
            st = i
        elif i > nd and i < st:
            nd = i

    return nd


arr = [12, 35, 1, 10, 34, 1]
print2largest(arr)
