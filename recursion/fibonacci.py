def getFibonacciNumber(k):
    if k == 1:
        return 1
    elif k == 0:
        return 0
    return getFibonacciNumber(k - 1) + getFibonacciNumber(k - 2)


# tc = O(2**n)

# 0 1 1 2 3 5 8 13 21 34 55


def printFibonacciWithLoop(n):
    a = 0
    b = 1
    if n < 1:
        return
    print(a, end=" ")
    for _ in range(1, n):
        print(b, end=" ")
        next = a + b
        a = b
        b = next


def printFibonacci(n):
    for i in range(n):
        print(getFibonacciNumber(i), end=" ")


if __name__ == "__main__":
    # cc = getFibonacciNumber(7)
    # print(cc, "uuu")
    # cc = printFibonacciWithLoop(7)
    # print(cc, "uuu")
    cc = printFibonacci(7)
    print(cc, end=" ")
