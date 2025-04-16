def frequencyCount(arr, N, P):
    fre = {}
    for i in range(N):
        fre[arr[i]] = fre.get(arr[i], 0) + 1

    print(fre)

    for j in range(N):
        arr[j] = fre.get(j + 1, 0)

    print(arr)


a = [3, 3, 3, 3]
p = 3
frequencyCount(a, len(a), p)
