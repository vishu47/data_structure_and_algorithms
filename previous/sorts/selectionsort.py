def selection(arr):
    l = len(arr)
    for i in range(l):
        min = i
        for j in range(i + 1, l):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


a = [4, 1, 3, 9, 7]
cc = selection(a)
print(cc)
