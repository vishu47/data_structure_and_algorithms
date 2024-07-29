def equilibriumPoint(arr):
    # l = len(arr)
    # runSum = 0
    # total = 0
    # for num in arr:
    #     total += num

    # for i in range(l):
    #     if runSum == total - runSum - arr[i]:  # 13 - 4 - 5 = 4
    #         return i + 1
    #     runSum += arr[i]

    # return -1

    start = 0
    end = len(arr) - 1
    leftSum = 0
    rightSum = 0

    while start < end:
        if leftSum > rightSum:
            rightSum += arr[end]
            end -= 1
        else:
            leftSum += arr[start]
            start += 1

    if leftSum == rightSum:
        return start + 1
    return -1


x = [1, 3, 5, 2, 2]
res = equilibriumPoint(x)
print(res)
