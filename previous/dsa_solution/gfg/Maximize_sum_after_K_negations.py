def maximizeSum(a, n, k):
    # mostSum = 0
    # neg = []
    # a.sort()
    # for i in range(n):
    #     if a[i] < 0:
    #         neg.append(a[i])
    #     else:
    #         mostSum += a[i]
    # for j in range(len(neg)):
    #     if k == 0:
    #         break
    #     neg[j] = -neg[j]
    #     mostSum += neg[j]
    #     k -= 1
    # if k % 2 == 1:
    #     mostSum -= neg[-1]
    # return mostSum
    
    a.sort()
    for i in range(len(a)):
        if a[i] < 0 and k > 0:
            a[i] = -a[i]
            k -= 1

    a.sort()
    if k % 2 == 1:
        a[0] = -a[0]
    return sum(a)


A = [1, 2, 3, 4, 5]
K = 5
cc = maximizeSum(A, len(A), K)
print(cc)
