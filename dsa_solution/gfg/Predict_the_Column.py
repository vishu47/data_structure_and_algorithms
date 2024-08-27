def columnWithMaxZeros(arr, N):
    col = float("inf")
    zeros = 0
    for i in range(N):
        countZ = 0
        for j in range(N):
            if arr[j][i] == 0:
                countZ += 1

        if countZ > zeros:
            zeros = countZ
            col = i

    if col == float("inf"):
        return -1
    else:
        return col


a = [
    [1, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0],
]
cc = columnWithMaxZeros(a, len(a))
print(cc)
