def PatterOnes(n: int) -> None:
    i = 1
    line = 1
    while i <= n:
        line = (line * 10) + 1
        print(line)
        i += 1


PatterOnes(4)
