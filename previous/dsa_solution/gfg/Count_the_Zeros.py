def countZeroes(arr):
    count = 0
    for i in arr:
        if i == 0:
            count += 1
    return count


a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
cc = countZeroes(a)
print(cc)
