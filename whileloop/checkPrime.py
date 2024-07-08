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


def checkPrime(num: int) -> bool:
    count = CountOptimalFactorsNumber(num)
    return count == 2


print(checkPrime(17))
