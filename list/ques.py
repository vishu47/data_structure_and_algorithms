# a = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]
a = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]

# print app prime number


for i in range(0, len(a)):
    factors = True
    for j in range(2, a[i]):
        if a[i] % j == 0:
            factors = False
            break
    if factors:
        print(a[i], "primeNumber")


# for i in range(0, len(a)):
#     factors = 1
#     for j in range(2, a[i]):
#         if a[i] % j == 0:
#             factors += 1
#     if factors <= 1:
#         print(a[i], "primeNumber")

# def is_prime(num: int):
#     n = 1
#     for i in range(2, num):
#         if num % i == 0:
#             n += 1

#     if n >= 2:
#         return "Not Prime"
#     return "Prime"


# for i in range(0, len(a)):
#     print(is_prime(a[i]), a[i])


# sum of odd number for odd index
# summ = 0
# for i in range(0, len(a)):
#     if i % 2 != 0:
#         summ += a[i]
# print(summ)


# summ = 0
# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         summ += a[i]
# print(summ)


# summ = 0
# for i in a:
#     summ += i
# print(summ)
