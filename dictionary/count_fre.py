lst = [4, 3, 4, 5, 6, 5, 4, 4, 2, 1, 2, 3, 3, 4, 5, 6]

ds = {}
for num in lst:
    if num in ds:
        ds[num] += 1
    ds[num] = 1

# print(ds)


d = {}
for num in lst:
    d[num] = d.get(num, 0) + 1


print(d)

maxVal = 0
maxKey = ""
for key, val in d.items():
    if val > maxVal:
        maxVal = val
        maxKey = key

print(f"{maxKey} : {maxVal}")
