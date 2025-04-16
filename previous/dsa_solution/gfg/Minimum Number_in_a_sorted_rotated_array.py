def minNumber(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return arr[i + 1]


a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
minNumber(a)
