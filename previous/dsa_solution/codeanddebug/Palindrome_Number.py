def isPalindrome(x: int):
    # sign = -1 if x < 0 else 1
    # xx = abs(x)
    # res = 0
    # while xx != 0:
    #     pop = xx % 10
    #     res = res * 10 + pop
    #     xx = xx // 10
    # final = res * sign
    # return x == final

    xs = str(x)
    nxs = ""
    for i in range(len(xs) - 1, -1, -1):
        nxs += xs[i]
    if nxs == xs:
        return True
    return False


c = -121
cc = isPalindrome(c)

print(cc)
