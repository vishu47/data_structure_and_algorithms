def threeWayPartition(array, a, b):
    last = len(array) - 1
    start = 0
    mid = 0
    elm = 0

    while mid <= last:
        elm = array[mid]
        if array[mid] < a:
            array[mid], array[start] = array[start], array[mid]
            mid += 1
            start += 1
        elif array[mid] <= b and array[mid] >= a:
            mid += 1
        else:
            array[mid], array[last] = array[last], array[mid]
            last -= 1
    print(array)
    return 1


arr = [10, 7, 6, 1, 4, 10, 5, 2, 7, 5, 3, 3, 8, 3, 8]
aa = 5
bb = 5
cc = threeWayPartition(arr, aa, bb)
print(cc)
