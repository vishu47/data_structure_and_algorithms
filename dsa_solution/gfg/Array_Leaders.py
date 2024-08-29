def leaders(n, arr):
    largeRight = -1
    lead = []
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > largeRight:
            lead.append(arr[i])
            largeRight = max(largeRight, arr[i])

    i, j = 0, len(lead) - 1
    while i <= j:
        lead[i], lead[j] = lead[j], lead[i]
        i += 1
        j -= 1
    return lead


arr = [16, 17, 4, 3, 5, 2]
cc = leaders(len(arr), arr)
print(cc)
