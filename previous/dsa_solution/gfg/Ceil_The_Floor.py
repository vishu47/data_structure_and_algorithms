def getFloorAndCeil(x: int, arr: list) -> list:
    floor = float("inf")
    ceil = float("-inf")
    for i in range(len(arr)):
        if arr[i] >= x and arr[i] <= floor:
            floor = arr[i]
        if arr[i] <= x and arr[i] >= ceil:
            ceil = arr[i]

    if floor == float("inf"):
        floor = -1

    if ceil == float("-inf"):
        ceil = -1

    return [ceil, floor]


x = 17
a = [36, 82, 88, 56, 21, 17, 73, 86]
cc = getFloorAndCeil(x, a)
print(cc)
