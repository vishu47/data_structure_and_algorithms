def isPossible(N, arr):
    st = ""
    summ = 0
    for num in arr:
        st += str(num)
    for i in st:
        summ += int(i)

    if summ % 3 == 0:
        return 1
    else:
        return 0


a = [40, 50, 90]
isPossible(len(a), a)
