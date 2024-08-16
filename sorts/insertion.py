def insertionSort(arr):
    l = len(arr)
    for i in range(0, l - 1):
        j = i - 1
        key = arr[i]
        print(key, j)
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(arr)


a = [0, 9, 3, 5, 7, 7, 54]
cc = insertionSort(a)
print(cc)
