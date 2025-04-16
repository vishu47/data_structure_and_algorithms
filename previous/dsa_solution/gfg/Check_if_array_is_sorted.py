def arraySortedOrNot(arr) -> bool:
    for i in range(1, len(arr) - 1):
        if arr[i - 1] <= arr[i] > arr[i + 1]:
            return False
    return True


# a = [10, 20, 30, 40, 50]
# a = [90, 80, 100, 70, 40, 30]
a = [12, 3, 5, 10, 10, 12, 12, 1, 13, 13, 13, 14, 14, 16, 17, 18, 18, 19]
cc = arraySortedOrNot(a)

print(cc)
