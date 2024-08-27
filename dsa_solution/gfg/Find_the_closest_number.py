def findClosest(n: int, k: int, arr: list[int]) -> int:
    low = 0
    high = 0
    for i in range(0, n):
        if arr[i] < k:
            low = arr[i]
        else:
            high = arr[i]
            break

    absLow = abs(low - k)
    absHigh = abs(high - k)

    if absLow < absHigh:
        return low
    elif absLow > absHigh:
        return high
    else:
        return max(low, high)


a = [1, 2, 3, 5, 6, 8, 9]
l = 4
cc = findClosest(len(a), l, a)
print(cc)
