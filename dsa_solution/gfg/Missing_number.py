def missingNumber(n: int, arr: list[int]) -> int:
    sum = n * (n + 1) / 2
    tsum = 0
    for i in arr:
        tsum += i

    return int(sum - tsum)


a = [1, 4, 3]
cc = missingNumber(4, a)
print(cc)
