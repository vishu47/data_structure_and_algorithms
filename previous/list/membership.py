lst = [1, 2, 5, 7, 5, 7, 55, 6, 6, 6, 7, 8, 9, 9, 1]

res = []
for i in range(len(lst)):
    if lst[i] not in res:
        res.append(lst[i])

print(res)
