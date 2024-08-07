def minDist(arr, n, x, y):
    ans = float("inf")
    left = -1
    right = -1
    for i in range(len(arr)):
        if arr[i] == x:
            left = i
        if arr[i] == y:
            right = i
        if left != -1 and right != -1:
            ans = min(ans, abs(right - left))

    if left == -1 or right == -1:
        return -1
    return ans


# x = [1, 3, 2]
x = [5, 3, 1, 8, 3, 23, 2]
a = 2
b = 5
cc = minDist(x, len(x), a, b)
print(cc)
