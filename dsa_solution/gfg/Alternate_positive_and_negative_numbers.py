def rearrange(arr, n):
    neg = []
    pos = []

    for elm in arr:
        if elm < 0:
            neg.append(elm)
        else:
            pos.append(elm)

    if len(pos) > len(neg):
        l = len(neg)

        for j in range(l):
            arr[j * 2] = pos[j]
            arr[j * 2 + 1] = neg[j]
        # print(arr)
        for k in range(l, len(pos)):
            # print(k + l)
            arr[k + l] = pos[k]
    else:
        l = len(pos)
        for j in range(l):
            arr[j * 2] = pos[j]
            arr[j * 2 + 1] = neg[j]
        # print(arr)
        for k in range(l, len(neg)):
            # print(k + l)
            arr[k + l] = neg[k]
    # print(arr)


# a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
a = [93, 85, -59, 45, -89, -41, -4, -98, 79, -12]
rearrange(a, len(a))
