def printNos(N):
    if N <= 0:
        return
    printNos(N - 1)
    print(N)


printNos(10)
