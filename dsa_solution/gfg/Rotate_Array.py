def rotateArr(A, D, N):
    D = D % N  # 12%5
    A[:] = A[D:] + A[:D]

    print(A)


a = [1, 2, 3, 4, 5]
d = 11
n = 5
rotateArr(a, d, n)
