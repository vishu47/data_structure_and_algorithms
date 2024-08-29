def partition(arr, low, high):
    pivot = low
    i, j = low, high

    while i < j:
        while arr[i] <= arr[pivot] and i < high:
            i += 1
        while arr[j] >= arr[pivot] and j > low:
            j -= 1

        if i < j:  # this is required
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j


# partition([4, 3, 2, 57, 9, 16], 0, 5)


def quick(arr, low, high):
    if low < high:
        ind = partition(arr, low, high)
        # partition array left and right
        quick(arr, low, ind - 1)
        quick(arr, ind + 1, high)


a = [24, 18, 38, 43, 14, 40, 1, 54]
cc = quick(a, 0, len(a) - 1)
print(a)
