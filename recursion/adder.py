count = 0


def adder(n):
    global count
    if n % 2 == 0:
        count += n
    if n < 1:
        return count
    return adder(n - 1)


cc = adder(8)
print(cc)
