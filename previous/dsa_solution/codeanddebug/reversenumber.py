def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    res = 0
    x = abs(x)

    while x != 0:
        pop = x % 10
        x = x // 10
        res = res * 10 + pop

    return res * sign


num = 12345
cc = reverse(num)

print(cc)
