import math


def FactorsNumber(num: int) -> None:
    i = 1
    while i <= num:
        if num % i == 0:
            print(i, " ")
        i += 1


def OptimalFactorsNumber(num: int) -> None:
    half = num // 2  # it gives the integer value 17/2 = 9
    # print(half)
    i = 1
    while i <= half:
        if num % i == 0:
            print(i, " ")
        i += 1
    print(num, " ")


def SquareOptimalFactorsNumber(num: int) -> None:
    sq = round(num**0.5, 2)
    i = 1
    while i <= sq:
        if num % i == 0 and num // i != i:
            print(i, num // i)
        if num // i == i:
            print(i)

        i += 1


def CountOptimalFactorsNumber(num: int) -> int:
    half = num // 2  # it gives the integer value 17/2 = 9
    count = 0
    # print(half)
    i = 1
    while i <= half:
        if num % i == 0:
            count += 1
        i += 1
    return count + 1


def CountOptimalFactorsNumberSum(num: int) -> int:
    half = num // 2  # it gives the integer value 17/2 = 9
    i = 1
    sum = 0
    while i <= half:
        if num % i == 0:
            sum += i
        i += 1
    return sum + num


# FactorsNumber(20)
# OptimalFactorsNumber(17)
# SquareOptimalFactorsNumber(36)
# print(CountOptimalFactorsNumber(368))
print(CountOptimalFactorsNumberSum(368))
