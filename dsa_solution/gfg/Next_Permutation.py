def nextPermutation(N, arr):
    bindex = -1
    for i in range(N - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            bindex = i
            break
    if bindex == -1:
        return list(reversed(arr))

    for j in range(N - 1, i, -1):
        if arr[j] > arr[bindex]:
            arr[j], arr[bindex] = arr[bindex], arr[j]
            break

    reveLast = arr[bindex + 1 :]
    arr[:] = arr[: bindex + 1] + list(reversed(reveLast))
    return arr


a = [3, 2, 1]
cc = nextPermutation(len(a), a)
print(cc)
