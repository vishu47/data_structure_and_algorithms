from math import sqrt


def primeFactors():
    n = int(input("Enter a number: "))
    # better approch
    # for itself devisible
    # res = 1
    # for num in range(1, n // 2):
    #     if n % num == 0:
    #         res += 1

    # optimal approch
    # n = 36
    # 1 -> 36
    # 2 -> 18
    # 3 -> 12
    # 4 -> 9
    # 5 -> none
    # 6 -> 1

    res = []
    for num in range(1, int(sqrt(n)) + 1):
        print(n % num)
        if n % num == 0:
            res.append(num)
        if n // num != num:
            res.append(n // num)

    print(res)


primeFactors()
