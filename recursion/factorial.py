def factoril(n):
    # if n == 1: it will not consider the factorial(0)
    if n == 0 or n == 1:
        return 1
    return n * factoril(n - 1)


cc = factoril(6)
# cc = factoril(0)  gives the infinite loop because it will not return

print(cc)
