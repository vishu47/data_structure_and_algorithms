def firstRepeated(arr):
    # for i in range(len(arr)):
    #     for j in range(i + 1, len(arr)):
    #         print(arr[i], arr[j])
    #         if arr[i] == arr[j]:
    #             return i + 1
    # return -1

    dic = {}
    fin = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] in dic:
            fin = i
        else:
            dic[arr[i]] = 1
    return fin


a = [1, 5, 3, 4, 3, 5, 6]
# a = [1, 2, 3, 4]
# a = [7, 4, 0, 9, 4, 8, 8, 2, 4, 5, 5, 1]
cc = firstRepeated(a)
print(cc, "ccc")
