def sumOfDivisors(N):
    i = 1
    count = 0
    while i <= N:
        for j in range(1, i + 1):
            if i % j == 0:
                count += j
        i += 1
    return count


n = 4
cc = sumOfDivisors(n)
print(cc)
