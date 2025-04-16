def sumCal(a, b):

    # sum = 0
    # if a <= b:
    #     i = a
    #     while i <= b:
    #         sum += i
    #         i += 1
    # elif a >= b:
    #     i = b
    #     while i <= a:
    #         sum += i
    #         i += 1
    # return sum

    # using swap method
    sum = 0
    if a >= b:
        i = b
        end = a
    else:
        i = a
        end = b

    while i <= end:
        sum += i
        i += 1
    return sum


a = int(input())
b = int(input())
print(sumCal(a, b))
