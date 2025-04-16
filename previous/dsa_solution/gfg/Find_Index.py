def findIndex(arr, key):
    left = -1
    right = -1

    for i in range(len(arr)):
        if arr[i] == key and left == -1:
            left = i
            right = i
        elif arr[i] == key:
            right = i

    return [left, right]


a = [6, 5, 4, 3, 5, 5]
x = 5
cc = findIndex(a, x)
print(cc)
