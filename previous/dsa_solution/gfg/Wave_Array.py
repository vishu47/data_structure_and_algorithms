def convertToWave(n: int, arr: list[int]) -> None:
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]


a = [1, 2, 3, 4, 5, 6]
convertToWave(len(a), a)
