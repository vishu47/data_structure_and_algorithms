# pwer of each digit with number of digit in original number
# 1234 = 1**4 + 2**4 + 3**4 + 4**4


def ArmstrongNumber(x):
    num = x
    number = len(str(x))
    # number = int(log10(x))+1
    res = 0
    while num > 0:
        pop = num % 10
        res = res + pop**number
        num = num // 10
    return res == x


n = 1634
cc = ArmstrongNumber(n)
print(cc)
