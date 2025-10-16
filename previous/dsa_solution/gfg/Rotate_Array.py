def rotateArr(arr, d, n):
    '''
    when d is more that len of arr then it will once a time same array like 
    d = 5 then after rottaion it will be in the  same position so d = 6 rotaion final will be 5 + 1 so then i need to rotate only once for exact rotaion
    if d = 7 then final d = 5 + 2 fo final d will be 2 only i have to rorate incly by 2 places  
    '''
    # pythonic view
    # D = D % N  # 12%5
    # A[:] = A[D:] + A[:D]

    # print(A)

    r = arr[:d]
    for i in range(d , len(arr)):
        arr[i - d] = arr[i]

    for i in range(len(arr) - d, len(arr) ):
        arr[i] = r[i - (len(arr) - d)]

    print(arr)

a = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = 5
rotateArr(a, d, n)
