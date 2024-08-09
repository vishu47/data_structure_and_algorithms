def rearrange(arr, n):
    neg = []
    pos = []

    for elm in arr:
        if elm < 0:
            neg.append(elm)
        else:
            pos.append(elm)
    print(pos, neg)
    pi = 0
    ni = 0
    for i in range(0, n):
        print(i % 2 == 0)
        if i % 2 == 0:
            if len(pos) <= i:
                print(pi, pos[pi])
                arr[i] = pos[pi]
            pi += 1
        else:
            print(len(neg) <= i, len(neg), i)
            if len(neg) <= i:
                print(ni, neg[ni])
                arr[i] = neg[ni]
                ni += 1
    print(arr)


a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
rearrange(a, len(a))
