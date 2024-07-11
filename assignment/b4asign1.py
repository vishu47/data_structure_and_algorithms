def factorial(n):
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    return fact


# a = int(input())
# print(factorial(a))


def pattern(n: int) -> None:
    num = 2
    i = 1
    while i <= n:
        print(num)
        num = (num * 10) + 2
        i += 1


pattern(5)
