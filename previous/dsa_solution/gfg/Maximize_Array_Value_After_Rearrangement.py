def Maximize(a):
    MOD = 10**9 + 7
    a.sort()
    prod = 0
    for i in range(len(a)):
        prod += (a[i] * i) % MOD
    return prod


arr = [5, 3, 2, 4, 1]
cc = Maximize(arr)
print(cc)
