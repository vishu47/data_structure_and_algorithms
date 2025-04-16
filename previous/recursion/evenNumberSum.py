def evenNumberSum(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + evenNumberSum(n - 1)
    else:
        return evenNumberSum(n - 1)


cc = evenNumberSum(10)
print(cc)
