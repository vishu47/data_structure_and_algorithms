# # avg and best case
# def bubbleSort(arr, n):
#     l = n - 2  # except the last number to prevent index error
#     for i in range(l, -1, -1):
#         for j in range(0, i + 1):  # will run upto i
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr


# # tc -> O(n^2)
# # sc -> O(1)

# a = [6, 5, 4, 3, 2, 1]
# cc = bubbleSort(a, len(a))
# print(cc)


def testBubble(arr):
    l = len(arr)
    for i in range(l - 1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


a = [1, 3, 5, 7, 7, 54, 3, 2, 2, 2, 3, 5, 6, 4, 7, 8, 0, 5, 2]
testBubble(a)
