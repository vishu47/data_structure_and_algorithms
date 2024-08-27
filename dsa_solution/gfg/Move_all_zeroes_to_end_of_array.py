def pushZerosToEnd(arr, n):
    # nonZ = 0
    # for i in range(n):
    #     if arr[i] != 0:
    #         arr[nonZ] = arr[i]
    #         nonZ += 1
    # for j in range(nonZ, n):
    #     arr[j] = 0
    # print(arr)

    i = 0
    while i < n:
        if arr[i] == 0:
            break
        i += 1
    j = i + 1

    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    print(arr)


# fill first with the non zeror elements and then fill other places with thw zero

a = [3, 5, 0, 0, 4, 0, 8, 7]
cc = pushZerosToEnd(a, len(a))
print(cc)
