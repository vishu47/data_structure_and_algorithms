def majorityElement(A, N):
    candidate = A[0]
    count = 1
    for i in range(1, N):
        if A[i] == candidate:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate = A[i]
            count = 1
    # till this point majority element should be present here
    # if not then we can check in below code
    c = 0
    for j in A:
        if j == candidate:
            c += 1

    if c > (N // 2):
        return candidate
    else:
        return -1


a = [7]
cc = majorityElement(a, len(a))

print(cc)
