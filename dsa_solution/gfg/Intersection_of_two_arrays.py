def NumberofElementsInIntersection(a, b, n, m):

    print(len(set(b).intersection(set(a))))

    # count = 0
    # for num in a:
    #     i = 0
    #     while i < m:
    #         if num == b[i]:
    #             count += 1
    #         i += 1
    # return count


ar1 = [1, 2, 3, 4, 5, 6]
n = len(ar1)
ar2 = [3, 4, 5, 6, 7]
m = len(ar2)
NumberofElementsInIntersection(ar1, ar2, n, m)
