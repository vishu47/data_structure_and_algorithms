# def print2largest(arr):
#     # Code Here
#     st = 0
#     nd = 0

#     if len(arr) < 2:
#         return -1

#     for i in arr:
#         if i > st:
#             nd = st
#             st = i
#         elif i > nd and i < st:
#             nd = i

#     return nd


def print2largest(arr):
    # Code Here
    max1 = float("-inf")
    min1 = float("inf")
    max2 = float("-inf")
    min2 = float("inf")

    for it in arr:
        if it > max1:
            max1 = it
        if it < min1:
            min1 = it
    for item in arr:
        if item > max2 and item != max1:
            max2 = item
        if item < min2 and item != min2:
            min2 = it

    print(max1, min1, max2, min2)


arr = [12, 35, 1, 10, 34, 1]
print2largest(arr)
