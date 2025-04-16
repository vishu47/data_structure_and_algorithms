def findKRotation(arr):
    count = 0
    flag = 0
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            flag = True
        if flag:
            count += 1
    # print(count)
    return count


a = [5, 1, 2, 3, 4]
# a = [1, 2, 3, 4, 5]
# a = [6, 9, 2, 4]
findKRotation(a)
