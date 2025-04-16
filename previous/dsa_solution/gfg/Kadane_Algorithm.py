def maxSubArraySum(arr):
    Sum = float("-inf")
    maxi = 0
    for i in range(len(arr)):
        Sum += arr[i]
        if Sum > maxi:
            maxi = Sum
        if Sum < 0:
            Sum = 0

    return maxi


a = [-2, -3, 4, -1, -2, 1, 5, -3]
cc = maxSubArraySum(a)
print(cc)
