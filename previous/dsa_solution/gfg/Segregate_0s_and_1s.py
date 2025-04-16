def segregate0and1(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        if arr[end] == 1:
            end -= 1
        elif arr[start] == 1 and arr[end] != 1:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        else:
            start += 1
    return arr


a = [0, 0, 0, 0, 1, 1, 0]
cc = segregate0and1(a)
print(cc)
