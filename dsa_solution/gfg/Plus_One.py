def increment(arr, N):
    for i in range(N - 1, -1, -1):
        arr[i] = arr[i] + 1
        if arr[i] <= 9:
            return arr
        arr[i] = 0
    arr.insert(0, 1)
    return arr


a = [9, 9, 9]
cc = increment(a, len(a))

print(cc)
