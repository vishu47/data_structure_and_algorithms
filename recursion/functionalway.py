def func(n):
    if n == 1:
        return 1
    print()
    if n % 2 == 0:
        next = n
    else:
        next = 0
    print(n)
    return n + func(n - 1)


cc = func(5)
print(cc)
