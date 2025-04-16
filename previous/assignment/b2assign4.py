def curzonNumber(n: int) -> bool:
    a = 2**n + 1
    b = 2 * n + 1
    return a % b == 0


print(curzonNumber(14))
