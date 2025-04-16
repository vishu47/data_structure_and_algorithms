def transitionPoint(arr, n):
    index = -1
    for i in range(n):
        if arr[i] == 1:
            index = i
            return i
    if index == -1:
        return -1


a = [0, 0, 0, 0, 0]
cc = transitionPoint(a, len(a))
print(cc)
