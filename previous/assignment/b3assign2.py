def countNumber(a, b):

    if a >= b:
        i = b
        end = a
    else:
        i = a
        end = b

    count = 0
    while i <= end:
        if i % 3 == 0 and i % 5 == 0:
            count += 1
        i += 1
    return count


a = int(input())
b = int(input())
print(countNumber(a, b))
