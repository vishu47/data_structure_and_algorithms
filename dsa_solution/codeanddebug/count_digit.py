def evenlyDivides(N):
    arr = str(N)
    count = 0
    for i in arr:
        if int(i) != 0 and N % int(i) == 0:
            count += 1
    return count


st = 22074
cc = evenlyDivides(st)
print(cc)


# https://www.geeksforgeeks.org/problems/count-digits5716/1
