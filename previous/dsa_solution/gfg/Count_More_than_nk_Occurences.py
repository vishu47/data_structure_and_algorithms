def countOccurence(arr, n, k):
    t = n / k
    fr = {}
    count = 0
    for i in arr:
        fr[i] = fr.get(i, 0) + 1

    for elem in fr.keys():
        if fr[elem] > t:
            count += 1
    return count


# a = [3, 1, 2, 2, 1, 2, 3, 3]
a = [2, 3, 3, 2]
l = 3
cc = countOccurence(a, len(a), l)
print(cc)
