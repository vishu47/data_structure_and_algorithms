from typing import List


def zigZag(n: int, arr: List[int]) -> None:
    flag = "<"
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1] and flag == "<":
            arr[i + 1], arr[i] = arr[i], arr[i + 1]
        if arr[i] < arr[i + 1] and flag == ">":
            arr[i + 1], arr[i] = arr[i], arr[i + 1]
        if flag == ">":
            flag = "<"
        else:
            flag = ">"


a = [4, 3, 7, 8, 6, 2, 1]
zigZag(len(a), a)
