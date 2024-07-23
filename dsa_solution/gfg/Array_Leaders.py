def leaders(n, arr):
    lead = []
    lastELem = arr[-1]
    lead.append(lastELem)

    for i in range(n - 2, -1, -1):
        if arr[i] >= lastELem:
            lead.append(arr[i])
            lastELem = arr[i]

    return lead[::-1]


arr = [16, 17, 4, 3, 5, 2]
leaders(len(arr), arr)
