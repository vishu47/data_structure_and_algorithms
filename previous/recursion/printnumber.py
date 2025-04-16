count = 0


def printNumber(num, i=0):
    global count

    # withouut back tracking answer avaiable and print
    # if num < 0:
    #     return
    # print(num)
    # printNumber(num - 1)

    # with back tracking answer but print when function ends
    # if num < 0:
    #     return
    # printNumber(num - 1)
    # print(num)

    # if i > num:
    #     return count
    # if i % 2 == 0:
    #     count += i
    # return printNumber(num, i + 1)

    if i > num:
        return


n = int(input("Enter number : "))
cc = printNumber(n)
print(cc)
