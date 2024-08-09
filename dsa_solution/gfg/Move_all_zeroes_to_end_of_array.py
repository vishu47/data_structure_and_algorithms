def pushZerosToEnd(arr, n):
    nonZ = 0
    for i in range(n):
        if arr[i] != 0:
            arr[nonZ] = arr[i]
            nonZ += 1
    for j in range(nonZ, n):
        arr[j] = 0


# fill first with the non zeror elements and then fill other places with thw zero

a = [3, 5, 0, 0, 4, 0, 8, 7]
pushZerosToEnd(a, len(a))
